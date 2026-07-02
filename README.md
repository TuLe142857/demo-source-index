# Demo Tech Stack & Library - Graduation Thesis

This project is a workspace that manages independent demo modules for the technologies and libraries 
(tech stack/library) to be used in the graduation thesis. Each library or technology is integrated as a separate module.


## 1. Module Naming Conventions (Important)

To avoid conflicts with Python's Standard Library (e.g., `ast`, `test`, `json`, `sys`, `math`, ...), it is **MANDATORY** 
to prefix all module names with `demo_`:
- **Incorrect:** `ast`, `test`, `json`
- **Correct:** `demo_ast`, `demo_test`, `demo_json`


## 2. Process for Adding a New Demo

Run the following command (replace `<name>` with the demo module name; use `--package` if the demo provides CLI scripts):
```shell
uv init demo_<name> --package --vcs none
```
*This command will automatically initialize the `demo_<name>` directory and add this module to the `members` list in the [pyproject.toml](pyproject.toml) file at the root directory.*


## 3. Managing Demo Libraries

To install third-party libraries specifically for a single demo module without affecting other modules:
```shell
uv add --package demo_<name> <library_name>
```
*Example of installing `rich` for `demo_ast`:*
```shell
uv add --package demo_ast rich
```