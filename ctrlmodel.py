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

    def createWroteRel(self):
        try:
            print 'Start creating WROTE relationship between given nodes'
            searchNodes('Pless').wrote.connect(searchNodes('Here be dragons'))
            searchNodes('Lucy').wrote.connect(searchNodes('Initial Commit'))
            print 'Done creating WROTE relationship between given nodes'
        except Exception, e:
            raise e

    def createReadRel(self):
        try:
            print 'Start creating READ relationship between given nodes'
            searchNodes('John').read.connect(searchNodes('Here be dragons'))
            searchNodes('John').read.connect(searchNodes('Initial Commit'))
            searchNodes('Mary').read.connect(searchNodes('Initial Commit'))
            print 'Done creating READ relationship between given nodes'
        except Exception, e:
            raise e

    def createRecommendedRel(self):
        try:
            print 'Start creating RECOMMENDED relationship between given nodes'
            searchNodes('John').recommended.connect(
                searchNodes('Here be dragons'), {'date': date(1995, 1, 12)})
            # searchNodes('John').recommended.connect(
            #     searchNodes('Initial Commit'), {'date': date(1997, 11, 1)})
            searchNodes('Mary').recommended.connect(
                searchNodes('Initial Commit'), {'date': date(2005, 6, 3)})
            print 'Done creating RECOMMENDED relationship between given nodes'
        except Exception, e:
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
    except DoesNotExist, e:
        pass
    print 'We could not find any node with attribute:', name, '. Please try again.'
