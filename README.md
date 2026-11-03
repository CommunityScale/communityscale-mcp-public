# CommunityScale for Claude and ChatGPT

The plugins and directory materials for CommunityScale's MCP server at `https://api.communityscale.io/mcp/v1`: a Claude plugin, a ChatGPT plugin package, and the answers each directory asks for. The server's code lives in CommunityScale's application repository, so this repository holds no server code and no credentials.

The server gives AI assistants read-only access to US housing and demographic data, forecasts, dashboard reports, Census tables and a data dictionary. Users sign in with a CommunityScale account.

## Documentation

The setup guide and tool reference are at [docs.communityscale.io/docs/mcp](https://docs.communityscale.io/docs/mcp). It links back here. The two describe the same server, so when a tool changes, update the guide's tool table, the skill in `plugin/skills/`, and the test prompts in `submission/` and `chatgpt/plugin.json` together.

## What is here

| Path | Use |
|---|---|
| `plugin/` | The Claude plugin: manifest, MCP connection, skill, logo, README and license |
| `.claude-plugin/marketplace.json` | Lets Claude Code install the plugin from this repository |
| `chatgpt/` | The ChatGPT plugin manifest with its test cases, its MCP configuration and the ZIP builder. It reuses the skill and logo in `plugin/` |
| `submission/` | Paste-ready answers for each directory, the test prompts and the privacy policy addition |

## Install in Claude Code

```text
/plugin marketplace add CommunityScale/communityscale-mcp-public
/plugin install communityscale@communityscale
```

## Validate and build

```bash
claude plugin validate ./plugin
python chatgpt/build_zip.py https://YOUR-DEMO-VIDEO-LINK
```

The ZIP lands in `dist/`, which is not committed.

## Keeping it current

The skill and the server's instructions teach the same habits, so change both together, along with the guide at docs.communityscale.io/docs/mcp. Raise `version` in `plugin/.claude-plugin/plugin.json` and `chatgpt/plugin.json` with every release.
