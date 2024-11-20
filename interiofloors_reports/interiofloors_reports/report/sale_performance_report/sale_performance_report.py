import frappe
from frappe import _

# Define the item groups you want to include in the report
ALLOWED_ITEM_GROUPS = [
    "Laminate Floors",
    "HydroCore+ SPC Floor",
    "Rinovo Panels (4.5\"x9.5\")",
    "Rinovo PVC Skirting",
    "FlexiStone (Marble Sheet)",
    "FlexiRock (PU Stone)"
]

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Customer Group"), "fieldname": "customer_group", "fieldtype": "Data", "width": 250},
        {"label": _("Account Manager"), "fieldname": "account_manager", "fieldtype": "Data", "width": 220},
        {"label": _("Item Group"), "fieldname": "item_group", "fieldtype": "Data", "width": 220},
        {"label": _("Quantity Sold"), "fieldname": "quantity_sold", "fieldtype": "Float", "width": 220},
        {"label": _("Total Amount"), "fieldname": "total_amount", "fieldtype": "Currency", "width": 220},
    ]

def get_data(filters):
    conditions = []

    # Apply filter for allowed item groups
    conditions.append("si_item.item_group IN %(allowed_item_groups)s")
    filters["allowed_item_groups"] = ALLOWED_ITEM_GROUPS

    if filters.get("from_date") and filters.get("to_date"):
        conditions.append("si.posting_date BETWEEN %(from_date)s AND %(to_date)s")

    if filters.get("customer_group"):
        conditions.append("si.customer_group = %(customer_group)s")

    if filters.get("territory"):
        conditions.append("si.territory = %(territory)s")

    if filters.get("account_manager"):
        conditions.append("customer.account_manager = %(account_manager)s")

    where_clause = " AND ".join(conditions) if conditions else "1=1"

    data = frappe.db.sql(f"""
        SELECT
            si.customer_group AS customer_group,
            si_item.item_group AS item_group,
            SUM(si_item.qty) AS quantity_sold,
            SUM(si_item.amount) AS total_amount,
            customer.account_manager AS account_manager

        FROM
            `tabSales Invoice` si
        JOIN
            `tabSales Invoice Item` si_item ON si.name = si_item.parent
        JOIN
            `tabCustomer` customer ON si.customer = customer.name
        WHERE
            si.docstatus = 1 AND {where_clause}
        GROUP BY
            si.customer_name, si_item.item_group
        ORDER BY
            si.customer_name ASC
    """, filters, as_dict=True)

    return data

def get_all_child_item_groups(item_group):
    """Recursively get all child item groups for a selected parent group."""
    child_groups = frappe.db.get_all("Item Group", filters={"parent_item_group": item_group}, pluck="name")
    all_groups = child_groups[:]
    for group in child_groups:
        all_groups.extend(get_all_child_item_groups(group))
    return all_groups
