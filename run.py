import app

uri="https://andy.documents.azure.com:443/"
primaryKey="f0yq0RS4dHOD1x46AcyeX9hAqYaEBp3jSl2P6pbSUaSqZYRp2hLQ1hGyEuWHNnY0oK5DhLuurAq6hhXxvzIHBw=="
database_name="testDatabase"

client=app.createInstance(uri,primaryKey)
database=app.createDatabase(client,database_name)
container=app.createContainer(client,database)
