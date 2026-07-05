"""Test configuration for Video Generation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "video-generation-agent", "category": "Marketing"}
