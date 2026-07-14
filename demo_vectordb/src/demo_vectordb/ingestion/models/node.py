from .graph import NodeType

class Node:
	def __init__(self, *, 
		id:int, 
		project_id:int, 
		node_type: NodeType,
		llm_summary: str):

		if not id:
			raise ValueError("id is required")
		elif not isinstance(id, int):
			raise ValueError("id must be integer")

		self.id = id
		self.project_id = project_id
		self.node_type = node_type
		self.llm_summary = llm_summary


	def to_dict(self):
		return self.__dict__.copy()


node = Node(id = 1, project_id=2)

print(node.to_dict())
