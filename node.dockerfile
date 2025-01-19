FROM python:3.12-bookworm

RUN python -m pip install uv

COPY pyproject.toml .
COPY README.md .
COPY uv.lock .

RUN uv sync --frozen --no-install-project --no-dev

COPY . .

RUN uv sync --frozen

CMD ["uv", "run", "mcp-mesh"]
