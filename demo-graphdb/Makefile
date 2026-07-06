IMAGE = neo4j:latest
CONTAINER = neo4j-ast
USER = neo4j
PASSWORD = password123

run:
	docker run \
		--name $(CONTAINER) \
		-p 7474:7474 \
		-p 7687:7687 \
		-d \
		-e NEO4J_AUTH=$(USER)/$(PASSWORD) \
		$(IMAGE)

stop:
	docker stop $(CONTAINER)

start:
	docker start $(CONTAINER)

restart:
	docker restart $(CONTAINER)

logs:
	docker logs -f $(CONTAINER)

rm:
	docker rm -f $(CONTAINER)

.PHONY: run stop start restart logs rm