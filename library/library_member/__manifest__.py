{
    "name": "Library Members",
    "description": "Manage members borrowing books.",
    "author": "Italo Silva",
    "license": "AGPL-3",
    "depends": ["library_app", "mail"],
    "application": False,
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        #"views/book_list_template.xml",
        "views/member_list_template.xml",
    ],
    "demo":[
    	"data/library.member.csv",
    ],
    "instalable": True,
    'auto_install': False,
}
