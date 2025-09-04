# Get the directory where the script is located
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Source the .env file from the script's directory
if [ -f "$SCRIPT_DIR/.env" ]; then
  set -a
  source "$SCRIPT_DIR/.env"
  set +a
fi

export CLIENT_ID=root
export CLIENT_SECRET=s3cr3t
export DEFAULT_BASE_LOCATION=${POLARIS_STORAGE_LOCATION}
export ROLE_ARN=${AWS_ROLE_ARN}

cd ./polaris

./polaris \
  --client-id ${CLIENT_ID} \
  --client-secret ${CLIENT_SECRET} \
  catalogs \
  create \
  --storage-type s3 \
  --default-base-location ${DEFAULT_BASE_LOCATION} \
  --role-arn ${ROLE_ARN} \
  ${POLARIS_WAREHOUSE}