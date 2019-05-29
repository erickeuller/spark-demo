## Spark demo

Simple csv query using spark

### Usage

Copy the csv file to the ```./data``` folder and edit the ```./src/read_data.py``` script

### Requirements

- docker
- docker-compose

### Running 

#### Start spark

```sh
docker-compose up 
```

#### Running script

```sh
docker exec -it spark-demo_master_1 /usr/spark-2.4.1/bin/spark-submit /tmp/src/read_data.py
```
