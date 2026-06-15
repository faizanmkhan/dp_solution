# System Monitor Tasks

## Task 1 — Simple System Monitor App

Create a simple Python app that monitors your system/server. Output should be written to a JSON file and stdout.

For monitoring, use the `psutil` module: https://pypi.org/project/psutil/

The app should create snapshots of the system state every 30 seconds (configurable):

```json
{"Tasks": {"total": 440, "running": 1, "sleeping": 354, "stopped": 1, "zombie": 0},
"%CPU": {"user": 14.4, "system": 2.2, "idle": 82.7},
"KiB Mem": {"total": 16280636, "free": 335140, "used": 11621308},
"KiB Swap": {"total": 16280636, "free": 335140, "used": 11621308},
"Timestamp": 1624400255}
```

Output should be written to both the console and a JSON file.

The script must accept an interval (default = 30 seconds) and an output file name via `argparse`: https://docs.python.org/3/library/argparse.html

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
parser.add_argument("-f", help="Output file name", default="snapshot.json")
parser.add_argument("-n", help="Quantity of snapshots to output", default=20)

args = parser.parse_args()
...
with open(args.f, "a") as file:
    # use json.dump to write JSON-snapshot to file
    # don't forget to import json before
    ...
```

**Additional requirements:**

- Use `os.system('clear')` and `print(snapshot, end="\r")` for console output.
- Use `time.sleep()` to implement the interval.
- Timestamp is the current Unix timestamp as an integer (no float part).
- Separate snapshots in the JSON file by a newline.
- Clear the file content when the script starts.
- ⚠️ At least one (any) class must be created.
- ⚠️ Do **not** use `pass` anywhere.

---

## Task 2 — Distributive Package

Create a distributable package from the script in Task 1.

The package should follow a structure similar to this example:

```
zoo-example
├── animals
│   ├── handlers
│   │   ├── __init__.py
│   │   ├── walk.py
│   │   └── swim.py
│   ├── __init__.py
│   ├── crocodile.py
│   ├── monkey.py
│   └── zoo.py
├── README.md
└── setup.py
```

**Requirements:**

- Add a `setup.py` file.
- The tool name must be `snapshot` (`name="snapshot"`).
- Add a `README.md` with a description of how to install and use the tool:
  https://docs.gitlab.com/ee/user/markdown.html
- Do **not** include any built distributions in the PR (no `*.whl`, `*.tar.gz`, `*.rpm`, etc.) — only the project source.

**Verify the package works:**

```bash
cd ..
snapshot-util$ pip install -U ./snapshot
snapshot-util$ snapshot -i 1
```