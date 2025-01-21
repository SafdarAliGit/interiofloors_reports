// Copyright (c) 2025, portal and contributors
// For license information, please see license.txt

frappe.query_reports["Direct Production Quantity Report"] = {
    "filters": [
        {
            "fieldname": "company",
            "label": __("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "default": frappe.defaults.get_default("company"),
            "reqd": 1
        },
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
            "reqd": 1
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(),
            "reqd": 1
        },
        {
            "fieldname": "item_group",
            "label": __("Item Group"),
            "fieldtype": "Link",
            "options": "Item Group"
        },
        {
            "fieldname": "item",
            "label": __("Item"),
            "fieldtype": "Link",
            "options": "Item"
        },
        {
            "fieldname": "warehouse",
            "label": __("Warehouse"),
            "fieldtype": "Link",
            "options": "Warehouse"
        },
        {
            "fieldname": "warehouse_type",
            "label": __("Warehouse Type"),
            "fieldtype": "Select",
            "options": ["", "Raw Material", "Finished Goods", "Stores"],
            "default": ""
        },
        {
            "fieldname": "include_uom",
            "label": __("Include UOM"),
            "fieldtype": "Check",
            "default": 0
        },
        {
            "fieldname": "show_variant_attributes",
            "label": __("Show Variant Attributes"),
            "fieldtype": "Check",
            "default": 0
        },
        {
            "fieldname": "show_stock_ageing_data",
            "label": __("Show Stock Ageing Data"),
            "fieldtype": "Check",
            "default": 0
        }
    ]
};
