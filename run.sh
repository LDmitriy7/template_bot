python3 -m pip install poetry pyyaml
python3 on_startup.py

poetry export -o requirements.txt --without-hashes

docker compose build
docker compose up -d
