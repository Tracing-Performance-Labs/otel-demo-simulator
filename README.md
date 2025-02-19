# OTEL Demo Simulator

This repository contains various scripts that simulate actions
on the OTEL Demo website.

The purpose is to simulate normal user interaction in order to
capture the trace data emitted to study it.

## Build the docker image

```
docker build otel-demo-simulator .
```

## Run with the docker image

```
docker run -it --rm \
    -e OTEL_DEMO_APP_URL=http://0.0.0.0:8080 \
    --network=host \
    otel-demo-simulator
```

This assumes you have the demo application running locally on port 8080.
Replace as needed.

## License
MIT
