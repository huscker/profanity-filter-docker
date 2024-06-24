# Installation

## Docker


## Docker compose
1. Configure service
```bash
cat .env.template > .env
vim .env
```
2. Run bundle
```bash
docker compose up -d
```

## Helm
1. Add helm repo
```bash
helm repo add profanity-filter-docker https://huscker.github.io/profanity-filter-docker/
```
2. Install chart
```bash
helm install my-profanity-filter profanity-filter-docker/profanity-filter-docker --version 0.1.0
```
