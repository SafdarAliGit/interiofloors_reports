import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 250},
		{"label": _("Item Group"), "fieldname": "item_group", "fieldtype": "Data", "width": 220},
		{"label": _("Quantity Sold"), "fieldname": "quantity_sold", "fieldtype": "Float", "width": 220},
		{"label": _("Total Amount"), "fieldname": "total_amount", "fieldtype": "Currency", "width": 220},
	]

def get_data(filters):
	conditions = []

	if filters.get("month") and filters.get("year"):
		conditions.append("MONTH(si.posting_date) = %(month)s")
		conditions.append("YEAR(si.posting_date) = %(year)s")

	if filters.get("item_group"):
		conditions.append("si_item.item_group = %(item_group)s")

	if filters.get("from_date") and filters.get("to_date"):
		conditions.append("si.posting_date BETWEEN %(from_date)s AND %(to_date)s")

	if filters.get("customer_group"):
		conditions.append("si.customer_group = %(customer_group)s")

	if filters.get("territory"):
		conditions.append("si.territory = %(territory)s")

	where_clause = " AND ".join(conditions) if conditions else "1=1"

	data = frappe.db.sql(f"""
		SELECT
			si.customer_name AS customer_name,
			si_item.item_group AS item_group,
			SUM(si_item.qty) AS quantity_sold,
			SUM(si_item.amount) AS total_amount
		FROM
			`tabSales Invoice` si
		JOIN
			`tabSales Invoice Item` si_item ON si.name = si_item.parent
		WHERE
			si.docstatus = 1 AND {where_clause}
		GROUP BY
			si.customer_name, si_item.item_group
		ORDER BY
			si.customer_name ASC
	""", filters, as_dict=True)

	return data
