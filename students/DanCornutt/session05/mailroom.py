#!/usr/bin/env python3

"""
mailroom assignment part 2 & 3
"""
from operator import itemgetter
from collections import OrderedDict


DONORS = {
    "Fred Jones": [100.01, 200, 300], "Amy Shumer": [2000, 4000, 1000],
    "Billy Bills": [1020, 20440.55, 300], "Bob Sherlock": [10, 20, 30],
    "Tom Johnson": [100, 200, 900]
    }

WELCOME_PROMPT = (
    "Welcome to the main menu, please select from the following:\n"
    "1 - Send Thank You to a single donor.\n"
    "2 - Create a report from Donor history.\n"
    "3 - Send letters to all donors.\n"
    "4 - Modify Donor Database.\n"
    "5 - Quit\n"
    )

DATABASE_PROMPT = (
    "Welcome to the database menu, please select from the following:\n"
    "1 - See list of donors.\n"
    "2 - Add new donor or edit existing.\n"
    "3 - Quit this menu.\n"
)


def check_donor(name):
    """Returns True if user is in DB. Writes user if write=True
    :param1: name of donor
    """
    return name in DONORS.keys()

def write_donor(name):
    """Writes thank you email to file"""
    text = """Dearest {donor}, \n
    We greatly thank you for your recent contribution of ${recent:.2f}.\n
    It will go straight to the person who needs it the most, our CEO.\n
    Please give more next time.\n
    \tLove,\n
    \t\t\tThe Team""".format(donor=name, recent=DONORS[name][-1])
    with open(name.replace(" ","") + "_thank_you.txt", 'w') as f_out:
        f_out.write(text)


def thank_you(donor="", all_users=False):
    """Writes thank you letter to file, if all_users is True write letters for all users in database
    """
    if all_users:
        for d in DONORS:
            write_donor(d)
    else:
        donor = input("Type Donor Name =>").title()
        if check_donor(donor):
            write_donor(donor)
        else:
            print("Sorry I could not find the donor, exiting...")


def donor_db():
    """Editing Donor Menu"""
    menu_selection(DATABASE_PROMPT, DATABASE_DISPATCH)


def edit_donor():
    answer = input("input donor name=> ").strip().title()
    if answer:
        add_donation(answer)
    else:
        print("The name must be letters only, returning...")
        thank_you()

def add_donation(donor_name):
    """adds donation to donor records, adds donor if new donor

    :param1: donar name
    """
    donation = add_money()
    if donation:
        DONORS.setdefault(donor_name, []).append(donation)
        print(
            "Thank you {} for your donation of ${:,.2f} dollars!".format(
                donor_name, donation)
        )


def add_money():
    """Takes input from user, validates donation

    :returns: donation amount or None if donation is invalid.
    """
    donation = input("Please enter the donor amount larger than 0.01 => $")
    try:
        if float(donation) < 0.01:
            raise ValueError
    except ValueError:
        print("Donation Error, numbers only. Value must be number greater than 0.01")
        return None
    else:
        return float(donation)


def thank_you_all():
    """Writes thank you email to all users"""
    thank_you(all_users=True)


def report():
    """Finds column widths, sorts donors based on amount donated.
    :returns: report string
    """
    rpt_sheet = []
    len_col = OrderedDict({
        "n_size": len("Donor Name"),
        "t_size" : len("Total Given"),
        "ng_size": len("Num Gifts"),
        "ag_size": len("Average Gift")
    })

    for d in DONORS.items():
        if len(d[0]) > len_col["n_size"]:
            len_col["n_size"] = len(d[0])
        if len(str(sum(d[1]))) > len_col["t_size"]:
            len_col["Tt_size"] = len(str(sum(d[1])))
        if len((d[1])) > len_col["ng_size"]:
            len_col["ng_size"] = len((d[1]))
        if len(str(sum(d[1])/len(d[1]))) > len_col["ag_size"]:
            len_col["ag_size"] = len(str(sum(d[1])/len(d[1])))
        rpt_sheet.append((d[0], sum(d[1]), len(d[1]), sum(d[1])/len(d[1])))
    rpt_sheet.sort(key=return_total, reverse=True)

    sheet = (
        "{nm:{mnm}} | {tot:<{mtot}} | {ng:<{mng}} | {ag:<{mag}}\n{header}".format(
            nm="Donor Name", mnm=len_col["n_size"],
            tot="Total Given", mtot=len_col["t_size"],
            ng="Num Gifts", mng=len_col['ng_size'],
            ag="Average Gift", mag=len_col["ag_size"],
            header=("-" * sum(len_col.values()))
        )
    )
    for d in rpt_sheet:
        sheet = sheet + (
            "\n{n:{n_size}} |${t:>{t_size},.2f} | {ng:>{ng_size}} |$ {avg_g:<{ag_size},.2f}"
            .format(
                n=d[0], n_size=len_col['n_size'],
                t=d[1], t_size=len_col['t_size'],
                ng=d[2], ng_size=len_col['ng_size'],
                avg_g=d[3], ag_size=len_col['ag_size']
                )
        )
    return sheet


def make_report():
    """Prints report"""
    info = report()
    print(info)
    print(sheet)

def return_total(elem):
    """sorting function for list"""
    return elem[1]


def donor_list():
    """prints donor in dict"""
    for k in DONORS:
        print(k)


def unknown():
    """Handles unknown user input"""
    print("That is not a valid response!")


def quit_menu():
    """Quits menu, returns 'exit menu'. """
    print("Quitting this menu now.")
    return "exit menu"


def menu_selection(prompt, dispatch_dict):
    """dispatch function for mailroom"""
    while True: #this loops forever, until quit is selected
        response = input(prompt).strip()
        response = response[:1].lower()
        if dispatch_dict.get(response, unknown)() == "exit menu":
            break

MAIN_DISPATCH = {
    "1": thank_you,
    "2": make_report,
    "3": thank_you_all,
    "4": donor_db,
    "5": quit_menu,
    }

DATABASE_DISPATCH = {
    "1": donor_list,
    "2": edit_donor,
    "3": quit_menu
}

if __name__ == "__main__":
    menu_selection(WELCOME_PROMPT, MAIN_DISPATCH)
