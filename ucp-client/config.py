from ucp_client import PROFILE_PATH
import json
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("config")

def get_profile_data():
    with PROFILE_PATH.open(encoding="utf-8") as f:
        template = f.read()
    profile = json.loads(template)
    logger.info(f"Profile data: {profile}, type: {type(profile)}")
    version = profile.get("ucp").get("version")
    logger.info(f"version: {version}")
    capabilities = profile.get("ucp").get("capabilities")
    logger.info(f"Capabilities: {capabilities}; keys: {capabilities.keys()}; vals: {capabilities.values()}")
