# Copyright (c) 2026, Sai and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data()
    return columns, data

def get_columns():
    return [
        {
            "fieldname": "name",
            "label": "Name",
            "fieldtype": "Data",
            "width": 200
        }
    ]

def get_data():
    return frappe.db.sql("""
        SELECT name
        FROM `tabHOTEL`
    """, as_dict=1)