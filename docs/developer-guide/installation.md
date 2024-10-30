# Installation
## From source
Make sure you have Python `v3.10` and poetry v`1.8.0+` installed.
1. Install dependencies
```bash
poetry install --no-root
poetry shell
spacy download en
```
2. Configure service
```bash
cat .env.template > .env
vim .env
```
3. Run service
```bash
poetry run uvicorn service.__main__:app --host 0.0.0.0 --port 8000 --log-level info
```

## Using devbox
1. Prepare devbox environment
```bash
devbox install
```
2. Install project dependencies
```bash
devbox run install
```
3. Start services
```bash
devbox services up
```
4. Migrate database
```bash
devbox run migrate
```
5. Launch service
```bash
devbox run web
```
