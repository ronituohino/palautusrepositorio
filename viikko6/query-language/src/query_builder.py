from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, matcher=And()):
        self.matcher = matcher

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(self.matcher, team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(self.matcher, value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(self.matcher, value, attr))

    def oneOf(self, m1, m2):
        return QueryBuilder(Or(self.matcher, m1, m2))

    def build(self):
        return self.matcher
