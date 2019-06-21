class PartyAnimal:
    party_count = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.party_count += 1
        print(self.name, "party count", self.party_count)

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()