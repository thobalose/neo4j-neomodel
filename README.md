# neo4j_neomodel
Getting started with neomodel

## Usage

**Make sure [Neo4j](http://neo4j.com/download/other-releases/) is running first!**

```
$ $NEO4J_HOME/bin/neo4j status
```

**Backup and delete existing data:**

* Backup: Stop Neo4j and copy the `graph.db` folder:
  ```
  $ neo4j stop
  $ cd path/to/neo4j/data
  $ tar -zcf backup_graph.db.tar.gz graph.db/
  ```

* Delete existing data:
  ```
  $ neo4j-shell
  neo4j-sh (?)$ match (x)-[r]-(y) delete x,r,y;
  neo4j-sh (?)$ match (n) delete (n);
  ```

**Run:**
```
$ chmod +x run.sh && ./run.sh
```

**To restore your data:** 

* Stop neo4j and clean out a existing `graph.db` folder, and restore the original `graph.db` folder from your backup:
  ```
  $ neo4j stop
  $ cd data
  $ rm -rf graph.db
  $ tar -zxf backup_graph.db.tar.gz
  ```


