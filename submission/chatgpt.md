# ChatGPT directory: plugin answers

## Prepare

- Submit from the CommunityScale organization on the OpenAI Platform, after business verification. Copy the developer name exactly as it appears under **Verifications**.
- The submitter must be an Owner or hold **Apps Management: Write**.
- Record a demo of the five prompts in `test-prompts.md`, hosted where reviewers can open it without signing in.

## Build

```bash
python chatgpt/build_zip.py https://YOUR-DEMO-VIDEO-LINK
```

## Submit

1. In the Plugins dashboard, select **Upload new or existing plugin**, choose the verified identity and upload `dist/communityscale-chatgpt-plugin.zip`. If `Research` is rejected as the category, choose the closest one offered.
2. Under **MCPs**, select **Connect**. If validation rejects the `extensions` block in `chatgpt/mcp.json`, remove it and rebuild.
3. Complete domain verification with the token OpenAI provides.
4. Authorize with the reviewer account.
5. Enter the reviewer login, URL and sign-in steps under **Review details**, never in this repository.
6. Select **Submit for review**, complete the attestations, and choose **Publish plugin** after approval.
