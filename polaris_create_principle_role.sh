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

cd ./polaris

./polaris \
  --client-id ${CLIENT_ID} \
  --client-secret ${CLIENT_SECRET} \
  principal-roles \
  grant \
  --principal quickstart_user \
  quickstart_user_role

./polaris \
  --client-id ${CLIENT_ID} \
  --client-secret ${CLIENT_SECRET} \
  catalog-roles \
  grant \
  --catalog ${POLARIS_WAREHOUSE} \
  --principal-role quickstart_user_role \
  quickstart_catalog_role