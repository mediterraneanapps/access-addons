{
    "name": """Multiwebsite in Sec.Rules""",
    "summary": """Provide access depending on current website""",
    "category": "Access",
    "images": ['images/ir_rule_website.jpg'],
    "version": "12.0.1.3.2",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 6.00,
    "currency": "EUR",

    "depends": [
        "web_website",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/ir_rule_views.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
