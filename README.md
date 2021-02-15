![](https://travis-ci.com/punmister/klick_brick_cli.svg?token=JXew3bmbgspLsqYibfyf&branch=master)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# klick_brick_cli
A Command Line Interface Tool for the employees of KLICKBRICK to ease the onboarding process and utilities.

The Current version supports
* Greeting user

    ```klick_brick_cli "hello"```
* Onboarding checklist

    ```klick_brick_cli onboard```
* help

    ```klick_brick_cli --help```
* project initialization

    ```klick_brick_cli init```

#### Installation

You can dowload the wheel from dist folder and install the dependencies and package using pip as follows:

    pip install -r requirements.txt

    pip install klick_brick_cli-0.1.0-py3-none-any.whl

The project was made using very helpful tools like poetry and behave. "Behaviour Driven Development" and
"Test Driven Development" principles were used.

#### Testing
The project can be tested using the following command below
    behave
