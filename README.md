# OBDServer

The OBD Server is a simple Flask app. It supplies an API on the '/stats' path which implements a POST and GET method.
To connect to the OBD Server, you'll need to make use of some sort of OBD Client. For an example, check out my other repo for a simple python script to run on a Raspberry Pi: https://github.com/jashenco/OBDClient.

This repo makes use of docker to make the application easy to implement. I've implemented an easy CI-CD using my Flask template repo: https://github.com/jashenco/FlaskApp-CI-CD-Template.
Follow the link to implement it yourself. When pushing to your OBD Server repo it will automatically update the site where you're hosting the Server.

Check out an example implementation on the following URL: http://89.99.4.132:8080/stats.
