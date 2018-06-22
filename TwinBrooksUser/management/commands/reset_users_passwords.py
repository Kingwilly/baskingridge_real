from django.core.management.base import BaseCommand

from TwinBrooksUser.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            # Changes all passwords of users who are not staff.
            if not user.is_staff:
                user.set_password('watchungvalleygc')
                user.save()
                print user.get_short_name() + "'s password has been changed"

        print "Completed"
