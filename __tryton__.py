#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Stock Inventory for many locations',
    'name_fr_FR': 'Inventaire de stock par liste de locations',
    'name_de_DE': 'Lagerverwaltung Bestandskorrektur für mehrere Lagerorte',
    'version': '0.0.1',
    'author': 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'description': '''Add a wizard that allows to create automatically inventories for a
given list of locations. It also allows to filter by product and
categories of product.
    ''',
    'description_fr_FR': '''Ajoute un wizard qui permet de créer automatiquement des inventaires
pour une liste donnée d'emplacements. Il permet aussi de filtrer par
produit et par catégorie de produit.
''',
    'description_de_DE': '''Bestandskorrektur für mehrere Lagerorte
    - Fügt einen Wizard hinzu, der automatisch die Lagerbestände für eine Liste
      von Lagerorten erzeugt.
    - Ermöglicht die Filterung der Auswahl nach Artikel oder Artikelkategorie.
''',
    'depends': [
        'ir',
        'stock',
        'company',
        'product',
    ],
    'xml': [
        'inventory.xml',
    ],
    'translation': [
        'fr_FR.csv',
        'de_DE.csv',
    ],
}
