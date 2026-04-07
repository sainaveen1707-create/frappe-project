frappe.ui.form.on('test data', {
    refresh: function(frm) {
        calculate_all(frm);
    },

    product_1: function(frm) {
        calculate_all(frm);
    },

    product_2: function(frm) {
        calculate_all(frm);
    },

    operator: function(frm) {
        calculate_all(frm);
    },

    discount: function(frm) {
        calculate_all(frm);
    },

    tax: function(frm) {
        calculate_all(frm);
    },

    discount_product_1: function(frm) {
        apply_discount(frm, 'product_1');
    },

    discount_product_2: function(frm) {
        apply_discount(frm, 'product_2');
    },

    discount_total: function(frm) {
        apply_discount(frm, 'total');
    },

    discount_tax: function(frm) {
        apply_discount(frm, 'tax');
    }
});


function get_total(p1, p2, operator) {
    let total = 0;

    if (operator === '+') total = p1 + p2;
    else if (operator === '-') total = p1 - p2;
    else if (operator === '*') total = p1 * p2;
    else if (operator === '/') total = p2 !== 0 ? p1 / p2 : 0;

    return flt(total, 2);
}


function calculate_all(frm) {
    let p1 = flt(frm.doc.product_1);
    let p2 = flt(frm.doc.product_2);
    let operator = frm.doc.operator || '+';
    let tax_pct = flt(frm.doc.tax);

    let total = get_total(p1, p2, operator);
    let tax_amount = flt((total * tax_pct) / 100, 2);
    let grand_total = flt(total + tax_amount, 2);

    frm.set_value('total', total);
    frm.set_value('tax_amount', tax_amount);
    frm.set_value('grand_total', grand_total);
}


function apply_discount(frm, target) {
    let p1 = flt(frm.doc.product_1);
    let p2 = flt(frm.doc.product_2);
    let operator = frm.doc.operator || '+';
    let discount = flt(frm.doc.discount);
    let tax_pct = flt(frm.doc.tax);

    let total = get_total(p1, p2, operator);

    let disc_amt = 0;
    let base_total = total;
    let tax_amount = 0;
    let grand_total = 0;

    if (target === 'product_1') {
        disc_amt = flt((p1 * discount) / 100, 2);
        base_total = flt(total - disc_amt, 2);
    }

    else if (target === 'product_2') {
        disc_amt = flt((p2 * discount) / 100, 2);
        base_total = flt(total - disc_amt, 2);
    }

    else if (target === 'total') {
        disc_amt = flt((total * discount) / 100, 2);
        base_total = flt(total - disc_amt, 2);
    }

    else if (target === 'tax') {
        let original_tax = flt((total * tax_pct) / 100, 2);
        disc_amt = flt((original_tax * discount) / 100, 2);
        tax_amount = flt(original_tax - disc_amt, 2);
        grand_total = flt(total + tax_amount, 2);

        frm.set_value('tax_amount', tax_amount);
        frm.set_value('grand_total', grand_total);
        return;
    }

    tax_amount = flt((base_total * tax_pct) / 100, 2);
    grand_total = flt(base_total + tax_amount, 2);

    frm.set_value('total', base_total);
    frm.set_value('tax_amount', tax_amount);
    frm.set_value('grand_total', grand_total);
}