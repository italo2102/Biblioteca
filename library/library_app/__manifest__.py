{
    "name": "Biblioteca",
    "summary": "Modelo para una biblioteca, biblioteca y catálogos de libros",
    "author": "Italo Silva Guanilo",
    "license": "AGPL-3",
    "website": "https://github.com/italo2102/Biblioteca/tree/main/library",
    "version": "15.0.1.0.0",
    "category": "Services/Library",
    "depends": ["base"],
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
        ],
    "demo": [
        "data/res.partner.csv",
        "data/library.book.csv",
    ],
    "application": True,
}
