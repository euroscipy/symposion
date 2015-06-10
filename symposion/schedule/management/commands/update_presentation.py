from django.core.management.base import BaseCommand, CommandError
from symposion.schedule.models import Presentation

class Command(BaseCommand):
    args = 'presentation_id'
    help = 'updates the specified presentation from its base proposal'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError("provide a single presentation id")
        pk = int(args[0])
        try:
            presentation = Presentation.objects.get(pk=pk)
        except Presentation.DoesNotExist:
            raise CommandError('Presentation "%s" does not exist' % pk)

        presentation.update_from_proposal()

        self.stdout.write('Successfully update presentation "%s"' % pk)

