#!/bin/bash

INPUT="$1"

# 1. Extract test suite name from line 1
testName=$(head -1 "$INPUT" | sed 's/\[ \(.*\) \],.*/\1/')

# 2. Extract and parse individual test lines
testsJson=""
first=true

while IFS= read -r line; do
  # Match lines starting with "ok" or "not ok"
  if echo "$line" | grep -qE "^(not ok|ok) "; then
    # Determine status
    if echo "$line" | grep -q "^not ok"; then
      status="false"
      remainder=$(echo "$line" | sed 's/^not ok *//')
    else
      status="true"
      remainder=$(echo "$line" | sed 's/^ok *//')
    fi

    # Strip the leading test number and any spaces after it
    remainder=$(echo "$remainder" | sed 's/^[0-9]* *//')

    # Duration is the last field after the final ", "
    duration=$(echo "$remainder" | awk -F', ' '{print $NF}')

    # Name is everything except the last ", duration" part
    name=$(echo "$remainder" | sed "s/, $duration$//")

    # Build the test JSON object
    testObj=$(printf '{"name": "%s", "status": %s, "duration": "%s"}' "$name" "$status" "$duration")

    if [ "$first" = true ]; then
      testsJson="$testObj"
      first=false
    else
      testsJson="$testsJson,
    $testObj"
    fi
  fi
done < "$INPUT"

# 3. Extract the summary line
summaryLine=$(grep "tests passed" "$INPUT")

# Parse success count (first number)
success=$(echo "$summaryLine" | awk '{print $1}')

# Parse failed count (number before "tests failed")
failed=$(echo "$summaryLine" | grep -oP '\d+(?= tests failed)')

# Parse rating (number before %)
rating=$(echo "$summaryLine" | grep -oP '[\d.]+(?=%)')

# Parse duration (last field)
duration=$(echo "$summaryLine" | awk '{print $NF}')

# 4. Write output.json
cat << EOF | ./jq '.' > output.json
{
  "testName": "$testName",
  "tests": [
    $testsJson
  ],
  "summary": {
    "success": $success,
    "failed": $failed,
    "rating": $rating,
    "duration": "$duration"
  }
}
EOF

echo "output.json generated successfully."