# Day 16

Jan 30, 2026

Back to it. Needed this focus.

## SQL Window Functions - Crushed It

Solved 4 problems today:

1. **#178 Rank Scores** - DENSE_RANK() basics clicked
2. **#184 Department Highest Salary** - PARTITION BY finally makes sense  
3. **#185 Department Top 3 Salaries** - The full pattern is clear now
4. **#180 Consecutive Numbers** - Different approach, self-join with offsets

## What actually clicked

PARTITION BY = restart ranking for each group, but keep all rows (not like GROUP BY).

The "top N per group" pattern:
```sql
WITH ranked AS (
  SELECT *, DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as rk
  FROM Employee
)
SELECT * FROM ranked WHERE rk <= 3
```

Consecutive Numbers showed me window functions aren't the only tool - sometimes self-joins are cleaner.

## Mental state

2 hours of solid focus felt good. Using this to move forward.

Back on track. Ready for graphs tomorrow.