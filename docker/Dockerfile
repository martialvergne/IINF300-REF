FROM python:3.9
#ajout d'un utilisateur par sécurité
RUN useradd -ms /bin/bash pythonuser
WORKDIR /app
RUN pip install --no-cache-dir flask==3.1.0
COPY app .
RUN chown -R pythonuser:pythonuser /app
EXPOSE 5000
USER pythonuser
ENV FLASK_APP=/app/main.py
CMD ["flask", "run", "--host", "0.0.0.0"]