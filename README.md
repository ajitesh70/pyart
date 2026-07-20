# Demo: Passing Python wheels as GitHub Actions artifacts

Small demo showing how Job 1 produces Python wheels that Job 2 consumes during a Docker build.

Quick run (locally):

1. Create and activate a venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dev deps and run tests:

```powershell
pip install -r requirements-dev.txt -r requirements.txt
pytest
```

3. Build wheels for the Docker build to consume, then build the image:

```powershell
pip wheel -r requirements.txt -w wheelhouse
docker build -t demo-app:local .
```

What the workflow does:

- **Job `test`**: runs tests, builds wheels into `wheelhouse/`, and uploads them as an artifact named `python-wheels`.
- **Job `image`**: depends on `test`, downloads the `python-wheels` artifact into `./wheelhouse`, then runs `docker build`.

The key Dockerfile line that uses the artifact is:

```
COPY wheelhouse/ /wheels/
RUN pip install --no-index --find-links=/wheels -r requirements.txt
```

Note: if `--no-index` is removed, pip would hit the network and the artifact would be pointless — keeping `--no-index` proves the artifact is actually required.

Where to find the artifact in the GitHub UI: Actions → click the workflow run → scroll to the bottom → Artifacts
