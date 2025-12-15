#!/bin/bash
set -e

# --- Configuration ---
# Get the directory where the script is located, then resolve to project root
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

LOG_DIR="$PROJECT_ROOT/logs"
LOG_FILE="$LOG_DIR/sandbox.log"
PID_FILE="$LOG_DIR/sandbox.pid"
NEW_RELIC_CONFIG_PATH="$PROJECT_ROOT/newrelic.ini"

# --- Argument Parsing ---
FOREGROUND=false
TAIL_LOG=false
for arg in "$@"; do
  case $arg in
    -f|--foreground)
      FOREGROUND=true
      shift
      ;;
    -t|--tail)
      TAIL_LOG=true
      shift
      ;;
  esac
done

# --- Environment Setup ---
# Source .env file if it exists (from project root)
if [ -f "$PROJECT_ROOT/.env" ]; then
  set -a
  source "$PROJECT_ROOT/.env"
  set +a
fi

# Export environment variables for Gunicorn and New Relic
export NEW_RELIC_CONFIG_FILE="$NEW_RELIC_CONFIG_PATH"

# --- Main Logic ---
# Create logs directory if it doesn't exist
mkdir -p "$LOG_DIR"

echo "Changing directory to sandbox..."
cd "$PROJECT_ROOT/sandbox"

# Define the command to run the server
CMD="newrelic-admin run-program gunicorn --reload wsgi:application"

if [ "$FOREGROUND" = true ]; then
  echo "Starting sandbox server in foreground..."
  $CMD
else
  echo "Starting sandbox server in background..."
  $CMD > "$LOG_FILE" 2>&1 &

  # Save PID
  PID=$!
  echo $PID > "$PID_FILE"

  echo "Server started with PID $PID. Logs are in $LOG_FILE"

  if [ "$TAIL_LOG" = true ]; then
    echo "Tailing log file... (Press Ctrl+C to stop tailing)"
    tail -f "$LOG_FILE"
  fi
fi
