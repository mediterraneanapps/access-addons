{
    "name": """Control access to Apps""",
    "summary": """You can configure administrators which don't have access to Apps""",
    "category": "Access",
    # "live_test_url": "",
    "images": [],
    "version": "12.0.1.3.3",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    'price': 3.33,
    'currency': 'EUR',

    "depends": [
        'web_settings_dashboard',
        'ma_access_restricted'
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'views/access_apps.xml',
        'security/access_apps_security.xml',
        'security/ir.model.access.csv',
    ],
    "demo": [
    ],
    "qweb": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
