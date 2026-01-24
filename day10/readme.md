# Day 10: SQL Window Functions Foundation

**Date:** Jan 25, 2026  
**Duration:** 2 hours  
**Focus:** Window functions (RANK, DENSE_RANK, PARTITION BY)

## Problems Solved
1. ✅ #178 Rank Scores (25 min) — `DENSE_RANK()` basics
2. ✅ #184 Department Highest Salary (25 min) — `PARTITION BY` + JOIN
3. ✅ #185 Department Top 3 Salaries (40 min) — Multi-table window query

## Concepts Mastered
- `ROW_NUMBER` vs `RANK` vs `DENSE_RANK`
- `PARTITION BY` = "restart ranking per group"
- Window functions vs GROUP BY (keep all rows vs collapse)
- Combining windows + JOINs

## Notes
- #185 took longer than planned (40 min vs 25 min) — expected for first time
- PARTITION BY syntax clicked after #184
- Next: LAG/LEAD for day-over-day calculations

## Next Session
- Pandas: replicate #178 and #184 using `.rank()` and `.groupby()`
- DSA: Number of Islands (graph intro)