# Profanity filter

[![Build and Tests](https://img.shields.io/github/actions/workflow/status/huscker/profanity-filter-docker/build.yaml?branch=main)](https://github.com/huscker/profanity-filter-docker/actions/workflows/build.yaml)
[![Docker Pulls](https://img.shields.io/docker/pulls/huscker/profanity-filter-docker)](https://hub.docker.com/r/huscker/profanity-filter-docker)
[![Artifact Hub repo](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/profanity-filter-docker)](https://artifacthub.io/packages/helm/profanity-filter-docker/profanity-filter-docker)
[![Apache-2.0 license](https://img.shields.io/github/license/huscker/profanity-filter-docker)](https://github.com/huscker/profanity-filter-docker/blob/main/LICENSE)
[![Built with Devbox](https://www.jetify.com/img/devbox/shield_moon.svg)](https://www.jetify.com/devbox/docs/contributor-quickstart/)
---
Open-source service for filtering profane text.

Currently supported filtering backends:
- [profanity_filter](https://github.com/rominf/profanity-filter)

Features:
- Dynamic configuration of filtering backends
- Customizable list of profane words
- Admin panel for administration
- Service metrics included
# Installation
## From source
Make sure you have Python `v3.10` and poetry v`1.8.0+` installed.
1. Clone repository
```bash
git clone https://github.com/huscker/profanity-filter-docker.git
cd profanity-filter-docker
```
2. Install dependencies
```bash
poetry install --no-root
poetry shell
spacy download en
```
3. Configure service
```bash
cat .env.template > .env
vim .env
```
4. Run service
```bash
poetry run uvicorn service.__main__:app --host 0.0.0.0 --port 8000 --log-level info
```

## From docker-compose
1. Configure service
```bash
cat .env.template > .env
vim .env
```
2. Run bundle
```bash
docker compose up -d
```

## From helm
1. Add helm repo
```bash
helm repo add profanity-filter-docker https://huscker.github.io/profanity-filter-docker/
```
2. Install chart
```bash
helm install my-profanity-filter profanity-filter-docker/profanity-filter-docker --version 0.1.0
```
# Contribute guide
1. Fork repository
2. Clone your fork
3. Commit and push changes
4. Make a pull request to this repository
[For more details please follow github docs](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project#forking-a-repository).
