FROM python:3.12.5-slim-bullseye

RUN apt update

RUN apt install -y gcc

RUN apt install -y libpq-dev

WORKDIR /ppbglobal

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY leaderboard_site .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["bash"]

# FROM debian:bookworm

# CMD ["/bin/bash"]