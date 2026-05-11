from django.db import migrations
from datetime import date


PRODUCTS = [
    {"barcode": "5901234123457", "name": "Borjomi Sparkling Water",       "description": "Naturally carbonated mineral water from Georgia.",  "price": "3.50",  "quantity": 120, "unit": "milliliter", "expire_at": date(2027, 1, 15), "color": "#0a7a3b"},
    {"barcode": "5901234123458", "name": "Saperavi Dry Red",              "description": "Full-bodied dry red wine, Kakheti region.",          "price": "24.90", "quantity": 40,  "unit": "milliliter", "expire_at": date(2030, 6, 1),  "color": "#5c0a1d"},
    {"barcode": "5901234123459", "name": "Tarragon Lemonade",             "description": "Classic Georgian green lemonade.",                   "price": "2.80",  "quantity": 80,  "unit": "milliliter", "expire_at": date(2026, 12, 20), "color": "#7fbf3f"},
    {"barcode": "5901234123460", "name": "Cold-Pressed Sunflower Oil",    "description": "Unrefined, golden, family-pressed.",                 "price": "12.00", "quantity": 25,  "unit": "Liter",      "expire_at": date(2027, 3, 10), "color": "#e0a92f"},
    {"barcode": "5901234123461", "name": "Tkemali Plum Sauce",            "description": "Sour plum sauce with herbs, traditional recipe.",    "price": "6.40",  "quantity": 60,  "unit": "milliliter", "expire_at": date(2027, 8, 5),  "color": "#7a2233"},
    {"barcode": "5901234123462", "name": "Mountain Wildflower Honey",     "description": "Raw honey from Tusheti highlands.",                  "price": "18.50", "quantity": 30,  "unit": "milliliter", "expire_at": date(2028, 5, 1),  "color": "#c98a1a"},
    {"barcode": "5901234123463", "name": "Chacha Aged Spirit",            "description": "Georgian grape brandy, oak-aged 6 years.",           "price": "45.00", "quantity": 18,  "unit": "milliliter", "expire_at": None,              "color": "#b88a4a"},
    {"barcode": "5901234123464", "name": "Walnut Churchkhela",            "description": "Strung walnuts in grape-must, traditional sweet.",   "price": "4.20",  "quantity": 100, "unit": "milliliter", "expire_at": date(2026, 11, 1), "color": "#3a1e10"},
    {"barcode": "5901234123465", "name": "Mtsvane Amber Wine",            "description": "Skin-contact white from qvevri.",                    "price": "32.00", "quantity": 22,  "unit": "milliliter", "expire_at": date(2031, 4, 15), "color": "#d9a441"},
    {"barcode": "5901234123466", "name": "Svaneti Salt Blend",            "description": "Aromatic herb-salt from the mountains.",             "price": "5.60",  "quantity": 75,  "unit": "milliliter", "expire_at": date(2028, 9, 30), "color": "#a8916b"},
]


def seed_products(apps, schema_editor):
    Product = apps.get_model("core", "Product")
    Product.objects.bulk_create([Product(**p) for p in PRODUCTS])


def unseed_products(apps, schema_editor):
    Product = apps.get_model("core", "Product")
    Product.objects.filter(barcode__in=[p["barcode"] for p in PRODUCTS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_products, unseed_products),
    ]
