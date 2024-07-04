up:
	docker compose up

rm:
	sudo docker compose stop && docker rm $(docker ps -a -q) && docker rmi -f $(docker images -q) && rm -rf pgdata

rebuild:
	docker compose up -d --no-deps --build pijawcabot

venv:
	python3 -m venv venv && source venv/bin/activate && pip3 install --upgrade pip

git
	ssh-keygen -t rsa -b 4096 -C «devpijawca@gmail.com» && eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_rsa && cat ~/.ssh/id_rsa.pub