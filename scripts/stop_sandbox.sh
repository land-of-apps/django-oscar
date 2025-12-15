#!/bin/bash

# Get the directory where the script is located, then resolve to project root
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

PID_FILE="$PROJECT_ROOT/logs/sandbox.pid"

if [ -f "$PID_FILE" ]; then
  PID=$(cat "$PID_FILE")
  echo "Stopping sandbox server with PID $PID"
  kill "$PID"
  rm "$PID_FILE"
else
  echo "PID file not found at $PID_FILE. Is the server running?"
fi