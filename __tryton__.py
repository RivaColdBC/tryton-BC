#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    "name" : "Account Invoice Line Standalone",
    "name_de_DE" : "Fakturierung ungebundene Rechnungsposition",
    "name_fr_FR" : "Ligne de facture autonome",
    "name_es_CO" : "Línea de factura autónoma",
    "name_es_ES" : "Línea de factura independiente",
    "version" : "1.1.0",
    "author" : "B2CK",
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    "description": '''Allow to create standalone invoice lines and add them later to a draft
invoice. The invoice will only accept invoice lines with the same
type, company, currency and party.
''',
    "description_de_DE": '''Fakturierung mit ungebundenen Rechnungspositionen
    - Ermöglicht die Erstellung ungebundener Rechnungspositionen, die später zu
      Rechnungen mit Status Entwurf hinzugefügt werden können.
    - Innerhalb einer Rechnung können nur Rechnungspositionen mit
      übereinstimmendem Typ, Unternehmen, Währung und Partei verwendet werden.
''',
    "description_fr_FR": '''Permet de créer des lignes de facture autonomes et de les ajouter
ensuite à des factures dans l'état brouillon. La facture n'acceptera
que des lignes qui ont les même type, compagnie, devis et tiers.
''',
    "description_es_CO": '''Permite crear líneas individuales para facturación y añadirlas
posteriormente a una factura en borrador. La factuara aceptará únicamente líneas de factura del
mismo tipo, compañía, moneda y tercero.
''',
    "description_es_ES": '''Permite crear líneas de factura independientes y
añadirlas a una factura borrador. La factura solo aceptará líneas de factura
con el mismo tipo, empresa, divisa y tercero.
''',
    "depends" : [
        "ir",
        "account_invoice",
    ],
    "xml" : [
        "invoice.xml",
    ],
    'translation': [
        'de_DE.csv',
        'fr_FR.csv',
        'es_CO.csv',
        'es_ES.csv',
    ],
}
