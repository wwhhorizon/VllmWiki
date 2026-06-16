# KernelWiki 炼化方式笔记

状态：基于 KernelWiki 源仓库的 wiki 构建参考。  
目标：记录 KernelWiki 如何把原始材料炼化成结构化知识库，并映射到 VllmWiki。这里不讨论 KDA 的 kernel/算子优化流程。

## KernelWiki 仓库怎么说

KernelWiki 的 README、SKILL、CLAUDE 和 schema 文档里描述了一套知识库构建方式：

1. `sources/`：存放原始来源的结构化摘要，例如 PR、官方文档、blog、contest。
2. `wiki/`：存放综合后的知识页，每页有唯一 `id` 和 YAML frontmatter。
3. `queries/`：从 wiki/source frontmatter 自动生成交叉索引，不手写。
4. `data/`：存放 schema、tag、alias、version claim 等控制文件。
5. `candidates/`：存放候选来源 ledger，并记录 include/defer/exclude。
6. `artifacts/`：存放可追溯证据包，并用 `PROVENANCE.yaml` 固定来源。
7. `scripts/validate.py`：检查 frontmatter、schema、链接、证据和 ledger。
8. `scripts/query.py` / `get_page.py` / `grep_wiki.py`：提供知识库查询入口。

这就是 VllmWiki 要效仿的核心：不是复刻 KDA 的优化执行流程，而是复刻 KernelWiki 的 **知识组织、证据约束和查询验证方式**。

## KernelWiki 的炼化路径

```text
候选来源
  -> candidates/ledger
  -> sources/ 原始摘要页
  -> wiki/ 综合知识页
  -> queries/ 自动索引
  -> validate.py 质量门
```

其中每个 wiki claim 都必须能追溯到 source，且受 schema、tag、alias 和 confidence/reproducibility 规则约束。

## 映射到 VllmWiki

| KernelWiki 做法 | VllmWiki 对应 |
| --- | --- |
| `sources/` 原始摘要 | `cases/` 中每个 issue 的 source-adjacent 页面，以及 `audit/manifest.*` |
| `wiki/` 综合知识页 | `curated/` 里的 bitwise 机制页 |
| `queries/` 自动索引 | `indexes/`、`evidence/`，以及 `query/get/grep` 工具 |
| `data/schemas.yaml` | VllmWiki 的页面/ledger schema |
| `data/tags.yaml` | bitwise、prefix-cache、kv-cache-identity 等受控标签 |
| `data/aliases.yaml` | deterministic、reproducible、cache-hit 等同义词归一 |
| `data/version-claims.yaml` | 数据快照、评论缺失、KernelWiki 参考版本声明 |
| `candidates/` ledger | `candidates/bitwise_ledger.csv` |
| `validate.py` | `scripts/validate_vllmwiki.py` |

## VllmWiki 当前应该怎么炼化

VllmWiki 的目标是把 vLLM issue/PR 炼化成 wiki，而不是把 KDA 的算子优化流程写进文档。

当前聚焦 lane 是 bitwise/deterministic：

1. 从 `issues_raw.jsonl`、`prs_raw.jsonl` 和 CSV 表生成 `cases/`、`patterns/`、`domains/`。
2. 从自动命中的 bitwise 证据里生成 `curated/bitwise_review_queue.md`。
3. 把最重要的候选写入 `candidates/bitwise_ledger.csv`，标记 include/defer/exclude。
4. 只有读过原始 issue/PR，并明确缺失评论状态后，才把机制写入 `curated/bitwise/*.md`。
5. 每轮运行 `validate_vllmwiki.py`，保证链接、核心文件和 ledger 存在。

## 与 KernelWiki 仍有差距

- VllmWiki 目前还没有真正的 `sources/` 目录；`cases/` 暂时承担 source-adjacent page 作用。
- VllmWiki 的 Markdown 页还没有全面 YAML frontmatter。
- `queries/` 还没有像 KernelWiki 那样生成 by-problem/by-technique/by-repo 页面。
- 本地缺少 issue 评论正文和 PR changed files，因此很多 claim 必须保持 candidate/defer。

下一步应该优先补的是 KernelWiki 风格的结构，而不是增加 KDA 优化流程叙述。
