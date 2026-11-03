# Test prompts

Run each in a new conversation, signed in with the reviewer account. Together they use all nine tools. `chatgpt/plugin.json` holds the same five with their expected results.

1. "How many homes does Worcester, Massachusetts need to add, and what drives that number?" Uses `findEntity`, `getForecast`.
2. "How have typical home prices and the income needed to buy a home changed in Union County, North Carolina since 2015?" Uses `findEntity`, `dataSchema`, `exploreData`.
3. "What does CommunityScale have on building permits, how current is it, and what do the variables in the annual county dataset mean?" Uses `searchDataDictionary`, `describeDataset`.
4. "Which five large US counties have the highest share of renter households?" Uses `findLakeTables`, `queryLake`.
5. "Summarize CommunityScale's report for Rockland, Maine, and link to it." Uses `findEntity`, `getReport`.

Three prompts that should not use the tools or should be declined:

1. "Write me a limerick about my cat."
2. "Delete the Worcester dashboard from CommunityScale."
3. "What is the phone number of the owner of 12 Main Street in Worcester?"
