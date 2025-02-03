# Copyright (c) 2025, portal and contributors
# For license information, please see license.txt

# import frappe

import frappe

def execute(filters=None):
    # Columns for the report
    columns = [
        {"fieldname": "item_code", "label": "Item Code", "fieldtype": "Link", "options": "Item", "width": 300},
        {"fieldname": "item_name", "label": "Item Name", "fieldtype": "Data", "width": 300},
        {"fieldname": "closing_balance_qty", "label": "Closing Balance Qty", "fieldtype": "Float", "width": 350},
    ]

    data = get_closing_balances()

    return columns, data


def get_closing_balances():
    closing_balances = frappe.db.sql("""
        SELECT
            item_code,
            item_name,
            (SELECT SUM(actual_qty) FROM `tabStock Ledger Entry` 
             WHERE item_code = item.item_code) AS closing_balance_qty
        FROM `tabItem` AS item
        WHERE item.disabled = 0
    """, as_dict=True)

    return closing_balances
