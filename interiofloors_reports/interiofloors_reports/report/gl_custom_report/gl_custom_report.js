// Copyright (c) 2024, portal and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["GL Custom Report"] = {
    "filters": [
        {
            label: __("From Date"),
            fieldname: "from_date",
            fieldtype: "Date",
            default: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
            reqd: 1
        },
        {
            label: __("To Date"),
            fieldname: "to_date",
            fieldtype: "Date",
            default: frappe.datetime.get_today(),
            reqd: 1
        },
        {
            "fieldname": "account",
            "label": __("Account"),
            "fieldtype": "Link",
            "options": "Account",
            "get_query": function () {
                return {
                    filters: {"account_type": "Receivable"}
                };
            },
        },
        {
            label: __("Party"),
            fieldname: "party",
            fieldtype: "Link",
            options: "Customer"
        }
    ]
};
