# Video Generation Agent

[![CI](https://github.com/kogunlowo123/video-generation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/video-generation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Marketing | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Video content generation agent that creates marketing videos from scripts, generates thumbnails, adds captions and B-roll, optimizes for platform requirements, and manages video assets.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_video` | Generate a marketing video from script and assets |
| `create_thumbnail` | Create an optimized video thumbnail |
| `add_captions` | Generate and add captions/subtitles to a video |
| `optimize_for_platform` | Optimize video specs for a specific platform |
| `manage_assets` | Manage video asset library and metadata |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/video-generation/create` | Create or generate |
| `POST` | `/api/v1/video-generation/analyze` | Analyze performance |
| `POST` | `/api/v1/video-generation/optimize` | Optimize |
| `POST` | `/api/v1/video-generation/schedule` | Schedule |
| `POST` | `/api/v1/video-generation/report` | Generate report |

## Features

- Video
- Generation
- Analytics
- Optimization

## Integrations

- Hubspot Marketing
- Marketo
- Mailchimp
- Google Analytics
- Meta Ads

## Architecture

```
video-generation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── video_generation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Marketing Platform + LLM + Analytics**

---

Built as part of the Enterprise AI Agent Platform.
