IMAGE=neo4j:5.26
CONTAINER=neo4j

run:
	docker run -d \
		--name $(CONTAINER) \
		-p 7474:7474 \
		-p 7687:7687 \
		-e NEO4J_AUTH=neo4j/password \
		-v neo4j_data:/data \
		$(IMAGE)

start:
	docker start $(CONTAINER)

stop:
	docker stop $(CONTAINER)

restart:
	docker restart $(CONTAINER)

logs:
	docker logs -f $(CONTAINER)

shell:
	docker exec -it $(CONTAINER) bash

remove:
	docker rm -f $(CONTAINER)

clean:
	docker rm -f $(CONTAINER) || true
	docker volume rm neo4j_data || true