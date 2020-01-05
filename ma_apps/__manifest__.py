{
    'name': 'Custom Apps',
    'summary': """Simplify Apps Interface""",
    'images': [],
    'version': '1.0.0',
    'application': False,
    'author': 'Mediterranean Apps',
    "support": "mediterranean.apps@gmail.com",
    'category': 'Access',
    'license': 'LGPL-3',

    'depends': [
        'ma_access_apps',
    ],
    'data': [
        'views/apps_view.xml',
        'security.xml',
        'data/ir_config_parameter.xml',
    ],

    'post_load': None,
    'pre_init_hook': None,
    'post_init_hook': None,

    'auto_install': False,
    'installable': False
}
