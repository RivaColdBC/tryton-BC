#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Account Invoice History',
    'name_de_DE': 'Fakturierung Historisierung',
    'name_es_CO': 'Histórico de Facturación',
    'name_es_ES': 'Histórico de Facturación',
    'version': '1.3.0',
    'author': 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'description': '''Add historization for Invoice fields.
''',
    'description_de_DE': '''Fügt Historisierung zu den Rechnungsfeldern hinzu
''',
    'description_es_CO': '''Histórico de Facturación a nivel de campos
''',
    'description_es_ES': '''Histórico de Facturación a nivel de campos
''',
    'description_fr_FR': '''Ajoute l'historisation au champs de la facture.
''',
    'depends': [
        'account_invoice',
        'party',
    ],
    'xml': [
    ],
    'translation': [
        'de_DE.csv',
        'es_CO.csv',
        'es_ES.csv',
        'fr_FR.csv',
    ]
}
