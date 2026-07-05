"""Video Generation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_video():
    """Test Generate a marketing video from script and assets."""
    tools = AgentTools()
    result = await tools.generate_video(script="test", style="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_create_thumbnail():
    """Test Create an optimized video thumbnail."""
    tools = AgentTools()
    result = await tools.create_thumbnail(video_id="test", title_text="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_add_captions():
    """Test Generate and add captions/subtitles to a video."""
    tools = AgentTools()
    result = await tools.add_captions(video_id="test", language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_for_platform():
    """Test Optimize video specs for a specific platform."""
    tools = AgentTools()
    result = await tools.optimize_for_platform(video_id="test", platform="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.video_generation_agent_agent import VideoGenerationAgentAgent
    agent = VideoGenerationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
