---
name: get-started
description: Answer questions about housing, population, affordability and economic conditions in US communities with CommunityScale data. Use for a place, county or national housing question, a ranking of places, or what a housing dataset or variable means.
---

# Answer housing questions with CommunityScale

CommunityScale publishes housing and demographic data for US municipalities and counties, and Census tables down to block groups.

## Choose the tool

- `findEntity` turns a place name into a municipality or county geoid. Use it for the geoid and `geo_keys` that `exploreData` filters take, and when a name could match more than one place. Never guess a filter value.
- `getForecast` gives a place's current dashboard figures: housing supply targets, cost burden by income group, affordability, income thresholds and population forecasts. It takes the place name with its state (`place`, such as "Worcester, MA") as well as a geoid, so a question about one place needs no `findEntity` call; check the `place` it returns is the one meant.
- `exploreData` gives trends and breakdowns from curated sources. Call `dataSchema` once per source first, unless the tool description lists the fields (as it does for `housing_affordability`), ask only for the measures you need, and filter to the place and years in the question.
- `findLakeTables` and `queryLake` reach what those sources do not: ACS at any geography down to block groups, joins, rankings and calculated columns.
- `searchDataDictionary` and `describeDataset` say which dataset covers a topic, how current it is and what each variable means. When the question also asks what the variables mean, pass `include_variables` to `searchDataDictionary` and skip `describeDataset`.
- `getReport` returns the published dashboard report. It is long, so use it only when asked for the report. Like `getForecast`, it takes a `place` name.

## Work efficiently

- Answer what was asked. When a question names no place, run it nationally rather than asking for one.
- A ranking across every county or block group is one `queryLake` query with ORDER BY and LIMIT. Filter `year`, `layer` and `state` where a table has them, and join `app.geo_search` on `geoid` to name the places.
- `exploreData` takes `order_by`, such as `["calendar_year"]` for a series or `["permitted_units desc"]` with a limit for the top places.
- `searchDataDictionary` and `describeDataset` give each dataset's `tables`, the names `queryLake` reads it by.
- Before you build on a table, check in the data dictionary what its columns measure, in what units and at which geographies. A table with a fitting name may count something else, and one listed for a geography may be empty there, so confirm with a count before you rank.
- Stop once you have what the question needs.

## Write the answer

- Lead with the result, one line per finding, each with the place, the figure and its year.
- Report what the data shows and no more. Add a line only when it changes how to read the figures, such as the reading you took or that very small places lead a ranking.
- When a question can be read more than one way, take the likeliest reading, answer it and say which you took.
- When ranking a rate, say how large the top places are, because the smallest often lead.
- Write for someone who has not seen the data: leave out table, column and variable names.
- Link each place with the `url` from `findEntity`, or from the `place` that `getForecast` and `getReport` return. End with the sources, linked with the `url` from the data dictionary tools or `findLakeTables`. Never write one of these links yourself.
- When these tools do not cover a question, say that they do not. That is not evidence that CommunityScale lacks the data.

## Example

Question: which large county has the highest share of renters?

Answer:

The Bronx, NY (linked) has the highest renter share among counties with at least 50,000 households, at 79.9% in 2024.
I took "large" as at least 50,000 households.
Sources: ACS 5-year table B25003, Tenure (linked)
