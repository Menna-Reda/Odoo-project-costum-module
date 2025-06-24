from odoo import models, fields, api
class ProjectCollaborator(models.Model):
    _name = 'project_custom.collaborator'
    _description = 'Project Collaborator'
    project_id = fields.Many2one('project.project', string='Project', required=True, ondelete='cascade')
    employee_id = fields.Many2one('hr.employee', string="Employee")
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string="Status", default='active')

    def action_active(self):
        self.write({'status': 'active'})

    def action_inactive(self):
        self.write({'status': 'inactive'})
