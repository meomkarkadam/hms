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



class StudentEnrollment(models.Model):
    _name = 'student.enrollment'




    name = fields.Char("Name")
    erp_id = fields.Char("Student ID")


    academic_year = fields.Char(
        string="Academic Year",
        default=lambda self: self.get_academic_year()

    )

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
        ],

        string="Academic Class"
    )


    # @api.onchange('academic_year')
    # def _compute_student_id(self):
    #     for rec in self:
    #         rec.erp_id = rec.academic_year.erp_id

    def get_academic_year(self):
        year = datetime.now().year
        next_year = year + 1
        return f"{year}-{str(next_year)[-2:]}"

    ref_id = fields.Integer("Student ID starting with")



    _sql_constraints = [
        ('erp_unique', 'unique(erp_id)', 'ERP ID must be unique!')
    ]

    phone = fields.Char(
        string="Phone",
        store=True
    )


    @api.onchange('ref_id')
    def _onchange_field_a(self):
        self.erp_id = self.ref_id

    def action_test_button(self):
        for rec in self:
            print("Button Clicked", rec.name)



