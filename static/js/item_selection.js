function update_item_dropdowns(options_arr) {
    var selected_items = []
    var selected_values = []

    var all_current_items = document.getElementsByClassName("form_input");

    for (i = 0; i < all_current_items.length; i++) {
        var selectbox = all_current_items[i].querySelector("select")
        selected_values.push(selectbox.options[selectbox.selectedIndex].value);
        selected_items.push([selectbox.options[selectbox.selectedIndex].value,  selectbox.options[selectbox.selectedIndex].text]);
        while (all_current_items[i].querySelector("select").options.length > 0) {
            all_current_items[i].querySelector("select").options.remove(0);
        }
    }

    for (i = options_arr.length - 1; i >= 0; --i) {
        if (selected_values.includes(options_arr[i][0])) {
            options_arr.splice(i, 1);
        }
    }

    for (i = 0; i < all_current_items.length; i++) {
        var new_option = document.createElement("option")
        new_option.value = selected_items[i][0];
        new_option.text = selected_items[i][1];
        all_current_items[i].querySelector("select").add(new_option)
        for (j = 0; j < options_arr.length; j++) {
            var next_option = document.createElement("option")
            next_option.value = options_arr[j][0];
            next_option.text = options_arr[j][1];
            all_current_items[i].querySelector("select").add(next_option, all_current_items[i].querySelector("select").options[j - 1])
        }
    }
}

function update_clone_children(clone, last_selected_index) {
    // ID format id_form-[index]-[item | quantity]
    var clone_item = clone.querySelector("select");
    var clone_qty  = clone.querySelector("input[type = 'number']");

    var increment_index = function(idx) { return parseInt(idx) + 1; };

    clone_item.name = clone_item.name.replace(/(\d+)/, increment_index);
    clone_qty.name  = clone_qty.name.replace(/(\d+)/,  increment_index);

    clone_item.id   = clone_item.id.replace(/(\d+)/, increment_index);
    clone_qty.id    = clone_qty.id.replace(/(\d+)/, increment_index);

    clone_item.remove(last_selected_index);
}

function create_new_item_input() {
    var main_container    = document.getElementById("item_input_container");
    var all_current_items = document.getElementsByClassName("form_input");
    var last_input        = all_current_items[all_current_items.length - 1];
    var last_input_clone  = last_input.cloneNode(true)

    update_clone_children(last_input_clone,
        last_input.querySelector("select").selectedIndex);

    var add_item_btn  = last_input.querySelector("#add-item");
    all_current_items[all_current_items.length - 1].appendChild(add_item_btn);
    add_item_btn.remove();


    var total_forms   = document.querySelector("#id_form-TOTAL_FORMS");
    total_forms.value = parseInt(total_forms.value) + 1;

    main_container.appendChild(last_input_clone);
    update_item_choices()
}
