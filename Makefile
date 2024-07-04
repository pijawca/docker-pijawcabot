up:
	docker compose up

rm:
	sudo docker compose stop \
	&& docker rm $(docker ps -a -q) \
	&& docker rmi -f $(docker images -q) \
	&& rm -rf pgdata \

rebuild:
	docker compose up -d --no-deps --build pijawcabot