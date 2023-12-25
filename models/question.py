from odoo import models, fields, api

class Question(models.Model):
    _name = 'course_certification_management.question'
    _description = 'Question Model'

    question = fields.Text(string='Question', required=True)
    sequence = fields.Integer('Sequence', default=0)
    content_id = fields.Many2one('course_certification_management.content', string="Content", required=True)
    response_ids = fields.One2many('course_certification_management.response', 'question_id', string='Responses')


     # statistics
    attempts_count = fields.Integer(compute='_compute_statistics', groups='website_slides.group_website_slides_officer')
    attempts_avg = fields.Float(compute="_compute_statistics", digits=(6, 2), groups='website_slides.group_website_slides_officer')
    done_count = fields.Integer(compute="_compute_statistics", groups='website_slides.group_website_slides_officer')


    @api.constrains('response_ids')
    def _check_answers_integrity(self):
        for question in self:
            if len(question.response_ids.filtered(lambda answer: answer.is_correct)) != 1:
                raise ValidationError(_('Question "%s" must have 1 correct answer', question.question))
            if len(question.response_ids) < 2:
                raise ValidationError(_('Question "%s" must have 1 correct answer and at least 1 incorrect answer', question.question))

    @api.depends('content_id')
    def _compute_statistics(self):
        return True
        # slide_partners = self.env['slide.slide.partner'].sudo().search([('slide_id', 'in', self.slide_id.ids)])
        # slide_stats = dict((s.slide_id.id, dict({'attempts_count': 0, 'attempts_unique': 0, 'done_count': 0})) for s in slide_partners)

        # for slide_partner in slide_partners:
        #     slide_stats[slide_partner.slide_id.id]['attempts_count'] += slide_partner.quiz_attempts_count
        #     slide_stats[slide_partner.slide_id.id]['attempts_unique'] += 1
        #     if slide_partner.completed:
        #         slide_stats[slide_partner.slide_id.id]['done_count'] += 1

        # for question in self:
        #     stats = slide_stats.get(question.slide_id.id)
        #     question.attempts_count = stats.get('attempts_count', 0) if stats else 0
        #     question.attempts_avg = stats.get('attempts_count', 0) / stats.get('attempts_unique', 1) if stats else 0
        #     question.done_count = stats.get('done_count', 0) if stats else 0