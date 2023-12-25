from odoo import fields, models

class CourseTag(models.Model):
    _name = 'course_certification_management.course_tag'
    _description = 'Course Tag'

    # Description
    name = fields.Char('Name', required=True, translate=True)
    
    
