1) create secrets/env.toml from secrets/env.sample.toml
2) docker build -t template_bot .
3) docker run --network=host --restart=unless-stopped -d template_bot