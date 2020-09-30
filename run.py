import app

uri="unique uri here"
primaryKey="primary key here"
database_name="testDatabase"

client=app.createInstance(uri,primaryKey)
database=app.createDatabase(client,database_name)
container=app.createContainer(client,database)
