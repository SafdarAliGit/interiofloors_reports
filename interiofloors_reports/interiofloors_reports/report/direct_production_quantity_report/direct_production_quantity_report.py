# Copyright (c) 2025, portal and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)

    return columns, data

def get_columns():
    return [
        {"label": "Item", "fieldname": "item_code", "fieldtype": "Data", "width": 150},
        {"label": "Item Name", "fieldname": "item_name", "fieldtype": "Data", "width": 200},
        {"label": "Item Group", "fieldname": "item_group", "fieldtype": "Data", "width": 150},
        {"label": "Warehouse", "fieldname": "warehouse", "fieldtype": "Data", "width": 150},
        {"label": "Stock UOM", "fieldname": "stock_uom", "fieldtype": "Data", "width": 100},
        {"label": "Balance Qty", "fieldname": "balance_qty", "fieldtype": "Float", "width": 120},
        {"label": "Balance Value", "fieldname": "balance_value", "fieldtype": "Currency", "width": 120},
        {"label": "Opening Qty", "fieldname": "opening_qty", "fieldtype": "Float", "width": 120},
        {"label": "Opening Value", "fieldname": "opening_value", "fieldtype": "Currency", "width": 120},
        {"label": "In Qty", "fieldname": "in_qty", "fieldtype": "Float", "width": 120},
        {"label": "In Value", "fieldname": "in_value", "fieldtype": "Currency", "width": 120},
        {"label": "Out Qty", "fieldname": "out_qty", "fieldtype": "Float", "width": 120}
    ]

def get_data(filters):
    conditions = get_conditions(filters)

    query = f"""
        SELECT
            sle.item_code,
            i.item_name,
            i.item_group,
            sle.warehouse,
            i.stock_uom,
            SUM(CASE WHEN sle.voucher_type = 'Stock Reconciliation' THEN sle.actual_qty ELSE 0 END) AS opening_qty,
            SUM(CASE WHEN sle.voucher_type = 'Stock Reconciliation' THEN sle.stock_value_difference ELSE 0 END) AS opening_value,
            SUM(CASE WHEN sle.actual_qty > 0 THEN sle.actual_qty ELSE 0 END) AS in_qty,
            SUM(CASE WHEN sle.actual_qty > 0 THEN sle.stock_value_difference ELSE 0 END) AS in_value,
            SUM(CASE WHEN sle.actual_qty < 0 THEN ABS(sle.actual_qty) ELSE 0 END) AS out_qty,
            SUM(CASE WHEN sle.actual_qty < 0 THEN ABS(sle.stock_value_difference) ELSE 0 END) AS out_value,
            SUM(sle.actual_qty) AS balance_qty,
            SUM(sle.stock_value_difference) AS balance_value
        FROM
            `tabStock Ledger Entry` sle
        INNER JOIN
            `tabItem` i ON sle.item_code = i.name
        WHERE
            sle.docstatus = 1 {conditions}
        GROUP BY
            sle.item_code, sle.warehouse
    """

    return frappe.db.sql(query, filters, as_dict=True)

def get_conditions(filters):
    conditions = ""
    if filters.get("item_group"):
        conditions += " AND i.item_group = %(item_group)s"
    if filters.get("warehouse"):
        conditions += " AND sle.warehouse = %(warehouse)s"
    if filters.get("from_date") and filters.get("to_date"):
        conditions += " AND sle.posting_date BETWEEN %(from_date)s AND %(to_date)s"

    return conditions
