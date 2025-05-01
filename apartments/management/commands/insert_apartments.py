from django.core.management.base import BaseCommand
from apartments.models import Apartment

class Command(BaseCommand):
    help = 'Insert an apartment into the database with custom values'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, required=True)
        parser.add_argument('--barrio', type=str, required=True)
        parser.add_argument('--ciudad', type=str, required=True)
        parser.add_argument('--pais', type=str, required=True)
        parser.add_argument('--n_personas', type=int, required=True)
        parser.add_argument('--n_banos', type=int, required=True)
        parser.add_argument('--n_camas', type=int, required=True)

    def handle(self, *args, **options):
        Apartment.objects.create(
            Name=options['name'],
            Barrio=options['barrio'],
            Ciudad=options['ciudad'],
            Pais=options['pais'],
            N_Personas=options['n_personas'],
            N_Banos=options['n_banos'],
            N_Camas=options['n_camas'],
        )
        self.stdout.write(self.style.SUCCESS("Departamento ingresado correctamente"))
