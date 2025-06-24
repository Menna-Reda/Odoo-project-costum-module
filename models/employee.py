from odoo import models, fields, api
from odoo.exceptions import UserError

class CustomEmployee(models.Model):
    _inherit = 'hr.employee'
    github_account = fields.Char(string="Github Account", default='Menna-Reda',)
    collaborator_ids = fields.One2many('project_custom.collaborator', 'employee_id', string="Collaborators")

    @api.constrains('active')
    def _check_active_projects_on_archive(self):
        """
        Constraint to prevent archiving an employee who is an active collaborator in any project.
        """
        for employee in self:
            if not employee.active:
                active_collaborations = self.env['project_custom.collaborator'].search([
                    ('employee_id', '=', employee.id),
                    ('status', '=', 'active')
                ])

                if active_collaborations:
                    project_names = ', '.join(active_collaborations.mapped('project_id.name'))
                    raise UserError(_(
                        "You cannot archive employee '%s' because they are still an active collaborator in the following projects: %s. "
                        "Please set their collaboration status to 'inactive' or remove them from these projects first."
                    ) % (employee.name, project_names))