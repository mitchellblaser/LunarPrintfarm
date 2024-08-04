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
