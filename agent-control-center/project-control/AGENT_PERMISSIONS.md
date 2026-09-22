# AGENT PERMISSIONS

| Agent | Read | Write Source | Review | Merge Main | Release | Deploy |
|---|---|---:|---:|---:|---:|---:|
| Planner | Yes | No | No | No | No | No |
| Coder | Yes | Task branch only | No | No | No | No |
| Reviewer | Yes | No | Yes | No | No | No |
| Release Manager | Yes | No | No | No | Yes after approval | No |
| Deploy Agent | Approved artifact only | No | No | No | No | Yes after approval |
| State Monitor | Yes | Status only | No | No | No | No |
| Human Owner | Yes | Yes | Yes | Yes | Yes | Yes |

## Mandatory gates
1. No `APPROVED` → no coding.
2. No `TEST_PASS` → no review pass.
3. No `REVIEW_PASS` → no release candidate.
4. No `FINAL_APPROVED` → no merge/release/deploy.
