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
