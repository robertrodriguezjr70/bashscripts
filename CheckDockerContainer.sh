#!/bin/bash
set -euo pipefail

FILE="dockerContainerStatus.txt"
TMP_FILE="$(mktemp)"

docker info | grep -i Stopped: | awk '{print $2}' > dockerContainerStatus.txt

while IFS= read -r line || [ -n "$line" ]; do
  # Trim spaces
  value="$(echo "$line" | xargs)"

  # If the line is a number greater than 0, write "error"
  if [[ "$value" =~ ^-?[0-9]+$ ]] && [ "$value" -gt 0 ]; then
    echo "error" >> "$TMP_FILE"
  else
    echo "$line" >> "$TMP_FILE"
  fi
done < "$FILE"

mv "$TMP_FILE" "$FILE"
