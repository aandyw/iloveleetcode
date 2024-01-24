# Questions to revisit
- [ ] `36_valid_sudoku.py`
- [ ] `128_longest_consecutive_sequence.py`


### DFS
Get better at knowing when to add and pop nodes to visit to achieve expected behaviour

See [`39_combination_sum.py`](39_combination_sum.py)
```python
tracked_candidates.append(candidates[candidate_i])
dfs(candidate_i, tracked_candidates, total + candidates[candidate_i])
tracked_candidates.pop()
dfs(candidate_i + 1, tracked_candidates, total)
```