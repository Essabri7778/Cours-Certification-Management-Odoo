from odoo import models, fields, api

class CertificationQuestion(models.Model):
    _name ='course_certification_management.certification_question'
    _description = 'Certification Question'
    _rec_name='question_text'

    sequence = fields.Integer('Sequence', default=0)
    certification_ids = fields.Many2one('course_certification_management.certification', string='Certification')
    description = fields.Text(string='Description')
    question_text = fields.Text(string='Question Text', required=True)
    answer_type = fields.Selection(
        [('single', 'Multiple Choice '),
         ('multiple', 'Multiple Choice '),
         ('fill_blank', 'Fill-in the Blank')],
        string='Answer Type', required=True)

    answer = fields.Char(string='Answer')
    one_option = fields.One2many('course_certification_management.certification_question.option', 'question_id', string='One option Answer')
    options = fields.One2many('course_certification_management.certification_question.option', 'question_id', string='Many options Answer')
    photo = fields.Image(string='Question Photo', help='Question photo')
    
class CertificationQuestionOption(models.Model):
    _name = 'course_certification_management.certification_question.option'
    _description = 'Certification Question Option'
    _rec_name='option_text'
    
    question_id = fields.Many2one('course_certification_management.certification_question', string='Question')
    option_text = fields.Char(string='Option Text')
    is_correct = fields.Boolean(string='Is Correct')
