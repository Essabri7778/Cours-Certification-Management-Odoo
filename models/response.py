from odoo import models, fields, api

class Response(models.Model):
    _name = 'course_certification_management.response'
    _description = 'Response Model'

    text_value = fields.Char(string='Response', required=True)
    is_correct = fields.Boolean(string='Is True')
    comment = fields.Text(string='Response Comment')
    question_id = fields.Many2one('course_certification_management.question', string='Question')