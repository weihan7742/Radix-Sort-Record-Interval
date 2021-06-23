# Radix Sort - Record Interval
Consider a large dataset of records records. Given a number t, we wish to determine which
interval of length t contains the most recordss. All times in this question are measured in
whole seconds after midnight 1/1/1970, i.e. they are non-negative integers.

## Input
**recordss** is a unsorted list of non-negative integers. Each integer in recordss represents
the time that some records occurred.

**t** is a non-negative integer, representing a length of time in seconds.

## Output
An interval is a set of numbers that contains all numbers lying between some starting number
and some larger ending number (inclusive). These two numbers are called the endpoints of the
interval. The length of an interval is the absolute difference between the two endpoints.

Consequently, and interval starting at a and ending at b has length b-a. Conversley, an interval
starting at a of length d will end at a+d.

best_interval returns a two element tuple, (best_t, count). best_t is the time such
that the interval starting at best_t and ending at best_t + t contains more elements from
recordss than any other interval of length t.

If there are multiple such intervals, return the interval with minimal start time. Note that this
may mean the interval begins at a time which is not in recordss (see the example).

count is the number of elements in the interval of length t starting at best_t.

## Example
```
t = 5
recordss = [11, 1, 3, 1, 4, 10, 5, 7, 10]
>>> best_interval(records, t)
(0, 5)
```

## Complexity
best_interval should run in O(nk) time where
- n is the number of elements in recordss
- k is the greatest number of digits in any element in recordss

### Disclaimer
1. This case study derives from my school assignment.
2. Details of the actual case study has been sanitized and changed.

