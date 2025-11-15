# camView
enigam2 plugin to display a camera

This project allows you to display a surveillance camera on an Enigma2 receiver. It provides an easy way to view live streams from IP cameras on your television. The display of the surveillance camera can also be triggered externally via REST API calls.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Prerequisites

- An Enigma2 receiver with an installed image (e.g., OpenATV, OpenPLI)
- Access to the network where the IP camera is located
- Basic knowledge of using SSH and the command line

## Installation

1. Copy the files to the Enigma2 receiver. You need to place the files in the following directory:
```code
/usr/lib/enigma2/python/Plugins/Extensions/camView
```
opkg install exteplayer3

## Usage
1. Start the Enigma2 receiver and open the plugin from the main menu.
2. Select the IP camera you want to display.
3. Click "Start Stream" to view the live stream.

## External Control via REST
The display of the surveillance camera can also be triggered externally via REST API calls. You can send an HTTP GET request to the endpoint /start_stream to start the stream. Example:

```bash
    curl http://<receiver-ip>/start_stream?camera_id=<your_camera_id>
```
## Configuration
The configuration of the IP camera is done in the config.ini file. Here you can adjust the IP address, port, and other settings of the camera.

```ini
[camera]
ip_address = 192.168.1.100
port = 8080
username = yourusername
password = yourpassword
```

## Troubleshooting
- No image displayed: Check the IP address and port of the camera. Ensure that the camera is reachable on the network.
- Connection error: Make sure the Enigma2 receiver is connected to the internet and that firewall settings are not blocking the connection.
## License
This project is licensed under the MIT License. See the LICENSE file for more information.