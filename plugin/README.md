# CommunityScale

Ask Claude about housing in any US municipality or county and get figures with their sources. This plugin connects Claude to the data behind the CommunityScale dashboards and teaches it how to answer well: resolve the place first, use the fewest lookups, check what a table measures before ranking on it, and link every place and source.

## What it can answer

- Housing supply targets, cost burden by income group, affordability, income thresholds and population forecasts for a place
- Trends in home prices, income, wages, inflation, population and building permits
- Rankings and custom questions over Census tables, down to block groups
- What datasets exist on a topic, how current they are and what each variable means
- The published dashboard report for a place

## What it includes

- `skills/get-started`: guidance on using the tools and writing answers
- `.mcp.json`: the connection to `https://api.communityscale.io/mcp/v1`

## What it sends and stores

The plugin runs no local code and stores nothing on your computer. Tool calls go to the CommunityScale MCP server named above and to no other service. Every tool is read-only, so it cannot change your data or ours.

You sign in with a CommunityScale account the first time you connect. Create one at [app.communityscale.io/sign-up](https://app.communityscale.io/sign-up). The [privacy policy](https://communityscale.com/privacy-policy/) explains what the server records.

## Try it

- "How many homes does Worcester, Massachusetts need to add, and what drives that number?"
- "Which five large US counties have the highest share of renter households?"
- "What does CommunityScale have on building permits, and how current is it?"

Documentation: [docs.communityscale.io/docs/mcp](https://docs.communityscale.io/docs/mcp). Support: [communityscale.com/contact](https://communityscale.com/contact/).
