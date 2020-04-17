import cosmodb as db


def createInstance(uri,primaryKey):
    print("Creating Account Instance....")
    masterKey={
        "masterKey":primaryKey
    }
    try:
        account_instance=db.cosmos_client.CosmosClient(uri,masterKey)
        print("Account Instance Created!")
        return account_instance
    except db.errors.HTTPFailure as e:
        print("Error: " + e)

def createDatabase(instance,database):
    print("Creating '"+database+"' Database....")
    database_id={
        "id":database
    }
    try:
        database_instance=instance.CreateDatabase(database_id)
        print("'"+database+"' Database Created!")
    except db.errors.HTTPFailure:
       database_instance=instance.ReadDatabase("dbs/"+database)
       print("'"+database+"' Database exists!")
       print("Fetched Data from '"+database+"' Database!")
    return database_instance

def createContainer(instance,database,throughput=400,container=db.container):
    print("Creating '"+container['id']+ "' Container in '"+database['id']+ "' Database....")
    try:
        container_instance=instance.CreateContainer("dbs/"+database["id"],container,{'offerThroughput':throughput})
        print("'"+container['id']+"' Container Created!")
    except db.errors.HTTPFailure as e:
        if e.status_code== db.http_constants.StatusCodes.CONFLICT:
            container_instance=instance.ReadContainer("dbs/"+database["id"]+"/colls/"+ container['id'])
            print("'"+container['id']+"' Container exists!")
            print("Fetched Data from '"+container['id']+"' Container!")
        else:
            print("Error: " + e)
            raise e
    return container_instance