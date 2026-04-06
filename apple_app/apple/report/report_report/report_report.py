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
        },
		{
			"fieldname": "order",
			"label": "Order",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "customer",
			"label": "Customer",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "total",
			"label": "Total",
			"fieldtype": "Currency",
			"width": 200
		},
		{
			"fieldname": "status",
			"label": "Status",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "date",
			"label": "Date",
			"fieldtype": "Date",
			"width": 200
		},
		{
			"fieldname": "time",
			"label": "Time",
			"fieldtype": "Time",
			"width": 200
		},
		{
			"fieldname": "payment_method",
			"label": "Payment Method",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"fieldname": "delivery_address",
			"label": "Delivery Address",
			"fieldtype": "Data",
			"width": 200
		}
    ]

def get_data():
    return [
        {
            "name": "ORD-001",
            "order": "Burger",
            "customer": "Sai",
            "total": 250,
            "status": "Completed",
            "date": "2026-03-26",
            "time": "12:30:00",
            "payment_method": "Cash",
            "delivery_address": "Chennai"
        },
        {
            "name": "ORD-002",
            "order": "Pizza",
            "customer": "Gajini",
            "total": 500,
            "status": "Pending",
            "date": "2026-03-26",
            "time": "01:00:00",
            "payment_method": "UPI",
            "delivery_address": "Coimbatore"
        }
    ]