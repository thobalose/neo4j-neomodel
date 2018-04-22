from ctrlmodel import ctrlModel, deleteData


if __name__ == '__main__':
    deleteData()  # Start by deleting existing data
    create = ctrlModel()
    create.ctrlNodes()
    # searchNodes('Here be dragons')
    create.createWroteRel()
    create.createReadRel()
    create.createRecommendedRel()
    print 'Done!'
