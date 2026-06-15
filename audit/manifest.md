# 构建 Manifest

状态：`candidate_snapshot`
生成时间 UTC：`2026-06-15T13:56:07.807825+00:00`

## 源文件

| 源 | 行数 | SHA256 | 路径 |
| --- | ---: | --- | --- |
| `issues_raw` | 16,243 | `00c2deefebc0c2966812e18e0d964e95b1eec34011029f53570f98b316f60404` | `E:\Vllm-Issue\all\data\raw\issues_raw.jsonl` |
| `prs_raw` | 28,120 | `304c4affe852f1257f3591d51c24815f9cf6b57f777c1dc8acc0306c7846dbc5` | `E:\Vllm-Issue\all\data\raw\prs_raw.jsonl` |
| `cases_csv` | 7,345 | `4e628465b1495a186f21327950e99ec4077403f5a9d6748a8bae04ae9650a6c2` | `E:\Vllm-Issue\all\data\tables\cases.csv` |
| `prs_csv` | 8,974 | `751ba5afe1f00ca6bd12d22e47952851e079fc6464a26715f3f05057db5aafd3` | `E:\Vllm-Issue\all\data\tables\prs.csv` |
| `issue_pr_links_csv` | 2,272 | `0b870c7813973ce17ea7e43b59033d0db2356413429a819beb1e95e8fbb108a4` | `E:\Vllm-Issue\all\data\tables\issue_pr_links.csv` |

## 覆盖率

| 指标 | 值 |
| --- | ---: |
| `unique_issues` | 15,818 |
| `unique_cases` | 7,239 |
| `unique_prs` | 8,931 |
| `issues_with_links` | 1,275 |
| `index_issue_rows` | 15,818 |
| `pattern_evidence_rows` | 145,553 |
| `missing_issue_pages` | 0 |
| `issues_with_missing_comment_bodies` | 14,271 |

## 已知限制

- 本地没有 issue 评论正文；带评论的 issue 仍应保持 candidate 或 blocked。
- 没有 pull-request detail 数据时，PR 表中的 merge state 不能作为可靠 merge 证明。
- Pattern 证据在人工复核前只是基于关键词的候选证据。
- 本地 case 表里的 root_cause 为空；根因需要源文本或 PR/comment 证据支持。
