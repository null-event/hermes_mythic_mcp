# Mythic MCP

Mythic MCP is an MCP server that exposes Mythic C2 tasks to LLM clients for autonomous reconnaissance and operations. The included tools focus on macOS agent operations such as context enumeration, process/app listing, permissions checks, and file operations.

## Requirements

- `uv` and `python3`
- A reachable Mythic server and credentials
- An MCP client (e.g., Claude Desktop)

## Run Locally

Use `uv` to run the server with your Mythic credentials and endpoint:

```
uv --directory /full/path/to/mythic_mcp run main.py <username> <password> <host> <port>
```

Arguments come from `main.py` and are required to initialize the Mythic API client.

## Claude Desktop Configuration

Add the server to `claude_desktop_config.json`:

```
{
  "mcpServers": {
    "mythic_mcp": {
      "command": "/Users/<you>/.local/bin/uv",
      "args": [
        "--directory",
        "/full/path/to/mythic_mcp/",
        "run",
        "main.py",
        "<username>",
        "<password>",
        "<host>",
        "<port>"
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
- `read_file(agent_id, file_path)` — Read a file on the target via Mythic `cat`
- `run_shell_command(agent_id, command_line)` — Execute a shell command (`shell`)
- `upload_file(agent_id, file_name, remote_path, content)` — Upload a file (base64 content)
- `get_env(agent_id, command)` — Return environment variables for the session (`env`)
- `fda_check(agent_id, command)` — Check Full Disk Access TCC state
- `accessibility_check(agent_id, command)` — Check Accessibility (AX) permission state
- `get_execution_context(agent_id, command)` — Report execution context and bundle ID
- `ifconfig(agent_id, command)` — Enumerate IP addresses for the current session
- `list_apps(agent_id, command)` — List running GUI applications (`NSRunningApplication`)
- `list_processes(agent_id, command)` — Enumerate running processes (`ps`)
- `take_screenshot(agent_id, command)` — Capture screenshot (requires Screen Recording)
- `tcc_folder_checker(agent_id, command)` — Probe TCC-protected folders using mdquery
- `whoami(agent_id, command)` — Report current user context

Notes:
- Most tools expect an `agent_id` and a `command` string (often a simple label like `"env"` or `"ps"`).
- `tcc_folder_checker` requires an agent that supports this command and may fail without FDA.

## Typical Recon Workflow

1. `get_all_agents` — Identify active agent IDs
2. `whoami` and `get_execution_context` — Establish user and host application
3. `get_env` and `ifconfig` — Collect environment and network context
4. `list_processes` and `list_apps` — Inventory processes and applications
5. `fda_check`, `accessibility_check`, `tcc_folder_checker` — Verify TCC permissions and folder access

## Data Handling

Tool outputs are returned as plain text or JSON-like strings, wrapped in separators for easy parsing by MCP clients.

## Security

Operate within user consent and environment policy. TCC-protected locations (Desktop, Documents, Downloads) and UI automation require appropriate permissions (`Full Disk Access`, `Accessibility`, `Screen Recording`).
