
test_doc = frappe.get_doc("HOTEL", "HOTEL PARK")

frappe.msgprint(test_doc.hotel_name)

doc = frappe.new_doc("Try")
doc.hotel_name = "New Branch"
doc.insert()
hotels = frappe.db.get_list(
    "HOTEL",
    fields=['hotel_id', 'hotel_name', 'hotel_type'])
for f in hotels:
  frappe.msgprint(str(f))
 
 
type = frappe.db.get_value("HOTEL" , "HOTEL ARIMA" , "hotel_type")
frappe.msgprint(str(type))
type = frappe.db.get_all(
    "HOTEL",
    fields=["hotel_name", "hotel_id", "hotel_type"]
)

frappe.msgprint(str(type))

exists = frappe.db.exists("HOTEL", "HOTEL PARK")

if exists:
    frappe.msgprint("Hotel Exists in Database")
else:
  frappe.msgprint("Hotel Not Found")

type = frappe.db.count("HOTEL")

frappe.msgprint("Total Hotels: " + str(type))

frappe.delete_doc('HOTEL','HOTEL PARK')
frappe.msgprint('Deleted Successfully')

frappe.rename_doc("HOTEL", "HOTEL PARK", "HOTEL GRAND")



date = frappe.utils.getdate("2026-03-05")
frappe.msgprint(str(date))
