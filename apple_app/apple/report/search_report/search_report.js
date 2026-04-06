// Copyright (c) 2026, Sai and contributors
// For license information, please see license.txt


frappe.query_reports["Search Report"] = {
    filters: [
        {
            fieldname: "customer",
            label: "Customer",
            fieldtype: "Link",
            options: "Customer",
            reqd: 1,
			placeholder: "Select Customer",
            width: 220
        },
        {
             fieldname: "document_type",
            label: "Document Type",
            fieldtype: "Select",
            options: "\nSales Order\nCustomer Purchase Order\nBoth",
            reqd: 1
        },
		{
			fieldname: "from_date",
			label: "From Date",
			fieldtype: "Date",
			reqd: 1,
			placeholder: "Select From Date",
			width: 220
		},
		{
			fieldname: "to_date",
			label: "To Date",
			fieldtype: "Date",
			reqd: 1,
			placeholder: "Select To Date",
			width: 220
		},
		{
			fieldname: "Show Last Payment",
			label: "Show Last Payment",
			fieldtype: "Check",
			default: 0,
			width: 220
		}
    ]
};