from odoo import fields, models
from odoo.exceptions import ValidationError


class Book(models.Model):

    _name = "library.book"
    _description = "Libro"

    name = fields.Char("Titulo", required=True)
    isbn = fields.Char("ISBN")
    notes = fields.Text("Internal Notes")
    descr = fields.Html("Descripcion")
    last_borrow_date = fields.Datetime("Fecha de prestamo",
    	default=lambda self: fields.Datetime.now(),)
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner", string="Editor")
    author_ids = fields.Many2many("res.partner", string="Autores")
    gender = fields.Char(string="Género")
    _sql_constraints = [
        ("library_book_name_date_uq",
         "UNIQUE (name, date_published)",
         "Book title and publication date must be unique."),
        ("library_book_check_date",
         "CHECK (date_published <= current_date)",
         "Publication date must not be in the future."),
    ]

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide an ISBN for %s" % book.name)
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s ISBN is invalid" % book.isbn)
        return True
