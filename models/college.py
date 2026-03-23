from odoo import models, fields, api



class CollegeMaster(models.Model):
    _name = 'college.master'
    _description = 'College Master'

    partner_id = fields.Many2one('res.partner', string="Related Partner", required=True)
    name = fields.Char(related="partner_id.name", store=True, readonly=False)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    contact_no = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    # medical_history = fields.Text(string='Medical History')
    photo = fields.Binary(string='Store Photo', attachment=True)
    # appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string='Appointments')

    # @api.model
    # def create(self, vals):
    #     # Optional custom logic on creating a patient record
    #     return super(PatientMaster, self).create(vals)
    #
    # def name_get(self):
    #     # To represent the patient record with name and age in drop-downs
    #     result = []
    #     for record in self:
    #         name = f"{record.name} (Age: {record.age})"
    #         result.append((record.id, name))
    #     return result

