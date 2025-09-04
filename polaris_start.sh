# Get the directory where the script is located
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Source the .env file from the script's directory
if [ -f "$SCRIPT_DIR/.env" ]; then
  set -a
  source "$SCRIPT_DIR/.env"
  set +a
fi

cd ./polaris/

export ASSETS_PATH=$(pwd)/getting-started/assets/
export QUARKUS_DATASOURCE_JDBC_URL=jdbc:postgresql://postgres:5432/POLARIS
export QUARKUS_DATASOURCE_USERNAME=postgres
export QUARKUS_DATASOURCE_PASSWORD=postgres
export CLIENT_ID=root
export CLIENT_SECRET=s3cr3t
export STORAGE_LOCATION=$(POLARIS_STORAGE_LOCATION)


docker compose -p polaris -f getting-started/assets/postgres/docker-compose-postgres.yml \
  -f getting-started/jdbc/docker-compose-bootstrap-db.yml \
  -f getting-started/jdbc/docker-compose.yml up -d