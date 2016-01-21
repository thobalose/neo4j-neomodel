from model import *
from neomodel import UniqueProperty
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
