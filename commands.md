## Main commands

| Command                                  | Args                                                                                                                       | Description                                    | CHECK |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ----- |
| `--info`                                 | `<save-filename>`                                                                                                          | Show save file info                            | [x]   |
| `--to-json`                              | `<save-filename> <output-json-filename>`                                                                                   | Export save file to JSON                       | [x]   |
| `--from-json`                            | `<input-json-filename> <new-save-filename>`                                                                                | Create save file from JSON                     | [x]   |
| `--set-session-name`                     | `<new-session-name> <original-save-filename> <new-save-filename>`                                                          | Change session name in save file               | [x]   |
| `--find-free-stuff`                      | `[item] [save-filename]`                                                                                                   | Find free items in save file                   | [x]   |
| `--rotate-foundations`                   | `<primary-color-hex-or-preset> <secondary-color-hex-or-preset> <original-save-filename> <new-save-filename> [--same-time]` | Rotate foundation colors                       | [ ]   |
| `--clear-fog`                            | `<original-save-filename> <new-save-filename> [--same-time]`                                                               | Clear world fog of war                         | [ ]   |
| `--export-crash-sites`                   | `<save-filename> <output-json-filename>`                                                                                   | Export crash site data to JSON                 | [ ]   |
| `--resave-only`                          | `<original-save-filename> <new-save-filename>`                                                                             | Resave file without modifications              | [ ]   |
| `--add-missing-items-to-sav_stack_sizes` | —                                                                                                                          | Add missing items to internal stack size table | [ ]   |

## Player commands

| Command                        | Args                                                                                       | Description                          | CHECK |
| ------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------ | ----- |
| `--list-players`               | `<save-filename>`                                                                          | List all players in save file        | [x]   |
| `--list-player-inventory`      | `<player-num> <save-filename>`                                                             | Show inventory of selected player    | [x]   |
| `--export-player-inventory`    | `<player-num> <save-filename> <output-json-filename>`                                      | Export player inventory to JSON      | [x]   |
| `--import-player-inventory`    | `<player-num> <original-save-filename> <input-json-filename> <new-save-filename>`          | Import inventory from JSON into save | [ ]   |
| `--tweak-player-inventory`     | `<player-num> <slot-index> <item> <quantity> <original-save-filename> <new-save-filename>` | Modify single inventory slot         | [ ]   |
| `--export-hotbar`              | `<player-num> <save-filename> <output-json-filename>`                                      | Export player hotbar to JSON         | [ ]   |
| `--import-hotbar`              | `<player-num> <original-save-filename> <input-json-filename> <new-save-filename>`          | Import player hotbar from JSON       | [ ]   |
| `--change-num-inventory-slots` | `<num-inventory-slots> <original-save-filename> <new-save-filename>`                       | Change total inventory slots count   | [ ]   |

## Blueprint commands

| Command                            | Args                                                                                                                         | Description                                             | CHECK |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----- |
| `--blueprint --show`               | `<save-filename>`                                                                                                            | Show blueprint categories, subcategories and blueprints | [ ]   |
| `--blueprint --sort`               | `<original-save-filename> <new-save-filename>`                                                                               | Sort blueprints (categories → subcategories → names)    | [ ]   |
| `--blueprint --export`             | `<save-filename> <output-json-filename>`                                                                                     | Export blueprints to JSON                               | [ ]   |
| `--blueprint --import`             | `<original-save-filename> <input-json-filename> <new-save-filename>`                                                         | Import blueprints from JSON                             | [ ]   |
| `--blueprint --add-category`       | `<category> <original-save-filename> <new-save-filename>`                                                                    | Add new blueprint category                              | [ ]   |
| `--blueprint --add-subcategory`    | `<category> <subcategory> <original-save-filename> <new-save-filename>`                                                      | Add subcategory to category                             | [ ]   |
| `--blueprint --add-blueprint`      | `<category> <subcategory> <blueprint> <original-save-filename> <new-save-filename>`                                          | Add blueprint to subcategory                            | [ ]   |
| `--blueprint --remove-category`    | `<category> <original-save-filename> <new-save-filename>`                                                                    | Remove blueprint category                               | [ ]   |
| `--blueprint --remove-subcategory` | `<category> <subcategory> <original-save-filename> <new-save-filename>`                                                      | Remove subcategory from category                        | [ ]   |
| `--blueprint --remove-blueprint`   | `<category> <subcategory> <blueprint> <original-save-filename> <new-save-filename>`                                          | Remove blueprint                                        | [ ]   |
| `--blueprint --move-blueprint`     | `<old-category> <old-subcategory> <new-category> <new-subcategory> <blueprint> <original-save-filename> <new-save-filename>` | Move blueprint between categories                       | [ ]   |
| `--blueprint --reset`              | `<original-save-filename> <new-save-filename>`                                                                               | Reset blueprints to default state                       | [ ]   |

## Map markers

| Command                            | Args                                                                               | Description                        | CHECK |
| ---------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------- | ----- |
| `--list-map-markers`               | `<save-filename>`                                                                  | List all map markers in save file  | [x]   |
| `--add-map-markers-json`           | `<original-save-filename> <input-json-filename> <new-save-filename> [--same-time]` | Add map markers from JSON          | [x]   |
| `--add-map-markers-somersloops`    | `<original-save-filename> <new-save-filename> [--same-time]`                       | Add all Somersloops map markers    | [x]   |
| `--add-map-markers-mercer-spheres` | `<original-save-filename> <new-save-filename> [--same-time]`                       | Add all Mercer Spheres map markers | [x]   |
| `--add-map-markers-hard-drives`    | `<original-save-filename> <new-save-filename> [--same-time]`                       | Add all Hard Drives map markers    | [x]   |

## Somersloops

| Command                 | Args                                                                               | Description                                  | CHECK |
| ----------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------- | ----- |
| `--restore-somersloops` | `<original-save-filename> <new-save-filename> [--same-time]`                       | Restore all Somersloops to uncollected state | [ ]   |
| `--export-somersloops`  | `<save-filename> <output-json-filename>`                                           | Export Somersloops data to JSON              | [x]   |
| `--import-somersloops`  | `<original-save-filename> <input-json-filename> <new-save-filename> [--same-time]` | Import Somersloops data from JSON            | [ ]   |

## Mercer spheres

| Command                    | Args                                                                               | Description                                     | CHECK |
| -------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------- | ----- |
| `--export-mercer-spheres`  | `<save-filename> <output-json-filename>`                                           | Export Mercer Spheres data to JSON              | [ ]   |
| `--import-mercer-spheres`  | `<original-save-filename> <input-json-filename> <new-save-filename> [--same-time]` | Import Mercer Spheres data from JSON            | [ ]   |
| `--restore-mercer-spheres` | `<original-save-filename> <new-save-filename> [--same-time]`                       | Restore all Mercer Spheres to uncollected state | [ ]   |

## Vehicle paths

| Command                 | Args                                                                                           | Description                         | CHECK |
| ----------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------- | ----- |
| `--list-vehicle-paths`  | `<save-filename>`                                                                              | List all vehicle paths in save file | [ ]   |
| `--export-vehicle-path` | `<path-name> <save-filename> <output-json-filename>`                                           | Export vehicle path to JSON         | [ ]   |
| `--import-vehicle-path` | `<path-name> <original-save-filename> <input-json-filename> <new-save-filename> [--same-time]` | Import vehicle path from JSON       | [ ]   |

## Dimensional depot

| Command                       | Args                                                                                    | Description                                  | CHECK |
| ----------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------- | ----- |
| `--export-dimensional-depot`  | `<save-filename> <output-json-filename>`                                                | Export dimensional depot contents to JSON    | [ ]   |
| `--reorder-dimensional-depot` | `<original-save-filename> <input-json-filename> <new-save-filename> [--same-time]`      | Reorder dimensional depot items using JSON   | [ ]   |
| `--adjust-dimensional-depot`  | `<original-save-filename> <item-name> <new-quantity> <new-save-filename> [--same-time]` | Adjust quantity of item in dimensional depot | [ ]   |
