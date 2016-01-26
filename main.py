from model import *
from ctrlmodel import *

if __name__ == '__main__':
    print 'ctrlNodes...'
    create = ctrlModel()
    create.ctrlNodes()
    searchNodes('Here be dragons')
    create.createWroteRel()
    create.createReadRel()
    print 'Done!'
