from django.core.management.base import BaseCommand
from TwinBrooksUser.models import User, UserPhoneNumber


# Takes a list of members code and their phone numbers and cross references that with the atual member list
# This saves the member's phone numbers into their user account bysearching for the membercode inside of the 
# UserPhoneNumber model.

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users_converted = 0
        users_not_converted = 0
        for user in User.objects.all():
            if not user.is_staff:
                users_converted += 1
                connected_user_phonenumber = UserPhoneNumber.objects.all().filter(member_code=user.member_code)
                if connected_user_phonenumber:
                    connected_user_phonenumber = connected_user_phonenumber.first()
                    user.phone_numner = connected_user_phonenumber.phone_numner
                    user.save()
                #  print str(user.get_short_name()) + "'s  phonenumber was saved"
                else:
                    users_not_converted += 1
                    print str(user.get_short_name()) + "'s  Phonenumber Not Added"
                    pass
            else:
                print "user was not staff"

        print "Completed"
        print str(users_converted) + " phonenumbers were added"
        print str(users_not_converted) + " phonenumbers were not added."
