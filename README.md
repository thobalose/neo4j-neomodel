# neo4j_neomodel
Getting started with [neomodel](https://github.com/robinedwards/neomodel)

## Usage

**Make sure [Neo4j](http://neo4j.com/download/other-releases/) is running first!**

```
$ cd path/to/neo4j/bin
$ neo4j status
```

**[Backup](http://stackoverflow.com/questions/25567744/backup-neo4j-community-edition-offline-in-unix-mac-or-linux?answertab=active#tab-top) and delete existing data:**

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
  neo4j-sh (?)$ match (x) delete (x);
  ```

**Run:**
* Recommended:
  * Add the following to `~/.bashrc`:

    ```
    export NEO4J_REST_URL=http://neo4j_username:Neo4j_passwd@localhost:7474/db/data/
    ```

* Maybe (still to be improved...)

  ```
  $ chmod +x set_env.sh && ./set_env.sh
  ```

**To restore your data:** 

* Stop neo4j and clean out a existing `graph.db` folder, and restore the original `graph.db` folder from your backup:

  ```
  $ neo4j stop
  $ cd path/to/neo4j/data
  $ rm -rf graph.db
  $ tar -zxf backup_graph.db.tar.gz
  ```


