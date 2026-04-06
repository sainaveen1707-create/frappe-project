# Copyright (c) 2026, Sai and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "fieldname": "document_type",
            "label": "Document Type",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "fieldname": "customer",
            "label": "Customer",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 180
        },
        {
            "fieldname": "sales_order",
            "label": "Sales Order",
            "fieldtype": "Link",
            "options": "Sales Order",
            "width": 180
        },
        {
            "fieldname": "transaction_date",
            "label": "Date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Data",
            "width": 140
        },
        {
            "fieldname": "grand_total",
            "label": "Grand Total",
            "fieldtype": "Currency",
            "width": 140
        },
        {
            "fieldname": "po_no",
            "label": "Customer Purchase Order",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "fieldname": "delivery_date",
            "label": "Delivery Date",
            "fieldtype": "Date",
            "width": 130
        }
    ]


def get_data(filters):
    if not filters:
        return []

    customer = filters.get("customer")
    document_type = filters.get("document_type")

    if not customer or not document_type:
        return []

    if document_type == "Sales Order":
        return frappe.db.sql("""
            SELECT
                'Sales Order' AS document_type,
                customer,
                name AS sales_order,
                transaction_date,
                status,
                grand_total,
                po_no,
                delivery_date
            FROM `tabSales Order`
            WHERE customer = %s
              AND docstatus < 2
            ORDER BY transaction_date DESC, creation DESC
        """, (customer,), as_dict=1)

    elif document_type == "Customer Purchase Order":
        return frappe.db.sql("""
            SELECT
                'Customer Purchase Order' AS document_type,
                customer,
                name AS sales_order,
                transaction_date,
                status,
                grand_total,
                po_no,
                delivery_date
            FROM `tabSales Order`
            WHERE customer = %s
              AND IFNULL(po_no, '') != ''
              AND docstatus < 2
            ORDER BY transaction_date DESC, creation DESC
        """, (customer,), as_dict=1)

    elif document_type == "Both":
        return frappe.db.sql("""
            SELECT
                CASE
                    WHEN IFNULL(po_no, '') != '' THEN 'Customer Purchase Order'
                    ELSE 'Sales Order'
                END AS document_type,
                customer,
                name AS sales_order,
                transaction_date,
                status,
                grand_total,
                po_no,
                delivery_date
            FROM `tabSales Order`
            WHERE customer = %s
              AND docstatus < 2
            ORDER BY transaction_date DESC, creation DESC
        """, (customer,), as_dict=1)

    return []