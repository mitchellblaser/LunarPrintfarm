# Lunar Printfarm

A Print Farm Queueing and Distribution Manager for 3D Printers running Klipper and Moonraker.

## Screenshots

![Print Queue Page](/readme/screenshot01.png?raw=true)

## Getting Started

### Dependencies

* We depend on a couple of Python 3 libraries - all of which can be installed via requirements.txt.
* Additionally, the web GUI uses UIKit. A release of this is pre-included in the src/app/static/js and src/app/static/css.

### Installing

* Clone repository from GitHub.
* Install requirements with `python -m pip install -r ./requirements.txt`
* Run `flask --app ./src/lunar.py --debug run`
* Navigate to `localhost:5000`

## Features

* Quick and simple monitoring of many OctoPrint and Klipper printers
* Uploading G-Code Files to printers remotely from Web UI
* Assignable Tags for each printer to mark colors, materials and zones

## Future Roadmap

* Bulk G-Code Uploading, with Filter options referencing Tags for each printer
* A per-printer queue, with Auto Print Ejection in between each job
* A "Print Repeat" button for each printer, which allows for continuous printing.
* GUI Configuration, rather than manually editing the Configuration file.

## Authors

Mitchell Blaser

## Version History

* Development
    * The project is not yet ready for use, a release will be created on GitHub once it's ready for you :)

## License

It's open source (obviously). Haven't made a license.txt file yet because I've got more important things to do - I'll get around to that at some point

## Acknowledgments

Libraries we're using - thanks :)
* [flask](https://github.com/pallets/flask)
* [UIKit](https://github.com/uikit/uikit)
