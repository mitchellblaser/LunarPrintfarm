# Lunar Printfarm

A Print Farm Queueing and Distribution Manager for 3D Printers running Klipper and Moonraker.

## Getting Started

### Dependencies

* We depend on a couple of Python 3 libraries - all of which can be found in requirements.txt.
* Additionally, the web GUI uses UIKit. A release of this is pre-included in the src/app/static/js and src/app/static/css.

### Installing

* Clone down from GitHub.
* MacOS/Linux Users: Run chmod +x lunar.sh && ./lunar.sh
* Windows Users: lunar.bat

### Executing program

* Run either ./lunar.sh or ./lunar.bat depending on your OS
* The Flask server will start a webserver on localhost:5000, so navigate to there in the web browser.

## Authors

Mitchell Blaser
[@mblaser_](https://twitter.com/mblaser_)

## Version History

* Development
    * The project is not yet ready for use, a release will be created on GitHub once it's ready for you :)

## License

It's open source. Haven't made a license.txt file yet because I've got more important things to do - I'll get around to that at some point

## Acknowledgments

Libraries we're using - thanks :)
* [flask](https://github.com/pallets/flask)
* [UIKit](https://github.com/uikit/uikit)
* [Moonraker](https://github.com/Arksine/moonraker)