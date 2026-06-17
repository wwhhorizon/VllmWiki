# VllmWiki 实现说明

状态：持续更新的实现文档。  
参考状态：已从 KernelWiki 源仓库阅读；具体调研见 [KernelWiki 炼化方式笔记](KERNELWIKI_REFINEMENT_NOTES.md)。

## 一句话设计

VllmWiki 是一个 source-backed、evidence-graph-driven、持续 curated 的 vLLM issue/PR 工程知识库。所有生成结论在原始 issue、PR 和可用讨论证据被阅读前，都只是 hypothesis。

## 为什么这是 Wiki，不是报告

报告会冻结结论；VllmWiki 把 raw evidence、candidate pattern、curated mechanism、review queue 和 quality gate 放在一起，让知识库可以持续迭代而不丢 provenance。

## KernelWiki 对齐

VllmWiki 主要效仿 KernelWiki 的知识库构建方式：source pages、wiki pages、queries、schema/frontmatter、candidate ledger、validator 和 version claims。这里不描述 KDA 的 kernel/算子优化流程。

| KernelWiki 概念 | VllmWiki 实现 |
| --- | --- |
| `sources/` raw layer | `all/data/raw/*.jsonl`、`all/data/tables/*.csv`、[audit/manifest.md](audit/manifest.md)、case 页源摘录 |
| `wiki/` synthesized layer | [curated/**](curated/bitwise_determinism.md)、[patterns/**](patterns/bitwise_determinism_equivalence.md)、[domains/**](domains/attention_kv_cache.md)、本地生成的 `cases/**` |
| `queries/` generated index layer | 本地生成的 `indexes/issues.csv`、`indexes/prs.csv`、`evidence/pattern_evidence.csv`、`scripts/` 查询工具 |
| `data/schemas.yaml` | [data/schemas.yaml](data/schemas.yaml)：case、pattern、mechanism、ledger 的必填字段 |
| `data/tags.yaml` / `aliases.yaml` | [data/tags.yaml](data/tags.yaml)、[data/aliases.yaml](data/aliases.yaml)：受控 bitwise 词表 |
| `data/version-claims.yaml` | [data/version-claims.yaml](data/version-claims.yaml)：数据快照和 KernelWiki 参考版本声明 |
| `candidates/` ledgers | [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv)：include/defer/exclude 决策 |
| query/get/grep/validate tools | [query_vllmwiki.py](scripts/query_vllmwiki.py)、[get_page.py](scripts/get_page.py)、[grep_wiki.py](scripts/grep_wiki.py)、[validate_vllmwiki.py](scripts/validate_vllmwiki.py) |

## 五层结构

| 层 | 目的 | 当前产物 |
| --- | --- | --- |
| Source layer | 保留本地 raw issue/PR 文本和 hash | `all/data/raw/*.jsonl`、[audit/manifest.md](audit/manifest.md) |
| Evidence layer | 抽取 source snippet 和候选链接，不伪装成最终真相 | 本地生成的 `evidence/pattern_evidence.csv`、`indexes/issues.csv`、`indexes/prs.csv` |
| Candidate wiki layer | 为每个 issue 和主要 pattern 生成页面，避免信息消失 | `cases/**`、`patterns/**`、`domains/**` |
| Curated mechanism layer | 把反复出现的机制提升成人类可读 lesson | [curated/bitwise_determinism.md](curated/bitwise_determinism.md)、`curated/bitwise/**` |
| Governance layer | 定义质量门、状态标签和迭代协议 | [QUALITY_GATE.md](QUALITY_GATE.md)、[ITERATION_PROTOCOL.md](ITERATION_PROTOCOL.md) |

## 知识状态

| 状态 | 含义 | 允许用途 |
| --- | --- | --- |
| `candidate` | 来自 raw body、表格提示或关键词证据 | 导航、triage、review queue |
| `reviewed` | 已阅读 issue body 和 linked PR body | 机制 seed 页，仍要标注 source limit |
| `curated` | 根因、修复、验证和边界都有证据支持 | canonical wiki lesson |
| `blocked` | 缺少评论、PR detail、文件或外部证据 | backlog，不作为最终结论 |

## 证据规则

- 表格是路由提示，不是真相。
- `root_cause_hint` 不是 root cause。
- `closed` 不等于 fixed。
- linked PR 在检查正文、closure language 和 PR detail 前不能被完全信任。
- 缺少评论正文的页面，如果 resolution 可能在评论里，就不能完全 curated。
- 每条优化手段必须回答：改了什么、为什么修复、适用边界、如何验证。

## 当前工具

- `python VllmWiki\scripts\generate_vllm_wiki.py`
- `python VllmWiki\scripts\generate_bitwise_review_queue.py`
- `python VllmWiki\scripts\run_vllmwiki_iteration.py`
- `python VllmWiki\scripts\query_vllmwiki.py bitwise --kind issue --limit 5`
- `python VllmWiki\scripts\get_page.py 33123 --follow-sources`
- `python VllmWiki\scripts\grep_wiki.py "deterministic prefix" --only wiki`
- `python VllmWiki\scripts\validate_vllmwiki.py`

## 子代理复核模型

子代理是 review lane，不是权威来源。每个子代理必须输出 reviewed item、promoted item、blocked item 和 rule update。主线程负责集成结论、维护文件一致性和 audit trail。

## 仍是 Candidate 的原因

- 多数 issue 评论正文本地不可用。
- PR merge/file/commit detail 不完整。
- 部分 issue-PR link 噪声较高，需要审计。
- 非 bitwise pattern family 目前仍主要是生成导航，还不是 curated lesson。
