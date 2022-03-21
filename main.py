import json

def get_type(v):
    info = {
        "tag": "",
        "description": "",
        "required": False
    }

    t = type(v)

    if t == str:
        info["type"] = "string"
    elif t == int:
        info["type"] = "integer"
    elif t == list:
        c_type = get_type(v[0])["type"]
        if c_type == "string":
            info["type"] = "enum"
        elif c_type == "object":
            info["type"] = "array"
    elif isinstance(t, object):
        info["type"] = "object"

    return info


def build_schema(root):
    schema = dict()
    for k in root:
        v = root[k]
        t = get_type(v)

        if t["type"] == "object":
            schema[k] = build_schema(v)
        else:
            schema[k] = t
    return schema


f = open("./data.json")
corpus = json.load(f)
schema = build_schema(corpus["message"])
print(schema)
f.close()

ff = open("schema.json", "w")
json.dump(schema, ff)