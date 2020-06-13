# implement County class here
class County:
    def __init__(self, name, population, voters):
        self.name = name
        self.population = population
        self.voters = voters

    def pct(self):
        return self.voters / self.population


def highest_turnout(datain):
    highestcounty = data[0]
    highestpct = 0
    for county in datain:
        pct = county.pct();
        if pct > highestpct:
            highestcounty = county
            highestpct = pct
    rettuple = (highestcounty.name, highestpct)

    return rettuple


# will be evaluated using these as inputs
allegheny = County("allegheny", 1000490, 645469)
philadelphia = County("philadelphia", 1134081, 539069)
montgomery = County("montgomery", 568952, 399591)
lancaster = County("lancaster", 345367, 230278)
delaware = County("delaware", 414031, 284538)
chester = County("chester", 319919, 230823)
bucks = County("bucks", 444149, 319816)
data = [allegheny, philadelphia, montgomery, lancaster, delaware, chester, bucks]

result = highest_turnout(data)  # do not change this line!
print(result)  # prints the output of the function
# do not remove this line!
