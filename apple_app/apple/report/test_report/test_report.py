# Copyright (c) 2026, Sai and contributors
# For license information, please see license.txt

# import frappe


# import frappe

# def execute(filters=None):
	
#     columns = get_columns()
#     data = get_data()
#     return columns, data

# def get_columns():
#     return [
#         {
#             "fieldname": "hotel_name",
#             "fieldtype": "Data",
#             "label": "Student",
#             "width": 200
#         }
#     ]

# def get_data():
#     return frappe.db.sql("""
#         SELECT hotel_name 
#         FROM `tabHOTEL`
#     """, as_dict=True)


import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data()
    return columns, data

def get_columns():
    return [
        {
            "fieldname": "hotel_name",
            "fieldtype": "Data",
            "label": "Hotel Name",
            "width": 200
        }
    ]

def get_data():
    return frappe.db.sql("""
        SELECT name AS hotel_name 
        FROM `tabItem`
    """, as_dict=True)
		
	


