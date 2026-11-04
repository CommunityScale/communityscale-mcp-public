# Claude directory: MCP connector answers

Submit at [claude.ai/directory/manage](https://claude.ai/directory/manage): **Submit new**, then **MCP connector**. Submit this before the plugin.

## 1. Connection

- Server URL: `https://api.communityscale.io/mcp/v1`
- Users connect to different URLs: no

## 2. Tools

The portal reads these from the server. Expect nine read-only tools: `findEntity`, `getForecast`, `exploreData`, `dataSchema`, `getReport`, `findLakeTables`, `queryLake`, `searchDataDictionary`, `describeDataset`.

## 3. Listing

- Server name: `CommunityScale`
- One-liner: `US housing data, forecasts and a data dictionary for municipalities and counties.`
- Categories: the closest data or research options offered
- Documentation URL: `https://docs.communityscale.io/docs/mcp`
- Privacy policy URL: `https://communityscale.com/privacy-policy/`
- Icon: `plugin/assets/logo.png`
- URL slug: `communityscale`, which is permanent once published

Description:

```text
CommunityScale connects Claude to the housing data behind our community dashboards, so you can ask about any US municipality or county and get figures with their sources.

Ask about housing supply targets, cost burden by income group, affordability, income thresholds and population forecasts. Explore trends in home prices, income, wages, inflation, population and building permits. Run rankings and custom questions over Census tables, down to block groups. Read the published dashboard report for a place.

A data dictionary is built in: search for the datasets we hold on a topic, see how current each one is, and read the definition and unit of every variable.

The connection is read-only. It needs a CommunityScale account, and it never changes your data or ours.
```

## 4. Use cases

- Primary use cases: answering housing questions about a US place; checking housing supply targets and cost burden; tracking trends in prices, income and permits; ranking places on Census measures; finding and understanding datasets in the data dictionary
- What users need first: a CommunityScale account, created at `https://app.communityscale.io/sign-up`
- Reads or writes: reads data only

## 5. Company

- Company name: `CommunityScale LLC`
- Website: `https://communityscale.com`

## 6. Authentication

- Authentication requirement: **Always required**
- Authentication method: OAuth sign-in. Claude identifies itself with its client ID metadata document, and dynamic client registration also works, so no client ID or secret is entered

## 7. Data handling

- Underlying API: our own
- Personal health data: no
- Sponsored content: no

## 8. Test and launch

Enter the login in the portal's credential fields if it offers them, and leave it out of the text below. Then add:

```text
Connect to https://api.communityscale.io/mcp/v1 and choose sign in when prompted.
Every account can read all of the data, so this one needs no setup or sample data.
Use the five prompts in the repository's submission/test-prompts.md; together they run all nine tools.
```

Confirm you ran every tool only after doing so.

## 9. Compliance

Seven acknowledgments, accepted by the person submitting. The connector makes no financial transactions and generates no AI media.

## 10. Review and submit

Fix any quality warnings, then submit.
