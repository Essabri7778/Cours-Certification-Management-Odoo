from odoo import api, fields, models



class Content(models.Model):
    _name = 'course_certification_management.content'
    _description = 'Course content'
    _order = 'sequence asc, id asc'
    _rec_name = 'title'

    # Description
    title  = fields.Char('Content Title', translate = True,required = True)
    description = fields.Text(string='Content Description')
    image = fields.Image(string ='Image')
    tag_ids = fields.Many2many('course_certification_management.course_tag',relation='content_tag_rel', string='Tags')
    type = fields.Selection([
        ('image', 'Image'),
        ('document', 'Document'),
        ('video', 'Video'),
    ], string='Content Type', required=True, default='document')
    sequence = fields.Integer('Sequence', default=0)
    visibility = fields.Boolean(string='Visibility')
    completion_time = fields.Float(string='Completion Time', help='Estimated completion time in hours')
    user_id = fields.Many2one('res.users', string='Uploaded by', default=lambda self: self.env.uid)
    date_published = fields.Datetime('Publish Date', readonly=True, tracking=1)
    
    # Resources
    datas = fields.Binary('Content', attachment=True)
    url = fields.Char('URL', help="Youtube or Google Document URL")
    content_downloadable = fields.Boolean('Allow Download', default=True, help="Allow the user to download the content of the slide.")
    
    # Relations
    course_id = fields.Many2one('course_certification_management.course', string='Course')

    # Section
    is_section = fields.Boolean(string="Is Section")
    # Quiz related fields    
    question_ids = fields.One2many('course_certification_management.question', 'content_id', string='Questions')
    questions_count = fields.Integer(string="Numbers of Questions", compute='_compute_questions_count')
    quiz_first_attempt_reward = fields.Integer("Reward: first attempt", default=10)
    quiz_second_attempt_reward = fields.Integer("Reward: second attempt", default=7)
    quiz_third_attempt_reward = fields.Integer("Reward: third attempt", default=5,)
    quiz_fourth_attempt_reward = fields.Integer("Reward: every attempt after the third try", default=2)

   
   
    @api.depends('question_ids')
    def _compute_questions_count(self):
        for slide in self:
            slide.questions_count = len(slide.question_ids)