from neomodel import (StructuredNode, StringProperty, DateProperty)


class Author(StructuredNode):
    print 'Class for Author nodes'
    # Names shoud not be duplicate (Unique_Index=True)
    # http://neo4j.com/docs/stable/query-constraints.html
    name = StringProperty(Unique_Index=True, required=True)
    born = DateProperty()
    died = DateProperty()


class Book(StructuredNode):
    print 'Class for Book nodes'

    title = StringProperty(Unique_Index=True, required=True)
    published = DateProperty()


class Reader(StructuredNode):
    print 'Class for Reader nodes'

    name = StringProperty(Unique_Index=True, required=True)
    born = DateProperty()
