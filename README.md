# PennApps #

To run findText.py

Step 1: Turn on the Google Slides API

* Create or select a project in the [Google Developers Console](https://console.developers.google.com/flows/enableapi?apiid=slides.googleapis.com) and automatically turn on the API. Click `Continue`, followed by `Go to credentials`.
* On the `Add credentials to your project` page, click the `Cancel` button located at the bottom of the page
* Select the `OAth consent screen` tab located at the top of the new page. Enter your Email address, Product name if not already set, and click the `Save` button.
* Back on the Credentials tab, select `OAuth client ID` from the list of credentials. Select the application type `Other`, enter the name "Google Slides API Quickstart", and click the `Create` button.
* Click OK to dismiss the resulting dialog.
* Download the generated file and move it to your working directory and rename it client_secret.json.

Step 2: Install the Google Client Library

Run the following command to install the library using pip:

pip install --upgrade google-api-python-client
