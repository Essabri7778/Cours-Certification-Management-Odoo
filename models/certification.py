
from odoo import api, fields, models, tools


class Certification(models.Model):
    _name = 'course_certification_management.certification'
    _description = 'Certification'
    
    _rec_name = 'name'

    name = fields.Char(string='Certification Name', required=True)
    description = fields.Text(string='Description')

    registration_type = fields.Selection(
        [('private', 'Private'), ('public', 'Public'), ('invitation', 'Invitation')],
        string='Registration Type',
        default='private',
        required=True
    )
    section = fields.Char(string='Section')
    sequence = fields.Integer('Sequence', default=0)
    question_ids = fields.One2many('course_certification_management.certification_question', 'certification_ids', string='Questions')
    questions_count = fields.Integer(string="Numbers of Questions", compute='_compute_questions_count')
    course_id = fields.Many2one('course_certification_management.course', string='Course')
    completion_time = fields.Float(string='Duration')
    #question_ids = fields.One2many('certifications.question', string='Questions')
    photo = fields.Image(string='Certification Photo', help='Certification photo')
    scoring_type = fields.Selection(
        [('no_scoring', 'No Scoring'),
         ('with_answers', 'Scoring with answers at the end'),
         ('without_answers', 'Scoring without answers at the end')],
        string='Scoring Type', default='with_answers')

    success_percentage = fields.Float(string='Success Percentage (%)', digits=(6, 2))
    test_layout = fields.Selection(
        [('one_page_all_questions', 'One page with all the questions'),
         ('one_page_per_section', 'One page per section'),
         ('one_page_per_question', 'One page per question')],
        string='Test Layout', default='one_page_all_questions')
    
    @api.depends('question_ids')
    def _compute_questions_count(self):
        for slide in self:
            slide.questions_count = len(slide.question_ids)

    @api.model
    def action_certification_question_form(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'course_certification_management.certification_question',  # Replace with your content model name
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_course_id': self.env.context.get('active_id')},
        }
    
