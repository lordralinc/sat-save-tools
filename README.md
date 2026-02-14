# Satisfactory Save Tools


[![PyPI version](https://badge.fury.io/py/sat-save-tools.svg)](https://pypi.org/project/sat-save-tools/)
[![Python versions](https://img.shields.io/pypi/pyversions/sat-save-tools)](https://pypi.org/project/sat-save-tools/)
[![PyPI status](https://img.shields.io/pypi/status/sat-save-tools)](https://pypi.org/project/sat-save-tools/)
[![License](https://img.shields.io/pypi/l/sat-save-tools)](https://pypi.org/project/sat-save-tools/)
![Game](https://img.shields.io/badge/Game-Satisfactory-orange)

A collection of Python tools for parsing **Satisfactory** save files, as well as
displaying and manipulating their contents.

_[Satisfactory](https://www.satisfactorygame.com/) is a non-competitive,
first-person, open-world factory-building and exploration game developed by
[Coffee Stain Studios](https://www.coffeestain.com/)._

## Table of Contents

- **[Environment Variables](#environment-variables)**
- **[Command-Line Interface (CLI)](#command-line-interface-cli)**
- **[Using as a Library](#using-as-a-library)**
- **[Development & Architecture](#development--architecture)**
- **[Credits & Thanks](#credits--thanks)**
- **[License](#license)**

## Environment Variables

The library behavior can be controlled via environment variables:

- **`SF_LOGS_ENABLE_STRUCT_PATHS`** – Enable logging of full struct paths.
  Default: `0`

- **`SF_LOGS_ENABLE_OFFSET`** – Enable logging of byte offsets in structs.
  Default: `0`

- **`SF_PROGRESS_USE_RICH`** – Enable Rich-based progress bars.
  Default: `1`

- **`SF_PROGRESS_LOG_EVERY`** – Controls how often progress information is logged to the console.
  Effective only if `SF_PROGRESS_USE_RICH` is set to `0`.
  Default: `100`

- **`SF_DUMP_UNPARSED_SAVE`** – Dump unparsed save files for inspection.
  Default: `0`

- **`SF_DUMP_UNPARSED_SAVE_FOLDER`** – Directory where unparsed save files are stored (`pathlib.Path` is used internally).
  Default: `unparsed`

## Command-Line Interface (CLI)

- [`info`](#info)
- [`to-json`](#to-json)
- [`from-json`](#from-json)
- [`make-objects-tree`](#make-objects-tree)
- [`export-consts-data`](#export-consts-data)
- [`set-session-name`](#set-session-name)
- [`html`](#html)
- [`somersloops`](#somersloops)
  - [`somersloops export`](#somersloops-export)
- [`players`](#players)
  - [`players list`](#players-list)
  - [`players inventory`](#players-inventory)
    - [`players inventory show`](#players-inventory-show)
    - [`players inventory export`](#players-inventory-export)
    - [`players inventory import`](#players-inventory-import)
- [`map`](#map)
  - [`map markers`](#map-markers)
    - [`map markers show`](#map-markers-show)
    - [`map markers add`](#map-markers-add)
    - [`map markers export`](#map-markers-export)
    - [`map markers remove`](#map-markers-remove)
- [`find-free-stuff`](#find-free-stuff)
- [`gen-cli-docs`](#gen-cli-docs)

```bash
usage: sst [-h] [--log-level LOG_LEVEL] [--disable-logging] [--data-folder DATA_FOLDER] {info,to-json,from-json,make-objects-tree,export-consts-data,set-session-name,html,somersloops,players,map,find-free-stuff,gen-cli-docs} ...
```

**Arguments:**
- `--log-level`: Set log level [default: INFO]
- `--disable-logging`: Disable logging
- `--data-folder`: Path to static JSON data

### Subcommands
#### `info`
```bash
usage: sst info [-h] [--json] [--plain] save_path
```

**Arguments:**
- `save_path`: Path to the input save file
- `--json, -j`: Show as JSON
- `--plain, -p`: Disable indent and colors for JSON output

#### `to-json`
```bash
usage: sst to-json [-h] [--output OUTPUT] save_path
```

**Arguments:**
- `save_path`: Path to the input save file
- `--output, -o`: Path to the output save file

#### `from-json`
```bash
usage: sst from-json [-h] [--output OUTPUT] save_path
```

**Arguments:**
- `save_path`: Path to the input save file
- `--output, -o`: Path to the output save file

#### `make-objects-tree`
```bash
usage: sst make-objects-tree [-h] [--output OUTPUT] save_path
```

**Arguments:**
- `save_path`: Path to the input save file
- `--output, -o`: Path to the output file

#### `export-consts-data`
```bash
usage: sst export-consts-data [-h] foldername
```

**Arguments:**
- `foldername`: Path to the save folder

#### `set-session-name`
```bash
usage: sst set-session-name [-h] [--output OUTPUT] save_path session-name
```

**Arguments:**
- `save_path`: Path to the input save file
- `session-name`: Session name
- `--output, -o`: Path to the output save file

#### `html`
```bash
usage: sst html [-h] [--output OUTPUT] save_path
```

**Arguments:**
- `save_path`: Path to the input save file
- `--output, -o`: Path to output JSON file; if not set, saved in {input}.html

#### `somersloops`
```bash
usage: sst somersloops [-h] {export} ...
```

### Subcommands
#### `somersloops export`
```bash
usage: sst somersloops export [-h] [--output OUTPUT] save_path
```

**Arguments:**
- `save_path`: Path to the input save file
- `--output, -o`: Path to the output JSON file

#### `players`
```bash
usage: sst players [-h] {list,inventory} ...
```

### Subcommands
#### `players list`
```bash
usage: sst players list [-h] save_path
```

**Arguments:**
- `save_path`: Path to the input save file

#### `players inventory`
```bash
usage: sst players inventory [-h] {show,export,import} ...
```

### Subcommands
#### `players inventory show`
```bash
usage: sst players inventory show [-h] --player-id PLAYER_ID save_path
```

**Arguments:**
- `save_path`: Path to the input save file
- `--player-id`: Player ID to show inventory for (required)

#### `players inventory export`
```bash
usage: sst players inventory export [-h] --player-id PLAYER_ID [--output OUTPUT] save_path
```

**Arguments:**
- `save_path`: Path to the input save file
- `--player-id`: Player ID to export inventory (required)
- `--output, -o`: Output file

#### `players inventory import`
```bash
usage: sst players inventory import [-h] [--inventory-path INVENTORY_PATH] --player-id PLAYER_ID [--output OUTPUT] save_path
```

**Arguments:**
- `save_path`: Path to the input save file
- `--inventory-path, -i`: Path to the JSON file
- `--player-id`: Player ID to import inventory (required)
- `--output, -o`: Path to the output save file

#### `map`
```bash
usage: sst map [-h] {markers} ...
```

### Subcommands
#### `map markers`
```bash
usage: sst map markers [-h] {show,add,export,remove} ...
```

### Subcommands
#### `map markers show`
```bash
usage: sst map markers show [-h] filename
```

**Arguments:**
- `filename`: Path to the save file or JSON file to show map markers from

#### `map markers add`
```bash
Usage: sst map markers add [-h] --output OUTPUT [--recreate-ids] [--account-id ACCOUNT_ID] [--skip-len-check] [--src SRC] [--mode {add,replace,merge}] [--ms] [--ms-name MS_NAME] [--ms-compass-view-distance MS_COMPASS_VIEW_DISTANCE] [--ms-icon-id MS_ICON_ID] [--somersloops]
                           [--somersloops-name SOMERSLOOPS_NAME] [--somersloops-compass-view-distance SOMERSLOOPS_COMPASS_VIEW_DISTANCE] [--somersloops-icon-id SOMERSLOOPS_ICON_ID] [--hard-drives] [--hd-name HD_NAME] [--hd-compass-view-distance HD_COMPASS_VIEW_DISTANCE]
                           [--hd-icon-id HD_ICON_ID]
                           filename
```

**Arguments:**
- `filename`: Save file path
- `--output, -o`: Output save file path (required)
- `--recreate-ids`: Recreate marker IDs
- `--account-id`: Account ID (required for account-bound markers)
- `--skip-len-check`: Disable the marker limit check
- `--src`: Source JSON file with markers
- `--mode`: Import mode
- `--ms`: Add Mercer spheres
- `--ms-name`: Name of the Mercer sphere markers [default: Mercer Sphere]
- `--ms-compass-view-distance`: Compass view distance for Mercer spheres [default: ECompassViewDistance::CVD_Off]
- `--ms-icon-id`: Icon ID for Mercer spheres. See icon_ids.json. [default: 334]
- `--somersloops`: Add Somersloops
- `--somersloops-name`: Name of the Somersloop markers [default: Somersloop]
- `--somersloops-compass-view-distance`: Compass view distance for Somersloops [default: ECompassViewDistance::CVD_Off]
- `--somersloops-icon-id`: Icon ID for Somersloops. See icon_ids.json. [default: 329]
- `--hard-drives, -hd`: Add Hard Drives
- `--hd-name`: Name of the Hard Drive markers [default: Hard drive]
- `--hd-compass-view-distance`: Compass view distance for Hard Drives [default: ECompassViewDistance::CVD_Off]
- `--hd-icon-id`: Icon ID for Hard Drives. See icon_ids.json. [default: 652]

#### `map markers export`
```bash
usage: sst map markers export [-h] [-o OUTPUT] filename
```

**Arguments:**
- `filename`: Path to the save file to export map markers from
- `-o, --output`: Path to output the exported map markers to (defaults: {filename}.map_markers.json)

#### `map markers remove`
```bash
usage: sst map markers remove [-h] [-o OUTPUT] [--id MARKER_IDS] filename
```

**Arguments:**
- `filename`: Path to the save file
- `-o, --output`: Path to output
- `--id, -i`: Marker IDs [default: []]

#### `find-free-stuff`
```bash
usage: sst find-free-stuff [-h] [--save_path SAVE_PATH] [--item ITEM]
```

**Arguments:**
- `--save_path, -s`: Path to the save file
- `--item, -i`:

#### `gen-cli-docs`
```bash
usage: sst gen-cli-docs [-h] [--readme README]
```

**Arguments:**
- `--readme`: Path to README.md [default: README.md]

## Using as a Library

You can import the package and use its API directly in your code:

> This example demonstrates how to load a `.sav` file and export it to JSON.

```python
import pathlib

from sat_sav_parse import SatisfactorySaveFile


def convert_to_json(filename: pathlib.Path, output: pathlib.Path | None = None) -> None:
    output = output or filename.with_suffix(".json")
    save_content = SatisfactorySaveFile.load_from_file(filename)
    save_content.save_to_json(output)

convert_to_json(pathlib.Path("save.sav"), pathlib.Path("output.json"))

```

## Development & Architecture

The project is built with **Poetry** and targets **Python 3.13+**.

The codebase is structured in a modular and explicit way to keep responsibilities clearly separated:

```tree
.
│   const.py           # Project-wide constants
│   data.py            # Extracted game data (JSON)
│   env.py             # Environment configuration
│   exceptions.py      # Custom exception types
│   logger.py          # Logging setup
│   progress.py        # Progress bar utilities
│   utils.py           # Shared helper functions
│
├───serde              # Binary serialization / deserialization
├───actions            # Data transformation utilities
├───cli                # Command-line interface (parsers and commands)
└───models             # Data models (Pydantic / structured data)
```

The architecture is designed so that the CLI is a thin layer on top of the core library logic, allowing the package to be used both programmatically and from the command line without duplication.

## Credits & Thanks

Original project:
https://github.com/GreyHak/sat_sav_parse

This repository contains a major rewrite and modernization of the original
`sat_sav_parse` project.

The original author chose not to merge these changes into the upstream
repository and suggested maintaining them independently.

## License

This project is licensed under the **GNU General Public License v3.0**,
inherited from the original project.
