# Installation

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
1. Add charts repo
```console
helm repo add profanity-filter-charts https://huscker.github.io/profanity-filter-charts/
```

2. Install chart
```bash
helm install profanity-filter profanity-filter-charts/profanity-filter --version 1.0.0
```
