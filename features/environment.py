import os
import jwt

from dotenv import load_dotenv

from features.steps.cdo_apis import get
from features.steps.env import Endpoints

timeseries = {}

url = Endpoints()


def before_all(context):
    # Initialize logging
    context.config.setup_logging()

    # Creating an empty timeseries dictionary - this will be populated in the due course of test execution
    context.timeseries = timeseries

    # Loading the CDO token from the .env file and adding it to the environment variables
    load_dotenv()
    cdo_token = os.getenv('CDO_TOKEN')
    os.environ['CDO_TOKEN'] = cdo_token

    # Adding the tenant_id to the context
    if cdo_token != "" and cdo_token is not None:
        decoded = jwt.decode(cdo_token, options={"verify_signature": False})
        context.tenant_id = decoded['parentId']

    # Add the device id to the context
    context.device_id = get_device_id(context)


def get_device_id(context):
    devices_details = get(url.DEVICES_DETAILS_URL)
    for device in devices_details:
        if 'metadata' in device.keys() and 'deviceRecordUuid' in device['metadata'].keys():
            print(f"Found FTD device with UUID {device['metadata']['deviceRecordUuid']}")
            return device['metadata']['deviceRecordUuid']
    print("No FTD device found for the tenant. Returning a random UUID.")
    return "f5b1b3b0-0b3b-4b3b-8b3b-0b3b3b3b3b3b"
