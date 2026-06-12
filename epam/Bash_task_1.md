# DevOps Essentials: Final Task 1

Please use the branch `task1` that already exists in your forked repository after you have started the task.

## Bash Task 1

Company ABC has an uncontrolled process for employee account creation. Currently, the process involves manually adding names, email addresses, and other personal data to the `accounts.csv` file without any naming conventions or validation rules.

The department head has decided to improve this process by implementing a standardized naming convention. While this is a good solution for new employees, the existing user list still needs to be updated.

You have been asked to help by developing an automated solution.

### Requirements

Create a Bash script that generates a new file named `accounts_new.csv` based on the existing `accounts.csv` file and the rules below.

#### 1. Update the Name Column

**Name format:**

- First letter of the first name and surname must be uppercase.
- All other letters must be lowercase.

**Examples:**

- `bart charlow` → `Bart Charlow`
- `CHRISTINA GONZALEZ` → `Christina Gonzalez`

#### 2. Update the Email Column

**Email domain:**

- All email addresses must use the domain `@abc.com`.

**Email format:**

- First letter of the first name + full surname.
- All characters must be lowercase.

**Examples:**

- `Christina Gonzalez` → `cgonzalez@abc.com`
- `Bart Charlow` → `bcharlow@abc.com`

If duplicate email usernames occur, append the `location_id` to make them unique.

**Examples:**

- `bcharlow6@abc.com`
- `bcharlow7@abc.com`

#### 3. Script Name

The script must be named:

```bash
task1.sh
```

#### 4. Script Argument

The path to `accounts.csv` must be passed as an argument.

**Example:**

```bash
./task1.sh accounts.csv
```

---

## Definition of Done

Develop a Bash script that:

- Automatically creates `accounts_new.csv`.
- Updates the **name** column according to the specified naming convention.
- Updates the **email** column according to the specified email convention.
- Does **not** use any additional installed packages.

---

## Example

### Input (`accounts.csv`)

```csv
2,1,Christina Gonzalez,Director,,
8,6,Bart charlow,Executive Director,,
9,7,Bart Charlow,Executive Director,,
```

### Output (`accounts_new.csv`)

```csv
2,1,Christina Gonzalez,Director,cgonzalez@abc.com,
8,6,Bart Charlow,Executive Director,bcharlow6@abc.com,
9,7,Bart Charlow,Executive Director,bcharlow7@abc.com,
```

---

## Reference