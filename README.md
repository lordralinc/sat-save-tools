# Satisfactory Save Tools

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
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
- [`export-consts-data`](#export-consts-data)
- [`set-session-name`](#set-session-name)
- [`players`](#players)
  - [`players list`](#players-list)
  - [`players inventory`](#players-inventory)
    - [`players inventory show`](#players-inventory-show)
    - [`players inventory export`](#players-inventory-export)
- [`map`](#map)
  - [`map markers`](#map-markers)
    - [`map markers show`](#map-markers-show)
    - [`map markers add`](#map-markers-add)
    - [`map markers export`](#map-markers-export)
    - [`map markers remove`](#map-markers-remove)
- [`find-free-stuff`](#find-free-stuff)
- [`gen-cli-docs`](#gen-cli-docs)

```bash
usage: python.exe -m sat_save_tools [-h] [--log-level LOG_LEVEL] [--disable-logging] [--data-folder DATA_FOLDER] {info,to-json,from-json,export-consts-data,set-session-name,players,map,find-free-stuff,gen-cli-docs} ...
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `--log-level`: Set log level [default: INFO]
- `--disable-logging`: Disable logging
- `--data-folder`: Path to static JSON data

### Subcommands
#### `info`
```bash
usage: python.exe -m sat_save_tools info [-h] [--json] [--plain] filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the save file
- `--json, -j`: Show as JSON
- `--plain, -p`: Disable indent and colors for JSON output

#### `to-json`
```bash
usage: python.exe -m sat_save_tools to-json [-h] [--output OUTPUT] filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the save file
- `--output, -o`: Path to output JSON file; if not set, saved in {input}.json

#### `from-json`
```bash
usage: python.exe -m sat_save_tools from-json [-h] [--output OUTPUT] filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the JSON file
- `--output, -o`: Path to output sav file; if not set, saved in {input}.sav

#### `export-consts-data`
```bash
usage: python.exe -m sat_save_tools export-consts-data [-h] foldername
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `foldername`: Path to the save file

#### `set-session-name`
```bash
usage: python.exe -m sat_save_tools set-session-name [-h] [--output OUTPUT] filename session-name
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the JSON file
- `session-name`: Session name
- `--output, -o`: Path to output JSON file; if not set, saved in {filename}.json

#### `players`
```bash
usage: python.exe -m sat_save_tools players [-h] {list,inventory} ...
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]

### Subcommands
#### `players list`
```bash
usage: python.exe -m sat_save_tools players list [-h] filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the JSON file

#### `players inventory`
```bash
usage: python.exe -m sat_save_tools players inventory [-h] {show,export} ...
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]

### Subcommands
#### `players inventory show`
```bash
usage: python.exe -m sat_save_tools players inventory show [-h] --player-id PLAYER_ID filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the JSON file
- `--player-id`: Player ID to show inventory for (required)

#### `players inventory export`
```bash
usage: python.exe -m sat_save_tools players inventory export [-h] --player-id PLAYER_ID [--output OUTPUT] filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the JSON file
- `--player-id`: Player ID to export inventory (required)
- `--output, -o`: Player ID to export inventory

#### `map`
```bash
usage: python.exe -m sat_save_tools map [-h] {markers} ...
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]

### Subcommands
#### `map markers`
```bash
usage: python.exe -m sat_save_tools map markers [-h] {show,add,export,remove} ...
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]

### Subcommands
#### `map markers show`
```bash
usage: python.exe -m sat_save_tools map markers show [-h] filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the save file or JSON file to show map markers from

#### `map markers add`
```bash
Usage: python.exe -m sat_save_tools map markers add [-h] --output OUTPUT [--recreate-ids] [--account-id ACCOUNT_ID] [--skip-len-check] [--src SRC] [--mode {add,replace,merge}] [--ms] [--ms-name MS_NAME] [--ms-compass-view-distance MS_COMPASS_VIEW_DISTANCE] [--ms-icon-id MS_ICON_ID] [--somersloops]
                                                    [--somersloops-name SOMERSLOOPS_NAME] [--somersloops-compass-view-distance SOMERSLOOPS_COMPASS_VIEW_DISTANCE] [--somersloops-icon-id SOMERSLOOPS_ICON_ID] [--hard-drives] [--hd-name HD_NAME] [--hd-compass-view-distance HD_COMPASS_VIEW_DISTANCE] [--hd-icon-id HD_ICON_ID]
                                                    filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
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
usage: python.exe -m sat_save_tools map markers export [-h] [-o OUTPUT] filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the save file to export map markers from
- `-o, --output`: Path to output the exported map markers to (defaults: {filename}.map_markers.json)

#### `map markers remove`
```bash
usage: python.exe -m sat_save_tools map markers remove [-h] [-o OUTPUT] [--id MARKER_IDS] filename
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `filename`: Path to the save file
- `-o, --output`: Path to output
- `--id, -i`: Marker IDs [default: []]

#### `find-free-stuff`
```bash
usage: python.exe -m sat_save_tools find-free-stuff [-h] [--filename FILENAME] [--item ITEM]
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
- `--filename, -f`: Path to the save file
- `--item, -i`:

#### `gen-cli-docs`
```bash
usage: python.exe -m sat_save_tools gen-cli-docs [-h] [--readme README]
```

**Arguments:**
- `-h, --help`: show this help message and exit [default: ==SUPPRESS==]
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
