# -*- coding: utf-8 -*-
{
    'name': "project_custom",

    'summary': "projects' development progress tracking with clients using Odoo ",

    'author': "Menna Reda",

    'version': '17.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'web',
                'hr',
                'project',
                'web_tour'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/collaborator_views.xml',
        'views/project_views.xml',
        'views/hr_employee_views.xml',
        'reports/project_report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

