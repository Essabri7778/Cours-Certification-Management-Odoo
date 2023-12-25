from odoo import http
from odoo.http import request

class CourseManagementWebsite(http.Controller):


    @http.route('/home', auth='public', website=True)
    def home_page(self, **kwargs):
        courses = request.env['course_certification_management.course'].sudo().search([])  # Adjust model name
        return request.render('Cours_Certifications_Management_Odoo.home_page', {
            'courses': courses,
        })
