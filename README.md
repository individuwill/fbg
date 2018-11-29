# FBG

# Usage

+ Obtain the proper username and password.
+ Install docker.
+ Download the [pages.json](https://github.com/individuwill/fbg/blob/master/app/pages.json) file and update it for your needs if needed.
+ Place the pages.json file on your server in the directory where you will run the docker command.

Run the following command

    docker run -d --name fbg --restart on-failure  -p 5001:80 -e username="test_user" -e password="test_password" -v $(pwd)/pages.json:/app/pages.json individuwill/fbg


Access the server now from your docker machine via the port mapped (5001 by default) https://your_server:5001/
