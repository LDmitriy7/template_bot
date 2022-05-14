poetry export -o requirements.txt --without-hashes

python3 -m pip install pyyaml
python3 on_startup.py

docker compose build
docker compose up -d