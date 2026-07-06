# graph/queries/function_queries.py

CREATE_FUNCTION = """
MERGE (f:Function {id:$id})

SET

f.name=$name,

f.start_line=$start,

f.end_line=$end
"""


LINK_FILE_FUNCTION = """

MATCH (file:File {path:$path})

MATCH (func:Function {id:$id})

MERGE (file)-[:CONTAINS]->(func)

"""