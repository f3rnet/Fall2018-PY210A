# this is the primary function for the program


class Donor():
    def __init__(self, name, donation):
        self.name = name
        self.donations = [donation]  # why are we using this in a class?
          # adds donation to db

    def add_donation(self, donation):
        self.donations.append(donation)

    @property
    def num_donation(self):
        return len(self.donations)

    def sum_donations(self):  # this is avg
        return sum(self.donations) / len(self.donations)


# does this person exist. if not add. if so add donation

class DonorCollection(self, name, donation):
    def __init__(self, donors):
        # donors = {'Bill Gates': [1000, 2000, 3000],
        #           'Rick James': [5000, 5000, 6000, 3000],
        #           'James Brown': [4000, 10000, 9000, 12000],
        #           'Prince': [5500, 6500, 7000, 12000],
        #           'Cat Williams': [2000, 3000, 1000]}

        donors = {}

    def add_donor(self, name, donation):
        if name not in donors:
            donors(name) = [donation]
        else:  # rasise exception not return
            return 'Donor exists'

    def find_donor(self, name):
        if name in donors:
            return name, [i for i in donors[name]]

    def list_donors(self, donors):
        return [i for i in donors.keys()]

    def thank_donors(donors):
        # this function generates a list of donors and their amounts
        # there we determine if the users choice is in the db
        mailto = input(
            "To whom would you like to send a thank you letter? \n"
            "Type 'List' for a list of donors: ")
        if mailto == "List":
            for i in donors:
                print(i)
        elif mailto in donors:
            return ("Dear {}, \n Thank you for your generous donation"
                    " of ${}.".format(mailto,
                                      str(donors[mailto][-1:]).strip('[]')))
        else:
            # now we add the new donor to the db and send an email
            return ("{} not found in donors.".format(mailto))
            user_choice = input(
                "Would you like to add this name to the donor "
                "list? y/n ").lower()
            if user_choice == "y":
                donation_amount = int(input("How much was the "
                                            "donation?: $"))
                donors[mailto] = donation_amount
                return ("Dear {}, \n Thank you for your generous donation"
                        " of ${}.".format(mailto, donation_amount))
            else:
                pass

    def letter_to_everyone(donors):
        for mailto in donors:
            with open(f'{mailto}.txt', 'w') as file:
                file.write("Dear {}, \n Thank you for your generous "
                           "donation of ${}."
                           .format(mailto, str(donors[mailto][-1:])
                                   .strip('[]')))
                file.close()
        return ("Sent Letter to All Donors!")

    def create_report(donors):
        report = ['{:<20}{:<10}{:<5}{:<20}'.format(i, sum(donors[i]), len(
            donors[i]), sum(donors[i]) / len(donors)) for i in donors]
        for i in report:
            print(i)
        return report


# what else do we want to know about a donor?
# sum donation. avg donation. (add these as methods)
# make a class that manages the collection of donors
# input or print doesn't go in Classes





# this exits the program
# this will allow it to take any or no arguments at all without errors.
def goodbye(*args, **kwargs):
    print("Goodbye", exit())


# this function will serve as the menu and prompt the user for choices

def menu():
    functions_list = {"1": thank_you,
                      "2": create_report, "3": everyone, "4": goodbye}

    print('[1] Send a Thank You \n[2] Create a Report \n[3] Send Letters to everyone \n[4] Quit')
    user_choice = input('Enter the number for the required option: ')
    functions_list[user_choice](donors)


def mailroom(donors):
    while True:
        menu()


if __name__ == '__main__':
    donors = get_donors_db()
    mailroom(donors)
