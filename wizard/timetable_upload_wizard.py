from odoo import models, fields
import base64
import io
import openpyxl


class TimetableImportWizard(models.TransientModel):
    _name = 'timetable.import.wizard'
    _description = 'Timetable Import Wizard'

    excel_file = fields.Binary(
        string='Upload Excel File',
        required=True
    )

    file_name = fields.Char(
        string='File Name'
    )

    # def action_import_timetable(self):
    #
    #     file_data = base64.b64decode(self.excel_file)
    #
    #     workbook = openpyxl.load_workbook(
    #         io.BytesIO(file_data)
    #     )
    #
    #     sheet = workbook.active
    #
    #     for row in sheet.iter_rows(
    #         min_row=2,
    #         values_only=True
    #     ):
    #         date, time, subject, faculty, class_name = row
    #
    #         # Create timetable record
    #         self.env['timetable.master'].create({
    #             'date': date,
    #             'time': time,
    #             # Other fields
    #         })
    #
    #     return {'type': 'ir.actions.act_window_close'}

