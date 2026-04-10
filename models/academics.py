from odoo import models, fields, api



class AcademicsMaster(models.Model):
    _name = 'academics.master'
    _description = 'Academics Master'

    course = fields.Selection([
        ('mbbs cbme', 'MBBS-CBME'),
        ('mbbs old', 'MBBS-OLD'),
    ],
        string="Course",
        default='mbbs cbme', )
    academic_year = fields.Selection(
        [
            ('2024-25', '2024-25'),
            ('2025-26', '2025-26'),
            ('2026-27', '2026-27'),
            ('2027-28', '2027-28'),
        ],
        string='Academic Year'
    )

    def action_confirm(self):
        print("fffffffffffffff")

class SubjectMaster(models.Model):
        _name = 'subject.master'
        _description = 'Subject Master'


        subject = fields.Selection([
            ('anatomy', 'Anatomy'),
            ('biochemistry', 'Biochemistry'),
            ('physiology', 'Physiology'),
            ('psm', 'PSM'),
            ('pathology', 'Pathology'),
            ('microbiology', 'Microbiology'),
            ('pharmacology', 'Pharmacology'),
            ('fmt', 'FMT'),
            ('surgery', 'Surgery'),
            ('medicine', 'Medicine'),
            ('obgy', 'OBGY'),
            ('orthopedics', 'Orthopedics'),
            ('ent', 'ENT'),
            ('ophthalmology', 'Ophthalmology'),
        ], string='Subject', required=True)



class Timetable(models.Model):
    _name = 'college.timetable'
    _description = 'Weekly Timetable'

    name = fields.Char(
        string='Timetable Name'
    )

    academic_year_id = fields.Many2one(
        'academic.year',
        string='Academic Year'
    )

    line_ids = fields.One2many(
        'college.timetable.line',
        'timetable_id',
        string='Timetable Lines'
    )

class TimetableLine(models.Model):
    _name = 'college.timetable.line'
    _description = 'Weekly Timetable Line'

    timetable_id = fields.Many2one(
        'college.timetable',
        string='Timetable'
    )

    day = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    ], string='Day')

    start_time = fields.Float(
        string='Start Time'
    )

    end_time = fields.Float(
        string='End Time'
    )

    subject_id = fields.Many2one(
        'subject.master',
        string='Subject'
    )

    faculty_id = fields.Many2one(
        'res.partner',
        string='Faculty'
    )
