# Agent Manual for django-oscar

This document is a guide for AI agents working on the `django-oscar` repository.

## Project Overview

This is the repository for `django-oscar`, an open-source e-commerce framework for Django.
Development and testing is often done within the `sandbox` project, which is a self-contained Oscar site.

## Development

### Running the Sandbox Server

The `sandbox` is a pre-configured Django project for testing and development. It runs on the `gunicorn` WSGI server to ensure compatibility with tools like New Relic, even in a development environment.

To run the development server, use the `run_sandbox.sh` script, which has several modes:

1.  **Start in the background (default):**
    ```bash
    ./scripts/run_sandbox.sh
    ```
    This will start the gunicorn server in the background. Logs are stored in `logs/sandbox.log` and the process ID in `logs/sandbox.pid`.

2.  **Start in the background and tail logs:**
    ```bash
    ./scripts/run_sandbox.sh --tail
    ```
    This starts the server in the background and immediately begins tailing the log file.

3.  **Start in the foreground:**
    ```bash
    ./scripts/run_sandbox.sh --foreground
    ```
    This will start the server in the foreground, printing all output directly to the console.

4.  **Stop the server:**
    ```bash
    ./scripts/stop_sandbox.sh
    ```
    This will stop the background server.

### Running Tests

Tests are run using `pytest`. You can run the full test suite with `coverage` to also measure code coverage.
...
You might need to run `npm ci` before running `npm run eslint` if you haven't installed the npm dependencies.

### New Relic Instrumentation

The project is instrumented with New Relic for performance monitoring. To enable it, you need to:

1.  **Set the license key:** Create a `.env` file in the root of the project and add your New Relic license key to it:
    ```
    NEW_RELIC_LICENSE_KEY=your_license_key
    ```
    The `run_sandbox.sh` script will automatically source this file.

2.  **Run with instrumentation:** Use the `run_sandbox.sh` script, which is pre-configured to launch the application with gunicorn and the New Relic agent.
    ```bash
    ./scripts/run_sandbox.sh
    ```
    This script will automatically set the `NEW_RELIC_CONFIG_FILE` environment variable and use `newrelic-admin run-program` to instrument the gunicorn server.

3.  **Configuration:** The New Relic configuration is in `newrelic.ini`.
