import json
from jsonschema import validate

#Load schema and test data
with open("./schema.json") as s:
    schema = json.load(s)
with open("./data.json") as d:
    data = json.load(d)    
    
# If no exception is raised by validate(), the instance is valid.
validate(instance=data, schema=schema)
print('Test successful')
