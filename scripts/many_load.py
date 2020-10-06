from unesco.models import Site, Category, States, Region, Iso
import csv

def run():
    fhand = open('data/unesco_data.csv')
    reader = csv.reader(fhand)

    next(reader) # Skipping header row or 1st row

    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    #name	description	justification	year	longitude	latitude	area_hectares	category	states	region	iso

    for row in reader:
        c = Category.objects.get_or_create(name=row[7])[0]
        s = States.objects.get_or_create(name=row[8])[0]
        r = Region.objects.get_or_create(name=row[9])[0]
        i = Iso.objects.get_or_create(name=row[10])[0]

        try:
            y = int(row[3])
        except:
            y = None
        try:
            area = float(row[6])
        except:
            area = None
        site = Site(
            name=row[0],
            description=row[1],
            justification=row[2],
            year=y,
            longitude=row[4],
            latitude=row[5],
            area_hectares=area,
            category=c,
            states=s,
            region=r,
            iso=i)
        site.save()
