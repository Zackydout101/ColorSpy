# ColorSpy

More than just Red, Green, and Blue

ColorSpy is an app that lets you know the exact color your phone is seeing taking into consideration the different hues not just the plain of ROYGBV(Red Orange Yellow Gree Blue Violet)

- It leaverages the power of data science to take an image from the front end, finds the most dominant color in the frame of you allow the user to move their device as much they want with no need to zoom in.

## Setup

Run the following commands to install the dependencies

```bash
. ./install.sh
```

```
./run.sh

```
## Tech stack
Front-end:
    - Unity
    - Android studio
Back-end:
    - Python
    - Flask
    - Gunicorn
    - Sklearn
    - numpy

## challnages
- Finding maintained open source RSA libraries that work both for the front end and backend
- Data serialization
- Color detection using the available data and extrapolating from it to find the closest name to the color we are seeing



## Endpoints

|           | -      |                   |
| --------- | ------ | ----------------- |
| Endpoint  | Method | Description       |
| `/ `      | GET    | index             |
| `/key `   | GET    | get AES key       |
| `/image ` | POST   | send image to API |
