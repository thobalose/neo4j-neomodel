from neomodel import (StructuredNode, StructuredRel,
                      StringProperty, DateProperty, RelationshipTo, OneOrMore)


class Recommended(StructuredRel):
    """docstring for Recommended"""
    date = StringProperty(default=None)


class Author(StructuredNode):
    print 'Class for Author nodes'
    # Names shoud not be duplicate (Unique_Index=True)
    # http://neo4j.com/docs/stable/query-constraints.html
    name = StringProperty(Unique_Index=True, required=True)
    # The DateProperty accepts datetime.date objects which are stored as a
    # string property YYYY-MM-DD
    born = DateProperty()
    died = DateProperty(default=None)

    wrote = RelationshipTo('Book', 'WROTE', OneOrMore)
    recommended = RelationshipTo(
        'Book', 'RECOMMENDED', OneOrMore, model=Recommended)


class Book(StructuredNode):
    print 'Class for Book nodes'

    title = StringProperty(Unique_Index=True, required=True)
    published = DateProperty()


class Reader(StructuredNode):
    print 'Class for Reader nodes'

    name = StringProperty(Unique_Index=True, required=True)
    born = DateProperty()

    read = RelationshipTo('Book', 'READ', OneOrMore)
    recommended = RelationshipTo(
        'Book', 'RECOMMENDED', OneOrMore, model=Recommended)
