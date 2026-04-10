from odoo import models, fields, api

class DoctorMaster(models.Model):
    _name = 'hospital.master'
    _description = 'Hospital Master'

    partner_id = fields.Many2one('res.partner', string="Doctor Name", required=True)
    # name = fields.Char(string='Doctor Name', required=True)
    specialty = fields.Char(string='Specialty')
    contact_no = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    qualification = fields.Char(string='Qualification')
    experience = fields.Integer(string='Years of Experience')
    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Appointments')


    def name_get(self):
        # doctor with specility exit then shown it otherwise doctor name should be visible
        result = []
        for rec in self:
            name = f"{rec.name} ({rec.specialty})" if rec.specialty else rec.name
            result.append((rec.id, name))
        return result

    def call_on_active(self):
        active_id = self.env.context.get('active_id')
        print("kkkkkkkkkkkkkkkkkkkkkkkkkkk", active_id)
        if active_id:
            record = self.browse(active_id)
            print("Active-ID",record.id)

            # record.get_part()

    ####### Get an active_id for current record.

    # def call_on_active(self):
    #     active_id = self.env.context.get('active_id')
    #     if active_id:
    #         record = self.browse(active_id)
    #         record.get_part()
    #

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'

    doctor_id = fields.Many2one('doctor.master',String="Doctor")



class PatientMaster(models.Model):
    _name = 'patient.master'
    _description = 'Patient Master'

    doctor_id = fields.Many2one('res.partner', string="Doctor Name", required=True)
    patient_id = fields.Many2one('res.partner', string="Patient Name", required=True)
    # name = fields.Char(string='Doctor Name', required=True)

    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Appointments')

