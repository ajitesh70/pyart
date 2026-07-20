# Simple Python unit test demo

A tiny demo project with a Flask app and a simple pytest suite.

Quick run (locally):

1. Create and activate a venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies and run tests:

```powershell
pip install -r requirements-dev.txt -r requirements.txt
pytest
```

What the workflow does:

- **Job `test`**: checks out the repo, sets up Python, installs dependencies, runs `pytest`, and creates a generic build artifact.
- **Job `image`**: downloads the artifact, copies it into the Docker build context, and builds the image.

The Docker image build now consumes a build artifact produced by the earlier test job, without using wheel or wheelhouse packaging.
