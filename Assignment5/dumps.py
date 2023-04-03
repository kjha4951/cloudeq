#JavaScript object notation.
import json

x={"name": "komal",  "age":21,   "number":44444}
k=json.dumps(x)
print(type(k))

x='{"name": "komal",  "age":21,   "number":44444}'
k=json.loads(x)
print(type(k))

