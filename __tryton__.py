#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Account Invoice',
    'name_de_DE': 'Buchhaltung Rechnungsstellung',
    'version': '0.0.1',
    'author': 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'category': 'Accounting',
    'description': '''Financial and Accounting Module with:
    - Payment Term
    - Invoice / Credit Note
    - Supplier Invoice / Supplier Credit Note

With the possibilities:
    - to follow the payment of the invoices.
    - to define invoice sequences on fiscal year or period.
    - to credit any invoice.
''',
    'description_de_DE': '''Modul für Buchhaltung und Rechnungsstellung mit:
    - Definition von Zahlungsbedingungen
    - Erstellung von Rechnungen und Gutschriften für Kunden
    - Erstellung von Rechnungen und Gutschriften für Lieferanten

Ermöglicht:
    - die Verfolgung der Bezahlung von Rechnungen
    - die Definition von Rechnungssequenzen für das Geschäftsjahr bzw. die Buchungszeiträume
    - die Erstellung von Gutschriften zu jeglicher Rechnung
''',
    'depends': [
        'ir',
        'account',
        'company',
        'party',
        'product',
        'res',
        'workflow',
        'currency',
        'account_product',
    ],
    'xml': [
        'invoice.xml',
    ],
    'translation': [
        'fr_FR.csv',
        'de_DE.csv',
        'es_ES.csv',
    ]
}
