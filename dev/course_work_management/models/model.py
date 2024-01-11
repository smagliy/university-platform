from odoo import models, fields


class CourseWork(models.Model):
    _name = 'course.work'
    _description = 'Course Work Information'

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    course_work_name = fields.Char(string='Course Work Name', required=True)
    date = fields.Date(string='Date')
    estimate = fields.Float(string='Estimate')
    degree_type = fields.Selection([('bachelor', 'Bachelor'), ('master', 'Master')], string='Degree Type')
    number_course = fields.Integer(string='Number of Courses')
    # Add other fields as needed
