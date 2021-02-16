class Party:

    def __init__(self):
        self.list_peoples = list()

    def total_people(self):
        sum_people = len(self.list_peoples)
        return sum_people


party = Party()
while True:
    name = input()
    if name == "End":
        break
    party.list_peoples.append(name)
party.total_people()
print(f"Going: {', '.join(party.list_peoples)}")
print(f"Total: {party.total_people()}")
