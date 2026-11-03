# Claude directory: plugin answers

Submit at [claude.ai/directory/manage](https://claude.ai/directory/manage): **Submit new**, then **Plugin bundle**. Submit this after the connector, from the same account, so the two can be paired.

## Before you start

Connect GitHub on claude.ai. While this repository is private, the portal also needs the Claude GitHub App installed on it and your agreement to upload the source for scanning. The repository must be public before the listing goes live.

## 1. Source

- Repository: `CommunityScale/communityscale-mcp-public`
- Plugin path: `plugin`
- Branch or tag: leave empty to follow `main`

Select **Validate** and fix anything marked **Blocking**.

## 2. Listing details

The portal reads these from `plugin/.claude-plugin/plugin.json` and `plugin/README.md`. Change them there and validate again.

## 3. Data handling

- Reads or stores personal data: the plugin does not. The connected server records what the privacy policy describes
- Sends data to services other than its declared connectors: no
- How long it keeps data: the plugin keeps none
- Intended for people under 18: no

## 4. Compliance

Check the contact email and accept the four acknowledgments.

## 5. Review and submit

Keep **GitHub push webhook**, turn on **Auto-publish passing versions**, and submit. Afterward, select **Set up push updates**, which needs admin access to the repository. A person reviews a new plugin, and a version that passes goes live when you select **Publish**.
