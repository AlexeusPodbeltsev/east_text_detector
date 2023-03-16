FROM python:3.10-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /east_text_detector

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.3.2
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock README.md ./

COPY east_text_detector ./east_text_detector/
RUN poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root
#    poetry build

CMD ["poetry", "run", "streamlit", "run", "east_text_detector/demo_view.py", "--server.port=8501", "--server.address=0.0.0.0"]
