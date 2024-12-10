import frappe
from frappe import _
from frappe.utils import cint

from erpnext.accounts.party import get_partywise_advanced_payment_amount
from erpnext.accounts.report.accounts_receivable.accounts_receivable import ReceivablePayableReport


def execute(filters=None):
    args = {
        "party_type": "Customer",
        "naming_by": ["Selling Settings", "cust_master_name"],
    }
    return CustomAccountsReceivableReport(filters).run(args)


class CustomAccountsReceivableReport(ReceivablePayableReport):
    def __init__(self, filters=None):
        super().__init__(filters)
        self.account_type = "Receivable"  # Ensure this is set during initialization

    def run(self, args):
        # Ensure essential attributes are set
        self.party_type = args.get("party_type", "Customer")
        self.party_naming_by = frappe.db.get_value(
            args.get("naming_by")[0], None, args.get("naming_by")[1]
        )

        if not self.account_type:
            self.account_type = "Receivable"

        self.get_columns()  # Ensure columns are defined
        self.get_data(args)  # Fetch and format data
        return self.columns, self.data


    def get_columns(self):
        """Define custom columns for the report."""
        self.columns = [
            {"label": _("Posting Date"), "fieldname": "posting_date", "fieldtype": "Date", "width": 100},
            {"label": _("Customer"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 150},
            {"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
            {"label": _("Customer Group"), "fieldname": "customer_group", "fieldtype": "Data", "width": 150},

            {"label": _("Voucher Type"), "fieldname": "voucher_type", "fieldtype": "Data", "width": 120},
            {"label": _("Voucher No"), "fieldname": "voucher_no", "fieldtype": "Data", "width": 150},
            {"label": _("Due Date"), "fieldname": "due_date", "fieldtype": "Date", "width": 100},
            {"label": _("Invoiced Amount"), "fieldname": "invoiced_amount", "fieldtype": "Currency", "width": 130},
            {"label": _("Paid Amount"), "fieldname": "paid_amount", "fieldtype": "Currency", "width": 130},
            {"label": _("Credit Note"), "fieldname": "credit_note", "fieldtype": "Currency", "width": 130},
            {"label": _("Outstanding Amount"), "fieldname": "outstanding_amount", "fieldtype": "Currency", "width": 130},
            {"label": _("Territory"), "fieldname": "territory", "fieldtype": "Data", "width": 150},
        ]

    def get_data(self, args):
        self.data = []

        receivable_report = ReceivablePayableReport(self.filters)

        if not hasattr(receivable_report, "account_type"):
            receivable_report.account_type = "Receivable"
            receivable_report.filters.account_type = "Receivable"

        receivables = receivable_report.run(args)[1]

        for entry in receivables:
            row = {
                "posting_date": entry.get("posting_date"),
                "customer": entry.get("party"),
                "customer_name": entry.get("customer_name"),
                "customer_group": entry.get("customer_group"),
                "voucher_type": entry.get("voucher_type"),
                "voucher_no": entry.get("voucher_no"),
                "due_date": entry.get("due_date"),
                "invoiced_amount": entry.get("invoiced"),
                "paid_amount": entry.get("paid"),
                "credit_note": entry.get("credit_note"),
                "outstanding_amount": entry.get("outstanding"),
                "territory": entry.get("territory"),

            }
            self.data.append(row)


def get_gl_balance(report_date):
    """Utility function to fetch general ledger balances."""
    return frappe._dict(
        frappe.db.get_all(
            "GL Entry",
            fields=["party", "sum(debit - credit)"],
            filters={"posting_date": ("<=", report_date), "is_cancelled": 0},
            group_by="party",
            as_list=1,
        )
    )
