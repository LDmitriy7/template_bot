1) You must create env.toml from env-sample.toml
2) docker build -t template_bot .
3) docker run --network=host --restart=unless-stopped -d template_bot