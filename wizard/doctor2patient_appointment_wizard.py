from odoo import api, fields, models

class Appointment2patient(models.TransientModel):
    _name = 'appointment.wizard'
    _description = 'My Sample Wizard'

    name = fields.Char(string="Name")
    date_from = fields.Date(string="Start Date")
    date_to = fields.Date(string="End Date")

    def action_confirm_appointment(self):
        return {'type': 'ir.actions.act_window_close'}



    # def open_wizard(self):
    #     return {
    #
    #         'name': 'Wizard',
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         "view_type": "form",
    #         'res_model': ' appointment.wizard .view_appointment_wizard_form',
    #         'target': 'new',
    #         'view_id': self.env.ref
    #         ('appointment.wizard.view_appointment_wizard_form').id,
    #         'context': {'active_id': self.id},
    #     }
