# FBG

# Usage

+ Obtain the proper username and password.
+ Install docker.
+ Download the [pages.json](https://github.com/individuwill/fbg/blob/master/app/pages.json) file and update it for your needs if needed.
+ Place the pages.json file on your server in the directory where you will run the docker command.

Run the following command

    docker run -d --name fbg --restart on-failure  -p 5001:80 -e username="test_user" -e password="test_password" -v $(pwd)/pages.json:/app/pages.json individuwill/fbg


Access the server now from your docker machine via the port mapped (5001 by default) https://your_server:5001/

## Google Doc Setup

Use the `importhtml` formula function to retrieve the page.

A custom URL route has been added so that pages don't need to be defined in the docker container
deployment. The path is /custom/<class>/<url> .

The url should be encoded properly so it is not misinterpreted as part of the original url. Google
has a function for this named `encodeurl`.

The simplest way to accomplish this is to setup a cell containing the url that you want
and another cell with the class representing the table.

A1=datasmall
A2=https://subscribers.footballguys.com/myfbg/myviewstats.php?pos=qb&yr=2018&startwk=1&stopwk=17&profile=p

Then reference those cells in your importxml cell

A3=importhtml(CONCATENATE("http://my-docker-server/custom/", A1, "/", encodeurl(A2)), "table", 0)
