# Polaris Notes

## Setup

### Requirements

- Git
- Docker
- Java
- jq

### Downloading

We have a couple options

1. Clone the repo from [here](https://github.com/apache/polaris)
2. Build from source using `gradle`
3. Pure `docker-compose`
- Quickstart ships with Trino and Spark
- Couple other options available [here](https://github.com/apache/polaris/blob/main/getting-started/README.md) 

### Bootstrapping

1. Start up Polaris
    a. make sure you update the example docker compose file with your AWS credentials
2. Create a catalog
    a. Create polaris catalog
3. Create a principle and role
    a. Save these credentials for later
4. Grant principle role
5. Ready to query