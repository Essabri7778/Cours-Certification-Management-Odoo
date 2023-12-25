from odoo import api, fields, models, tools


class Course(models.Model):
    """ A Course is a container for content. """
    _name = 'course_certification_management.course'
    _description = 'Course'
    _order = 'id'
    _rec_name = 'title'
     
    # Description
    title = fields.Char(string = 'Course Title', translate = True,required = True)
    description = fields.Text(string = 'Course Description', translate=True)
    image = fields.Image(string ='Image')
    tag_ids = fields.Many2many('course_certification_management.course_tag',relation='course_tag_rel', string='Tags')
    color = fields.Char(string='Color')
    sequence = fields.Integer('Sequence', default=0)
    # Still neede thinking 
    rates = fields.Float(string='Rates')
    rating_count = fields.Integer(string='Rating Count')
    # Option
    level = fields.Selection([
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ], string='Level', default='beginner')
    responsible_id = fields.Many2one('res.users', string='Responsible')
    visibility = fields.Boolean(string='Visibility')
    
    # Content
    content_ids = fields.One2many('course_certification_management.content', 'course_id', string='Contents')
    certification_ids = fields.One2many('course_certification_management.certification', 'course_id', string='Certifications')

    # Participants
    participant_ids = fields.Many2many('res.users', string='Participants')
    

    # Computed Fields
    duration = fields.Float(string='Duration', compute='_compute_duration')
    nbr_participants = fields.Integer(string='Number of Participants', compute='_compute_nbr_participants')
    nbr_contents = fields.Integer(string='Number of Contents', compute='_compute_nbr_contents')
    members_done_count = fields.Integer(string='Number of done', compute='_compute_members_done_count')

   


    # Methodes 

    @api.depends('content_ids')
    def _compute_nbr_contents(self):
        for course in self:
            course.nbr_contents = len(course.content_ids)
    
    @api.depends('participant_ids')
    def _compute_nbr_participants(self):
        for course in self:
            course.nbr_participants = len(course.participant_ids)
    
    @api.depends('participant_ids')
    def _compute_members_done_count(self):
        for course in self:
            course.members_done_count = len(course.participant_ids)

    @api.depends('content_ids.completion_time')
    def _compute_duration(self):
        for course in self:
            course.duration = sum(course.content_ids.mapped('completion_time'))
    

    def open_website_url(self):
        # Your code to handle the action when the button is clicked
        # For example, you can navigate to a URL or perform other actions
        return True
    

    # Your other fields and methods...

   
    def action_view_ratings(self):
        # Define the logic for the action here
        # This method will be called when the "action_view_ratings" link is clicked
        pass

    @api.model
    def action_course_content_form(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'course_certification_management.content',  # Replace with your content model name
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_course_id': self.env.context.get('active_id')},
        }
    @api.model
    def action_course_certification_form(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'course_certification_management.certification',  # Replace with your certification model name
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_course_id': self.env.context.get('active_id')},
        }
    
    



    
   