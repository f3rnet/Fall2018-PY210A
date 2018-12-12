import os
from mailroom4 import Donor, DonorCollection


def test_donor_name():
    donor = Donor("Fred Flintstone", 3000)
    assert donor.donations is not None
    assert donor.name == "Fred Flintstone"


def test_donor_thank_you_letter():
    pass


def test_donor_collection():
    dc = DonorCollection()
    assert len(dc.add_donor("Bob", 9000)) >= 1
    assert "Bob" in dc.add_donor("Bob", 9000)

    assert dc.find_donor("Bob") is not None

    assert "Bob" in dc.list_donors("Bob")

    mailto = "List"
    print(dc.thank_donors(mailto))


def test_sum_donations():
    d = Donor('Jon', 5000)
    assert d.sum_donations() == 5000


def test_avg_donations():
    d = Donor('Jon', 5000)
    assert d.avg_donations() == 5000
    assert d.avg_donations() != 6000


def test_num_donations():
    d = Donor('Jon', 5000)
    assert d.num_donations() == 1
    assert d.num_donations() >= 0
    # assert type(d.sum_donations()) == int


def test_add_donations():
    d = Donor("Fred Flintstone", 3000)
    d.add_donations(500)
    assert len(d.donations) is not 0




# def test_get_donors_db():
#     # test that the database function returns a full database
#     donors = get_donors_db()
#     assert len(donors) != 0
#     assert len(create_report(donors)) == len(donors)


# def test_everyone():
#     donors = get_donors_db()
#     # tests that a file was created for each donor emailed
#     everyone(donors)
#     for i in donors:
#         assert os.path.exists(i + ".txt")
