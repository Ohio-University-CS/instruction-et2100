# ET2100
This repository is for the ET2100 Engineering Programming class, where students learn Python fundamentals and programming basics.

## Setup
Install uv if it is not already available:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Initialize the project environment in the repository root:

```bash
uv init
```

If you are working with an existing project environment, sync dependencies as needed:

```bash
uv sync
```

## Running Programs
Run a Python file from the project root:

```bash
uv run ./class_sample/01-variable.py
```

Run a script from inside a subfolder:

```bash
cd class_sample
uv run 01-variable.py
```

You only need to run `uv init` once for the project root. If the project is already initialized, you can continue using `uv run` directly.

## Notes
- Use `uv run` to execute Python files in the configured environment.
- If you are opening someone else's project, run `uv sync` first to set up the environment.

