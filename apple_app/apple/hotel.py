import frappe

@frappe.whitelist()
def get_custom_names():
    data = frappe.db.get_list(
        "HOTEL",
        fields=["hotel_name"], 
        limit_page_length=50
    )

    # convert to list
    return [d.hotel_name for d in data]