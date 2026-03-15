{
    'name': 'Hospital,College & Research Center Management',
    'version': '18.0',
    'sequence': 1,
    'category': 'Healthcare',
    'summary': 'Manage patients, doctors, appointments, and medical stores',
    'description': """
        A comprehensive Hospital Management System module for managing:
        - Patient master
        - Doctor master
        - Central medical store
        - Appointments
        - Prescriptions
        - Billing and invoicing
    """,
    'author': 'Omkar Kadam',
    'company': 'Evozard Consulting Service PVT LTD',
    'maintainer': 'Online Service',
    'website': 'https://www.yourcompanywebsite.com',
    'depends': ['base','mail','contacts','product'],

    'data': [
        'security/ir.model.access.csv',
        # 'views/menu.xml',
        # 'security/security.xml',
        'views/college_view.xml',
        'views/doctor_view.xml',
        'views/medical_store.xml',
        # 'views/student_view.xml',
        # 'views/appointment_views.xml',
        # 'data/demo_data.xml',
        # 'report/patient_report.xml',
        # 'wizard/doctor2patient_appointment_wizard.xml',
    ],
    'demo': [
        # 'data/demo_data.xml',
    ],
    # 'images': ['static/description/icon.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
