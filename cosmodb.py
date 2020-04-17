
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.documents as documents
import azure.cosmos.http_constants as http_constants
import json

container={
    'id':'Items',
    'partitionKey':{
        'paths':['/location'],
        'kind':documents.PartitionKind.Hash
    }
}

