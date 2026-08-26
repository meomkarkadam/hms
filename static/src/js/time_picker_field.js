/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class TimePickerField extends Component {
    static template = "hms.TimePickerField";
    static props = {
        ...standardFieldProps,
    };

    setup() {
        this.state = useState({
            value: this.props.record.data[this.props.name] || "",
        });
    }

    onChange(ev) {
        this.state.value = ev.target.value;
        this.props.record.update({
            [this.props.name]: ev.target.value,
        });
    }
}

registry.category("fields").add("time_picker", {
    component: TimePickerField,
    supportedTypes: ["char"],
});