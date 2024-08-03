import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_conditions(filters):
    conditions = []
    if filters.get("from_date"):
        conditions.append(f"gle.posting_date >= %(from_date)s")
    if filters.get("to_date"):
        conditions.append(f"gle.posting_date <= %(to_date)s")
    if filters.get("account"):
        conditions.append(f"gle.account = %(account)s")
    if filters.get("party"):
        conditions.append(f"gle.party = %(party)s")
    return " AND ".join(conditions)


def get_columns():
    return [
        {"fieldname": "posting_date", "label": _("Posting Date"), "fieldtype": "Date", "width": 100},
        {"fieldname": "account", "label": _("Account"), "fieldtype": "Link", "options": "Account", "width": 200},
        {"fieldname": "debit", "label": _("Debit"), "fieldtype": "Currency", "width": 120},
        {"fieldname": "credit", "label": _("Credit"), "fieldtype": "Currency", "width": 120},
        {"fieldname": "balance", "label": _("Balance"), "fieldtype": "Currency", "width": 120},
    ]


def get_data(filters):
    # SQL query to fetch ledger entries excluding Journal Entries
    query="""
    SELECT
        gle.posting_date,
        gle.account,
        gle.debit_in_account_currency AS debit,
        gle.credit_in_account_currency AS credit,
        0 AS balance
    FROM
        `tabGL Entry` AS gle
    WHERE
        gle.voucher_type != 'Journal Entry'
        AND 
        (SELECT account_type FROM `tabAccount` WHERE name = gle.account) ='Receivable'
        AND 
        gle.is_cancelled = 0
        AND
        {conditions}
    ORDER BY
        gle.posting_date ASC
    """.format(conditions=get_conditions(filters))
    data = frappe.db.sql(query, filters, as_dict=1)
    balance = 0
    for entry in data:
        # Compute the balance for each entry
        entry['balance'] = balance + (entry['debit'] - entry['credit'])
        # Update running balance
        balance = entry['balance']

    return data
