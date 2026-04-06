frappe.ui.form.on('Quotation', {
    refresh: function(frm) {

        frm.add_custom_button('Select Hotel', function() {

            let d = new frappe.ui.Dialog({
                title: 'HOTEL',
                fields: [
                    {
                        label: 'Hotel Name',
                        fieldname: 'name',
                        fieldtype: 'Select',
                        options: []
                    }
                ],
                primary_action_label: 'Submit',
                primary_action(values) {

                    frm.set_value('quotation_to', 'Customer');
                    frm.set_value('party_name', values.name);

                    d.hide();
                }
            });

            frappe.call({
                method: 'apple_app.apple.hotel.get_custom_names',
                callback: function(r) {
                    if (r.message) {
                        d.fields_dict.name.df.options = r.message;
                        d.fields_dict.name.refresh();
                    }
                }
            });

            d.show();
        });

    }
});