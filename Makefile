
kafka:
	docker-compose -f docker-compose-kafka.yml up

clean:
	docker-compose -f docker-compose-kafka.yml down -v
