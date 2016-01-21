from model import *
from neomodel import UniqueProperty, DoesNotExist
from datetime import date


class ctrlModel():

    def ctrlNodes(self):
        try:
            # Create Authors
            Author(name='Pless', born=date(1900, 01, 01),
                   died=date(1990, 12, 12)).save()
            Author(name='Lucy', born=date(1950, 12, 12)).save()
            # Create Books
            Book(title='Here be dragons', published=date(1950, 12, 12)).save()
            Book(title='Initial Commit', published=date(1990, 12, 12)).save()
            # Create Readers
            Reader(name='John', born=date(1980, 05, 06)).save()
            Reader(name='Mary', born=date(1985, 03, 07)).save()
        except UniqueProperty, e:
            raise e


def searchNodes(name):
    try:
        print 'Searching Node with Name=', name
        # Search all nodes with Label Author
        node = Author.nodes.get(name=name)
        # If this is found, print its attributes
        print node.labels(), 'Name =', node.name, 'Born:', node.born
        return node
    except DoesNotExist, e:
        pass
    try:
        # Searching all nodes with Label Book
        node = Book.nodes.get(title=name)
        print node.labels(), 'Title =', node.title, 'Published:', node.published
        return node
    except DoesNotExist, e:
        pass
    try:
        # Search all nodes with Label Reader
        node = Reader.nodes.get(name=name)
        print node.labels(), 'Name =', node.name, 'Born:', node.born
        return node
    except Exception, e:
        pass
    print 'We could not find any node with attribute:', name, '. Please try again.'
