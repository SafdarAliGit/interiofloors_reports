
frappe.query_reports["Monthly Consumption Report"] = {
    "filters": [
        {
            label: __("Month"),
            fieldname: "month",
            fieldtype: "Select",
            options: [
                {value: "01", label: __("January")},
                {value: "02", label: __("February")},
                {value: "03", label: __("March")},
                {value: "04", label: __("April")},
                {value: "05", label: __("May")},
                {value: "06", label: __("June")},
                {value: "07", label: __("July")},
                {value: "08", label: __("August")},
                {value: "09", label: __("September")},
                {value: "10", label: __("October")},
                {value: "11", label: __("November")},
                {value: "12", label: __("December")}
            ],
            default: frappe.datetime.str_to_obj(frappe.datetime.get_today()).getMonth().toString().padStart(2, '0'),
            reqd: 1
        },
        {
            label: __("Year"),
            fieldname: "year",
            fieldtype: "Select",
            options: (function () {
                var years = [];
                var current_year = new Date().getFullYear();
                for (var i = current_year - 10; i <= current_year + 10; i++) {
                    years.push(i.toString());
                }
                return years.join("\n");
            })(),
            default: new Date().getFullYear().toString(),
            reqd: 1
        },
    ]
};
