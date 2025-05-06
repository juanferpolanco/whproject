from django.db import connection
from .models import Apartment

def get_available_apartments(start_date, end_date, ciudad, distrito):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_available_apartments(%s, %s, %s, %s)", [start_date or None, end_date or None, ciudad or None, distrito or None])
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    # Convert raw rows into Apartment model instances (not saved, just in-memory)
    apartments = []
    for row in results:
        apartment = Apartment(
            id=row['id'],
            Name=row['name'],
            Barrio=row['barrio'],
            Ciudad=row['ciudad'],
            Pais=row['pais'],
            N_Banos=row['n_banos'],
            N_Camas=row['n_camas'],
            N_Personas=row['n_personas']
        )
        apartments.append(apartment)
    
    return apartments