// Copyright (c) 2024, portal and contributors
// For license information, please see license.txt

frappe.query_reports["Customer Group-wise Sale"] = {
    "filters": [
        {
            label: __("Item Group"),
            fieldname: "item_group",
            fieldtype: "Link",
            options: "Item Group",
            reqd: 0
        },
        {
            label: __("Customer Group"),
            fieldname: "customer_group",
            fieldtype: "Link",
            options: "Customer Group",
            reqd: 0
        },
        {
            label: __("Territory"),
            fieldname: "territory",
            fieldtype: "Link",
            options: "Territory",
            reqd: 0
        },
        {
            label: __("From Date"),
            fieldname: "from_date",
            fieldtype: "Date",
            default: frappe.datetime.month_start(),
            reqd: 1
        },
        {
            label: __("To Date"),
            fieldname: "to_date",
            fieldtype: "Date",
            default: frappe.datetime.month_end(),
            reqd: 1
        }
    ]
};
