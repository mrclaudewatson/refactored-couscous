# UID: U72087839
# Name: Claude Watson
# Description: To calculate the winnings a player may earn in a tournament.

class Person:
    def __init__(self, rn):
        self._realname = rn

class Player(Person):
    def __init__(self, rn, gn, tn, tr):
        Person.__init__(self, rn)
        self.__gamename = gn
        self.__teamname = tn
        self.__teamrank = tr

    def earnings(self, tr):
        p_earning = {"1st": 486500, "2nd": 333750, "3rd": 178000, "4th": 100125, "5th": 55625}
        if tr not in p_earning:
            return 0
        else:
            return p_earning[tr]

    def bonus(self, tr):
        p_bonus = {"1st": 25, "2nd": 20, "3rd": 15, "4th": 10, "5th": 5}
        if tr not in p_bonus:
            return 0
        else:
            return p_bonus[tr]

    def calcearning(self):
        return (self.earnings(self.__teamrank) + (self.earnings(self.__teamrank) * ( self.bonus(self.__teamrank)/100)))/5

    def __str__(self):
        return f"Team {self.__teamname} placed {self.__teamrank}, so they win ${self.earnings(self.__teamrank):,.2f} " \
               f"with a bonus of {self.bonus(self.__teamrank)}%.\n{self._realname} (aka {self.__gamename})'s earning "\
               f"is: ${self.calcearning():,.2f}"

# ---Driver---

realname = input("Enter the player's real name: ")
gamename = input("Enter the player's game name: ")
teamname = input("Enter the team's name: ")
teamrank = input("Enter the team's rank: ")

info = Player(realname, gamename, teamname, teamrank)
print(info)