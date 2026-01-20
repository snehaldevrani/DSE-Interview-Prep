# Day 6: Jan 19, 2026

**Duration**: ~2–3 hours  
**Focus**: Core SQL foundations (concept-first, analytics-oriented)

## SQL Topics Covered
- SELECT queries (specific columns vs *)
- WHERE filtering:
  - AND / OR
  - IN, BETWEEN
  - LIKE patterns
- ORDER BY (ASC/DESC, multiple columns)
- LIMIT and OFFSET
- Query execution order (logical understanding)
- Table aliases (usage, necessity, best practices)

## Joins
- INNER JOIN
- LEFT JOIN
- Differences in row retention and NULL behavior
- Why LEFT JOIN is common in analytics
- Join syntax and matching logic
- Aliases in joins and self-joins

## Aggregation
- GROUP BY
- Aggregate functions:
  - COUNT
  - SUM
  - AVG
  - MIN / MAX
- GROUP BY rules (columns in SELECT)
- GROUP BY with JOINs

## HAVING vs WHERE
- WHERE filters rows
- HAVING filters groups
- Understood execution order:
  FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
- Practiced combined usage
- Intentionally paused for reinforcement later

## LeetCode SQL (Platform)
- #182 Duplicate Emails
  - GROUP BY + HAVING COUNT > 1
  - Understood why WHERE cannot be used

## Notes
- Focused on depth and reasoning, not memorization
- Wrote queries manually and corrected logical mistakes
- Prioritized understanding how SQL evaluates queries
- Marked GROUP BY + HAVING for light revision tomorrow
