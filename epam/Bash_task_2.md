# DevOps Essentials: Final Task 2

Please use the branch `task2` that already exists in your forked repository after you have started the task.

## Bash Task 2

Company DEF has decided to use a testing tool for their employees. However, the current tool does not provide JSON output, which is required for further data processing and automation.

You have been asked to develop a Bash script that parses the test results and converts them into JSON format.

---

## Requirements

### 1. Parse `output.txt` and Convert It to `output.json`

### Example Input (`output.txt`)

```txt
[ Asserts Samples ], 1..2 tests
-----------------------------------------------------------------------------------
not ok 1 expecting command finishes successfully (bash way), 7ms
ok 2 expecting command prints some message (the same as above, bats way), 10ms
-----------------------------------------------------------------------------------
1 (of 2) tests passed, 1 tests failed, rated as 50%, spent 17ms
```

### Expected Output (`output.json`)

```json
{
  "testName": "Asserts Samples",
  "tests": [
    {
      "name": "expecting command finishes successfully (bash way)",
      "status": false,
      "duration": "7ms"
    },
    {
      "name": "expecting command prints some message (the same as above, bats way)",
      "status": true,
      "duration": "10ms"
    }
  ],
  "summary": {
    "success": 1,
    "failed": 1,
    "rating": 50,
    "duration": "17ms"
  }
}
```

---

### 2. Variable Number of Tests

The number of test cases is not fixed and may be greater than 2.

Your script must handle any number of test results present in the file.

---

### 3. Rating Format

The `rating` field must be stored as a numeric value.

The rating can be either:

- Integer (e.g. `50`, `100`)
- Floating-point number (e.g. `50.23`)

Examples:

```json
"rating": 50
```

```json
"rating": 50.23
```

---

### 4. Script Name

The script must be named:

```bash
task2.sh
```

---

### 5. Script Argument

The path to `output.txt` must be passed as an argument.

Example:

```bash
./task2.sh output.txt
```

---

## Additional Tools

If you need to use additional tools such as `jq`, you must use the executable provided in the repository:

```bash
./jq
```

You may also use any other tools explicitly allowed by the task requirements.

---

## Definition of Done

Develop a Bash script that:

- Reads and parses `output.txt`.
- Automatically generates `output.json`.
- Correctly extracts:
  - Test suite name
  - Test names
  - Test status (`true`/`false`)
  - Test duration
  - Summary statistics
- Supports any number of tests.
- Supports both integer and floating-point ratings.
- Produces JSON output matching the required structure.

---

## Reference
