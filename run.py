import app

uri="unique uri here"
primaryKey="primary key heree"
database_name="testDatabase"

client=app.createInstance(uri,primaryKey)
database=app.createDatabase(client,database_name)
container=app.createContainer(client,database)
