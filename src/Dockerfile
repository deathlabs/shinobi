FROM alpine:3.24
LABEL image.authors="Vic Fernandez III <@cyberphor>"
WORKDIR /home/shinobi/
COPY pyproject.toml pyproject.toml
COPY shinobi/ shinobi/
COPY uv.lock uv.lock
ENV UV_PYTHON_INSTALL_DIR=/home/shinobi/.uv-python
RUN apk add --no-cache python3 git uv && \
    apk upgrade --no-cache libcrypto3 libssl3 &&\
    uv sync --frozen --python /usr/bin/python3 && \
    uv run python -m pip uninstall pip -y || true &&\
    (apk del wget || true) &&\
    addgroup -g 1000 shinobi &&\
    adduser -D -G shinobi -u 1000 shinobi -h /home/shinobi/ &&\
    mkdir -p /home/shinobi/workspace &&\
    chmod ug+rwx,o+rx,g+s /home/shinobi/workspace &&\
    chown -R shinobi:shinobi /home/shinobi/
ENV PATH="/home/shinobi/.venv/bin:$PATH"
USER shinobi
EXPOSE 8002
CMD [ "python", "-m", "shinobi.main" ]
