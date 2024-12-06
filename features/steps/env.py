import os

from dotenv import load_dotenv

_endpoints = None

class Path:
    BEHAVE_FEATURES_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                        os.pardir))
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(BEHAVE_FEATURES_ROOT)))
    PYTHON_UTILS_ROOT = os.path.join(PROJECT_ROOT, "python", "utils")


class Endpoints:
    def __init__(self):
        load_dotenv()
        self.BASE_URL = "https://edge.{}.cdo.cisco.com".format(os.getenv('ENV').lower())
        self.INSIGHTS_URL = self.BASE_URL + "/api/platform/ai-ops-insights/v1/insights"
        self.TENANT_ONBOARD_URL = self.BASE_URL + "/api/platform/ai-ops-orchestrator/v1/onboard/tenant"
        self.TENANT_GCM_STACK_CONFIG_URL = self.BASE_URL + "/api/platform/ai-ops-tenant-services/v1/timeseries-stack"
        self.PROMETHEUS_RANGE_QUERY_URL = self.BASE_URL + "/api/platform/ai-ops-data-query/v1/healthmetrics/queryRange"
        self.TRIGGER_MANAGER_URL = self.BASE_URL + "/api/platform/ai-ops-orchestrator/v1/trigger"
        self.FMC_DETAILS_URL = self.BASE_URL + "/aegis/rest/v1/services/targets/devices?q=deviceType:FMCE"
        self.DEVICES_DETAILS_URL = self.BASE_URL + "/aegis/rest/v1/services/targets/devices"
        self.DEVICE_GATEWAY_COMMAND_URL = self.BASE_URL + "/api/platform/device-gateway/command"


def get_endpoints():
    global _endpoints
    if _endpoints is None:
        _endpoints = Endpoints()
    return _endpoints