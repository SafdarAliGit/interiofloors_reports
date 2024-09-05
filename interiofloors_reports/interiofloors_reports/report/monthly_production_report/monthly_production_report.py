import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_conditions(filters):
    conditions = ""
    if filters.get("month") and filters.get("year"):
        conditions += " AND MONTH(dp.date) = %(month)s"
        conditions += " AND YEAR(dp.date) = %(year)s"
    return conditions


def get_columns():
    return [
        {
            "fieldname": "item_name",
            "label": _("Item Name"),
            "fieldtype": "Data",
            "width": 200
        },
        {
            "fieldname": "type_of_product",
            "label": _("Type of Product"),
            "fieldtype": "Data",
            "width": 150
        },

        {
            "fieldname": "uom",
            "label": _("UOM"),
            "fieldtype": "Data",
            "width": 100
        },
        {
            "fieldname": "total_qty",
            "label": _("Total Quantity"),
            "fieldtype": "Data",
            "width": 120
        },
        {
            "fieldname": "amount",
            "label": _("Amount"),
            "fieldtype": "Currency",
            "width": 150
        }
    ]


def get_data(filters):
    data = []
    conditions = get_conditions(filters)

    # Fetching Finished Goods
    finished = frappe.db.sql(f"""
        SELECT 
            dpi.item_name AS item_code, 
            i.item_name AS item_name, 
            dpi.item_categor AS type_of_product, 
            dpi.uom,
            SUM(dpi.qty) AS total_qty, 
            SUM(dpi.amount) AS amount
        FROM 
            `tabDirect Production Item` dpi
        JOIN 
            `tabDirect Production` dp ON dpi.parent = dp.name
        JOIN 
            `tabItem` i ON dpi.item_name = i.name
        WHERE 
            dp.docstatus = 1
            {conditions}
            AND i.item_group = 'Finish Good'
        GROUP BY 
            dpi.item_name
    """, {
        "month": filters.get("month"),
        "year": filters.get("year")
    }, as_dict=True)

    return finished
