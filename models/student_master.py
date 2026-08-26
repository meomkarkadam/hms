from odoo import models, fields, api
from datetime import datetime


class StudentMaster(models.Model):
    _name = 'student.master'
    _description = 'Student Master'

    partner_id = fields.Many2one('res.partner', "Name")
    mobile = fields.Char(
        related='partner_id.mobile',
        string="Mobile No",
        store=True
    )


    email = fields.Char(
            related='partner_id.email',
            string="Email",
            store=True
        )

    phone = fields.Char(
            related='partner_id.phone',
            string="Phone",
            store=True
        )

    street = fields.Char(
            related='partner_id.street',
            string="Street",
            store=True
        )

    city = fields.Char(
            related='partner_id.city',
            string="City",
            store=True
        )

    state_id = fields.Many2one(
            'res.country.state',
            related='partner_id.state_id',
            string="State",
            store=True
        )

    zip = fields.Char(
            related='partner_id.zip',
            string="ZIP",
            store=True
        )

    country_id = fields.Many2one(
            'res.country',
            related='partner_id.country_id',
            string="Country",
            store=True
        )

    image_1920 = fields.Image(
        related='partner_id.image_1920',
        store=True
    )

    fathername = fields.Char("Father Name")

    mothername = fields.Char("Mother Name")

    designation = fields.Char("Designation")

    fathermobile_no = fields.Char("Father Mobile No")

    mothermobileno = fields.Char("Mother Mobile No")

    organization = fields.Char("Organization")

    fatheradhar = fields.Char("Father Adhar No")

    motheradharno = fields.Char("Mother Adhar No")

    fatherofficecontact = fields.Char("Father Office contact")

    mother_office_contact = fields.Char("Mother Office contact")




class StudentEnrollment(models.Model):
    _name = 'student.enrollment'




    partner_id = fields.Many2one('res.partner', "Name")

    erp_id = fields.Char("Student ID")


    # academic_year = fields.Char(
    #     string="Academic Year",
    #     default=lambda self: self.get_academic_year()
    #
    # )

    # academic_year_id = fields.Many2one(
    #     'academics.master',
    #     string='Academic Year',
    # )

    course = fields.Selection([
        ('mbbs cbme', 'MBBS-CBME'),
        ('mbbs old', 'MBBS-OLD'),
    ],
    string="Course",
    default='mbbs cbme',)

    admission_date = fields.Datetime("Admission Date")



    course = fields.Selection([
        ('mbbs cbme', 'MBBS-CBME'),
        ('mbbs old', 'MBBS-OLD'),
    ],
    string="Course",
    default='mbbs cbme',)


    ace_class = fields.Selection(
        [
            ('first professional MBBS', 'First Professional MBBS'),
            ('second profess MBBS', 'Second Professional MBBS'),
            ('third professional MBBS part I', 'Third Professional MBBS Part I'),
            ('third professional MBBS part II', 'Third Professional MBBS Part II'),
            ('Internship', 'Internship'),
        ],

        string="Academic Class"
    )


    # @api.onchange('academic_year')
    # def _compute_student_id(self):
    #     for rec in self:
    #         rec.erp_id = rec.academic_year.erp_id

    # def get_academic_year(self):
    #     year = datetime.now().year
    #     next_year = year + 1
    #     return f"{year}-{str(next_year)[-2:]}"

    ref_id = fields.Integer("Student ID starting with")



    _sql_constraints = [
        ('erp_unique', 'unique(erp_id)', 'ERP ID must be unique!')
    ]

    phone = fields.Char(
        string="Phone",
        store=True
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('enrolled', 'Enrolled')
    ], default='draft')

    def action_test_button(self):
        for rec in self:
            print("Button Clicked", rec.name)


    # @api.onchange('ref_id')
    # def _onchange_field_a(self):
    #     self.erp_id = self.ref_id

    # @api.model_create_multi
    # def create(self, vals_list):
    #
    #     for vals in vals_list:
    #
    #         if vals.get('academic_year_id'):
    #             academic_year = self.env[
    #                 'your.academic.year.model'
    #             ].browse(vals['academic_year_id'])
    #
    #             # Example: 2024-25
    #             year_name = academic_year.name
    #
    #             # Get first 2 digits: 24
    #             year_prefix = year_name[:2]
    #
    #             # Generate 6-digit sequence
    #             sequence = self.env[
    #                 'ir.sequence'
    #             ].next_by_code(
    #                 'student.enrollment.sequence'
    #             )
    #
    #             # Example: 24 + 000001
    #             vals['erp_id'] = (
    #                 f"{year_prefix}{sequence}"
    #             )


# def action_test_button(self):
#         for rec in self:
#             print("Enroll Button Clicked Action", rec.name)
#
#             self.env['student.master'].create({
#                 'partner_id': rec.partner_id,
#                 'erp_id': rec.erp_id,
#                 'email': rec.email,
#                 'mobile': rec.mobile,
#                 'course': rec.course,
#                 'admission_date': rec.admission_date,
#                 'ace_class': rec.ace_class,
#                 'academic_year': rec.academic_year,
#             })
#             rec.state = 'enrolled'
#
#
#
#
#

