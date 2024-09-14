FROM python:3.12.5-slim-bullseye

WORKDIR /ppbglobal

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY leaderboard_site .

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["bash"]