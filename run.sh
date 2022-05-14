sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

python3 -m pip install poetry pyyaml

poetry export -o requirements.txt --without-hashes

python3 on_startup.py

docker compose build
docker compose up -d
