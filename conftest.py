import json
import pytest
from core.api_client import APIClient
from core.validator import Validator
from core.ai_engine import AITestEngine
from core.utils import print_framework_header

@pytest.fixture(scope="session", autouse=True)
def show_author_info():
    print_framework_header()

@pytest.fixture(scope="session")
def config():
    with open("configs/config.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def setup_components(config):
    api_client = APIClient()
    validator = Validator()
    ai_engine = AITestEngine(config["openai_api_key"])
    return api_client, validator, ai_engine
