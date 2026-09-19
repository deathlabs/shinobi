FROM alpine:3.24
LABEL image.authors="Vic Fernandez III <@cyberphor>"
WORKDIR /home/tools/
COPY pyproject.toml pyproject.toml
COPY shinobi/ shinobi/
COPY uv.lock uv.lock
ENV UV_PYTHON_INSTALL_DIR=/home/tools/.uv-python
RUN apk add --no-cache python3 git uv && \
    apk upgrade --no-cache libcrypto3 libssl3 &&\
    uv sync --frozen --python /usr/bin/python3 && \
    uv run python -m pip uninstall pip -y || true &&\
    (apk del wget || true) &&\
    addgroup -g 1000 shinobi &&\
    adduser -D -G shinobi -u 1000 shinobi -h /home/tools/ &&\
    mkdir -p /home/tools/workspace &&\
    chmod ug+rwx,o+rx,g+s /home/tools/workspace &&\
    chown -R shinobi:shinobi /home/tools/
ENV PATH="/home/tools/.venv/bin:$PATH"
USER shinobi
EXPOSE 8002
CMD [ "python", "-m", "shinobi.main" ]
