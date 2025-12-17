# Mythic MCP

This is an MCP server that exposes Hermes Mythic C2 tasks for autonomous reconnaissance and macOS red team operations. The included tools focus on macOS Hermes agent operations such as context enumeration, process/app listing, permissions checks, and file operations.

## Requirements

- `uv` and `python3`
- A reachable Mythic server and credentials
- An MCP client (e.g., TRAE, Claude Desktop, etc.)

## TRAE/Cursor/Claude/Etc. Configuration

```
{
  "mcpServers": {
    "hermes_mythic_mcp": {
      "command": "/Users/<you>/.local/bin/uv",
      "args": [
        "--directory",
        "/full/path/to/hermes_mythic_mcp/",
        "run",
        "main.py",
        "<mythic_admin>",
        "<mythic_password>",
        "<mythic_host>",
        "<mythic_port>"
      ]
    }
  }
}
```

## Prompts

- `start_pentest(threat_actor, objective)`
- `start_recon()`

These prompts seed the LLM with context and are defined in `main.py`.

## Available Tools

All tools are defined in `main.py` and call into Mythic via `lib/mythic_api.py`.

- `get_all_payloads` — List all payloads registered in Mythic
- `get_all_agents` — List currently active callbacks/agents
- `read_file(agent_id, file_path)` — Read a file on the target via Mythic API
- `run_shell_command(agent_id, command_line)` — Execute a shell command
- `upload_file(agent_id, file_name, remote_path, content)` — Upload a file (base64 content)
- `get_env(agent_id, command)` — Return environment variables for the session
- `fda_check(agent_id, command)` — Check Full Disk Access (FDA)
- `accessibility_check(agent_id, command)` — Use AXIsProcessTrusted() to determine Accessibility permission
- `get_execution_context(agent_id, command)` — Read environment variables to determine payload execution context
- `ifconfig(agent_id, command)` — Enumerate IP addresses information
- `list_apps(agent_id, command)` — List running applications with NSApplication.RunningApplications
- `list_processes(agent_id, command)` — Enumerate running processes
- `take_screenshot(agent_id, command)` — Capture screenshot (requires Screen Recording permissions)
- `tcc_folder_checker(agent_id, command)` — Probe TCC-protected folders using mdquery
- `whoami(agent_id, command)` — Report current user context

Notes:
- Most tools expect an `agent_id` and a `command` string (often a simple label like `"env"` or `"ps"`).

## Typical Recon Workflow

1. `get_all_agents` — Identify active agent IDs
2. `whoami` and `get_execution_context` — Establish user and host application
3. `get_env` and `ifconfig` — Collect environment and network context
4. `list_processes` and `list_apps` — Inventory processes and applications
5. `fda_check`, `accessibility_check`, `tcc_folder_checker` — Verify TCC permissions and folder access

## Data Handling

Tool outputs are returned as plain text or JSON-like strings, wrapped in separators for easy parsing by MCP clients.

## Acknowledgments

- [Preliminary POC for Mythic API integration via MCP server](https://github.com/xpn/mythic_mcp)
- [Hermes Mythic Agent](https://github.com/MythicAgents/hermes)
- [Mythic C2 Framework](https://github.com/its-a-feature/Mythic)
