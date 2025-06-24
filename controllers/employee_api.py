from odoo import http
from odoo.http import request
import json
import base64

class EmployeeWithActiveProjects(http.Controller):

    @http.route('/api/employees_with_active_projects/', type='http', auth='none', csrf=False, methods=['GET'])
    def employees_with_thier_active_projects(self, **kwargs):
        """
        API endpoint to list all employees with their active projects.
        Authentication: Basic
        Method: GET
        Response: JSON
        """
        try:
            # Check for Basic Authentication manually
            auth_header = request.httprequest.headers.get('Authorization')

            if not auth_header or not auth_header.startswith('Basic '):
                return request.make_json_response({'error': 'Authentication required. Use Basic Auth.'}, headers={'Content-Type': 'application/json', 'WWW-Authenticate': 'Basic realm="Odoo API"'}, status=401)
            
            # Decode the Basic Auth credentials
            encoded_credentials = auth_header.split(' ')[1]
            try:
                decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
                username, password = decoded_credentials.split(':', 1)
            except (UnicodeDecodeError, ValueError):
                return request.make_json_response({'error': 'Invalid Basic Auth credentials format.'}, headers={'Content-Type': 'application/json', 'WWW-Authenticate': 'Basic realm="Odoo API"'}, status=401)

            # Authenticate the user
            try:
                request.session.authenticate(request.session.db, username, password)
            except Exception: # Catches errors if authentication fails (e.g., wrong username/password)
                return request.make_json_response({'error': 'Authentication failed. Invalid username or password.'}, headers={'Content-Type': 'application/json', 'WWW-Authenticate': 'Basic realm="Odoo API"'}, status=401)

            # Fetch employees with their active projects
            employees = request.env['hr.employee'].sudo().search([])
            res = []
            for employee in employees:
                active_projects = request.env['project_custom.collaborator'].sudo().search([
                    ('employee_id', '=', employee.id),
                    ('status', '=', 'active')
                ])
                project_names = active_projects.mapped('project_id.name')
                res.append({
                    'employee_id': employee.id,
                    'name': employee.name,
                    'job_title': employee.job_id.name if employee.job_id else '',
                    'work_email': employee.work_email or '',
                    'github_account': employee.github_account,
                    'active_projects': project_names
                })
            return request.make_json_response(res)

        except Exception as e:
            return request.make_json_response({'error': str(e)}, status=500)
