python -m pip -q install pyyaml

poetry export -o requirements.txt --without-hashes
python on_startup.py

docker compose build
docker compose up -d
