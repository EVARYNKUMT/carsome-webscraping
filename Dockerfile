FROM python:3.10-slim

RUN apt-get update && apt-get install -y tzdata

ENV TZ=Asia/Kuala_Lumpur

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sleep", "infinity"]