### Big Data Integration and processing course

#### Week 1

Installing the environment (use docker instead of Oracle VMBox)


- [cloudera/quickstart image](https://hub.docker.com/r/cloudera/quickstart)
- Type command ```docker pull cloudera/quickstart``` to get image of cloudera distribution

- Type command ```export EXPORT_VOLUME=$(pwd)```
- Type command ```docker run --hostname=quickstart.cloudera --privileged=true -t -i -p 7180:7180 -p 80:80 -p 8888:8888 -p 7187:7187 -v $EXPORT_VOLUME/:/data/ cloudera/quickstart /usr/bin/docker-quickstart``` to start docker container
- On `localhost:8888` you can find the `hue`-page. Use `cloudera` as username and password for access
  

 