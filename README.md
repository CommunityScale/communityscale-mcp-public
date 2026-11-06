# CommunityScale MCP

Connect your AI assistant to US housing data. CommunityScale's [Model Context Protocol](https://modelcontextprotocol.io) server gives Claude, ChatGPT, OpenCode, Hermes Agent and any other MCP client read-only access to the data behind our community dashboards: housing supply targets, cost burden, affordability, population forecasts, Census tables down to block groups, and a data dictionary that explains every variable.

| Setting | Value |
|---|---|
| URL | `https://api.communityscale.io/mcp/v1` |
| Transport | Streamable HTTP |
| Sign-in | OAuth with a CommunityScale account. Your client opens the sign-in page, and dynamic client registration means there is no client ID or secret to enter |
| Access | Read-only |
| Rate limit | 120 requests per minute per signed-in connection |

You need a CommunityScale account. Create one at [app.communityscale.io/sign-up](https://app.communityscale.io/sign-up), or from the sign-in page the first time you connect.

## Connect

### Claude (web and desktop)

[claude.ai/directory/communityscale](https://claude.ai/directory/communityscale)

### Claude Code

If you sign in to Claude Code with your Claude account, a connector you added in Claude is already available; run `/mcp` to see it. Or install the plugin, which adds the connection and a skill that teaches Claude how to answer with this data:

```text
/plugin marketplace add CommunityScale/communityscale-mcp-public
/plugin install communityscale@communityscale
```

To add only the connection:

```bash
claude mcp add --transport http communityscale https://api.communityscale.io/mcp/v1
```

Then run `/mcp` in Claude Code and sign in.

### ChatGPT

1. Open [chatgpt.com/plugins](https://chatgpt.com/plugins), select the plus button, then **Add custom MCP server**.
2. Name it `CommunityScale`, paste `https://api.communityscale.io/mcp/v1` as the URL and choose OAuth.
3. Select **Create as a plugin** and sign in.

Your plan and workspace settings decide whether you can add a custom MCP server.

### OpenCode

Add the server to `opencode.json` in your project, or to `~/.config/opencode/opencode.json` for every project:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "communityscale": {
      "type": "remote",
      "url": "https://api.communityscale.io/mcp/v1"
    }
  }
}
```

OpenCode asks you to sign in the first time it uses the server. To sign in right away:

```bash
opencode mcp auth communityscale
```

### Hermes Agent

```bash
hermes mcp add --url https://api.communityscale.io/mcp/v1 --auth oauth communityscale
hermes mcp test communityscale
```

Hermes opens your browser to sign in and keeps the token under `~/.hermes/mcp-tokens/`. In a running session, run `/reload-mcp` to load the tools. On a remote or SSH host, forward the sign-in callback's loopback port to your machine.

### Codex CLI

```bash
codex mcp add communityscale --url https://api.communityscale.io/mcp/v1
codex mcp login communityscale
```

### Gemini CLI

```bash
gemini mcp add --transport http communityscale https://api.communityscale.io/mcp/v1
```

Then run `/mcp auth communityscale` in Gemini CLI to sign in.

### Cursor

Add to `~/.cursor/mcp.json`, or `.cursor/mcp.json` in a project:

```json
{
  "mcpServers": {
    "communityscale": {
      "url": "https://api.communityscale.io/mcp/v1"
    }
  }
}
```

Cursor shows a sign-in button for the server under Settings, MCP.

### VS Code (GitHub Copilot agent mode)

Add to `.vscode/mcp.json` in a workspace, or run **MCP: Add Server** from the command palette:

```json
{
  "servers": {
    "communityscale": {
      "type": "http",
      "url": "https://api.communityscale.io/mcp/v1"
    }
  }
}
```

VS Code prompts you to sign in when the server starts.

### Other clients and your own agent

Any client that speaks MCP over Streamable HTTP with OAuth can connect with the URL alone. The server publishes its OAuth details at `https://api.communityscale.io/.well-known/oauth-protected-resource/mcp/v1`, and the sign-in service supports dynamic client registration and client ID metadata documents, so a client registers itself.

A client that only runs local (stdio) servers can reach it through [`mcp-remote`](https://www.npmjs.com/package/mcp-remote):

```json
{
  "mcpServers": {
    "communityscale": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://api.communityscale.io/mcp/v1"]
    }
  }
}
```

The Claude API and the OpenAI Responses API also accept remote MCP servers by URL, given an access token from the same OAuth flow.

## Add the skill to other agents

[`plugin/skills/get-started/SKILL.md`](plugin/skills/get-started/SKILL.md) teaches an assistant to answer well with these tools: resolve the place first, use the fewest calls, check what a table measures before ranking on it, and link every place and source. Claude Code gets it from the plugin, and ChatGPT from the plugin package. It follows the [Agent Skills](https://agentskills.io) format, so other agents can load it too. Copy the `get-started` folder, keeping its name:

| Agent | Skills folder |
|---|---|
| OpenCode, and other agents that read the shared folder | `~/.agents/skills/` |
| Hermes Agent | `~/.hermes/skills/`, or add `~/.agents/skills` under `skills.external_dirs` in `~/.hermes/config.yaml` |
| Claude Code, without the plugin | `~/.claude/skills/` |

```bash
git clone https://github.com/CommunityScale/communityscale-mcp-public
mkdir -p ~/.agents/skills
cp -R communityscale-mcp-public/plugin/skills/get-started ~/.agents/skills/
```

An agent without skill support works without it: the server also sends its own instructions, metric definitions and data cautions when a client connects.

## Tools

| Tool | What it does |
|---|---|
| `findEntity` | Resolves a place name or FIPS code to a municipality or county, with its dashboard link and the keys the other tools take |
| `getForecast` | Dashboard figures for a place: housing supply targets, cost burden by income group, affordability, income thresholds and population forecasts |
| `exploreData` | Trends and custom breakdowns: income, home prices, wages, inflation, population, building permits, HUD income limits and survey-weighted ACS microdata |
| `dataSchema` | The fields `exploreData` accepts for a source, with its publisher, license and latest vintage |
| `findLakeTables` | Finds tables to query by a word in their name, columns or description |
| `queryLake` | Read-only SQL over the data lake, such as ACS at any geography down to block groups, with joins |
| `searchDataDictionary` | Finds datasets on a topic and the tool that can query each one, optionally with their variables |
| `describeDataset` | The variables of one dataset, with each one's definition and unit |
| `getReport` | The published dashboard report for a municipality or county, as Markdown |

Every tool is read-only. The full reference is at [docs.communityscale.io/docs/mcp](https://docs.communityscale.io/docs/mcp).

## Try it

- "What share of renter households in Worcester, Massachusetts spend more than half their income on housing?"
- "How many homes does Rockland, Maine need to add by its target year, and what drives that number?"
- "Which five large US counties have the highest share of renter households?"
- "What does CommunityScale have on building permits, and how current is it?"

## Privacy

For each request the server records your IP address, a one-way fingerprint of your sign-in token, which tool ran, whether it succeeded and how long it took. It does not record your prompts, your conversations, the arguments a tool received or the results it returned. See the [privacy policy](https://communityscale.com/privacy-policy/).

## What is in this repository

The server's code lives in CommunityScale's application repository. This one holds the client side: no server code and no credentials.

| Path | Use |
|---|---|
| `plugin/` | The Claude plugin: manifest, MCP connection, skill, logo, README and license |
| `.claude-plugin/marketplace.json` | Lets Claude Code install the plugin from this repository |
| `chatgpt/` | The ChatGPT plugin manifest with its test cases, its MCP configuration and the ZIP builder. It reuses the skill and logo in `plugin/` |
| `submission/` | Answers for each directory listing, the test prompts and the privacy policy text |

### Validate and build

```bash
claude plugin validate ./plugin
python chatgpt/build_zip.py https://YOUR-DEMO-VIDEO-LINK
```

The ZIP lands in `dist/`, which is not committed.

### Keeping it current

This README, the guide at [docs.communityscale.io/docs/mcp](https://docs.communityscale.io/docs/mcp), the skill in `plugin/skills/`, and the test prompts in `submission/` and `chatgpt/plugin.json` describe the same server, so change them together when a tool changes. The skill and the server's own instructions teach the same habits. Raise `version` in `plugin/.claude-plugin/plugin.json` and `chatgpt/plugin.json` with every release.

## Support

[communityscale.com/contact](https://communityscale.com/contact/)
