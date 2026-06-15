# KDA 调研笔记

状态：基于源材料的参考笔记。  
已阅读的本地源材料：

- `mit-han-lab/kernel-design-agents`，commit `dda6be3cf1baedd3ed9c76511ef02f72243cc14c`
- KDA 的 `README.md`、`docs/agent-flow.md`、`prompts/basic-flow.md`、`CLAUDE.md`
- KDA 子模块来源 `DongyunZou/KernelWiki` 的 README 与仓库结构
- 用户提供的知乎链接 `https://zhuanlan.zhihu.com/p/2044459666327999866` 在当前环境无法读取正文，因此不作为可验证证据

## KDA 是什么

KDA 描述的是一套面向性能敏感 CUDA kernel 任务的 agent-centric workflow。对 VllmWiki 最重要的不是 CUDA 领域本身，而是它的操作循环：

1. 创建独立任务工作区。
2. 定义 task contract：目标、输入/输出、正确性要求、约束、验证命令、评估命令和 promotion criteria。
3. 让 agent 先检查本地代码与文档。
4. 写 draft plan，再转成可执行 plan。
5. 一次实现或评估一个 candidate。
6. 每个有意义的 candidate 后都运行验证。
7. 必要时测量目标指标。
8. 记录 candidate、父子关系、benchmark/evaluation/profile 证据，以及 keep/revise/reject 决策。
9. 重复直到满足 promotion criteria，或把 blocker 明确写出。

对 VllmWiki 来说，candidate 不是 CUDA 实现，而是候选 wiki claim、机制、issue-PR 链接或优化手段。

## KernelWiki 提供了什么

KernelWiki 是 KDA 指向的最具体 wiki 实现。它采用三层结构：

| KernelWiki 层 | 含义 | VllmWiki 对应物 |
| --- | --- | --- |
| `sources/` | 原始 PR、blog、doc、contest 页与不可变摘要 | raw JSONL、case 页、源摘录、source manifest |
| `wiki/` | 带 id/frontmatter 的综合知识页 | curated 机制页、domain、pattern |
| `queries/` | 自动生成的交叉引用索引 | indexes、query 输出、生成导航页 |

它还使用控制文件：

- `data/schemas.yaml`：每类页面的必填/可选字段。
- `data/tags.yaml`：受控词表。
- `data/aliases.yaml`：标准术语与同义词。
- `data/version-claims.yaml`：版本敏感 claim 注册表。
- `candidates/`：带 include/defer/exclude 决策的候选 ledger。
- `artifacts/`：带 provenance 的 verbatim/extracted/derived 证据包。

对应工具包括：

- `scripts/query.py`：统一关键词与过滤搜索。
- `scripts/get_page.py`：按 id/path 取页面，并可展开 source。
- `scripts/grep_wiki.py`：跨 wiki/source 正文做 regex 搜索。
- `scripts/validate.py`：schema 与链接验证。
- `scripts/generate-indices.py`：重建 cross-reference index。
- `scripts/repo_status.py`：输出语料统计。

## 映射到 VllmWiki

VllmWiki 应该是一个持续演进的知识系统，而不是一次性报告：

| KDA 概念 | VllmWiki 规则 |
| --- | --- |
| Task contract | 每条 curated lane 都写清目标、不变量、源输入、验证门与 promotion criteria。 |
| Candidate implementation | 每个候选 claim/measure/link 都进入 ledger，带状态和父证据。 |
| Validation command | `scripts/validate_vllmwiki.py` 检查链接、必需页面、ledger 与 curated 证据标记。 |
| Evaluation command | 迭代脚本报告覆盖率、队列规模、缺失源状态，以及 curated/reviewed 比例。 |
| Promotion criteria | `candidate -> reviewed -> curated` 需要源阅读、修复证据、验证方式和边界条件。 |
| Evidence records | 源快照、摘录、PR 链接、队列行和 audit 报告都必须靠近 claim。 |
| Repeat loop | `run_vllmwiki_iteration.py` 重建生成内容，并记录变化与 blocker。 |

## 当前构建目标

- `all/data/raw/*.jsonl` 作为原始源快照。
- `VllmWiki/cases/**` 作为 source-adjacent issue 页面。
- `VllmWiki/patterns/**` 与 `VllmWiki/domains/**` 作为生成导航视图。
- `VllmWiki/curated/**` 作为提升后的机制页。
- `VllmWiki/candidates/**` 存放 include/defer/exclude ledger。
- `VllmWiki/data/*.yaml` 存放 schema、tag、alias 与 version-sensitive claim。
- `VllmWiki/indexes/**`、`VllmWiki/evidence/**` 与后续 `VllmWiki/queries/**` 作为可查询表面。

## Bitwise 优先任务契约

- 目标：把 vLLM 中 bitwise、deterministic decoding、batch invariance、prefix-cache equivalence、KV identity 和 quantization drift issue 炼化成可复用机制。
- 正确性要求：没有原始 issue/PR 证据的 claim 不得 curated；依赖评论的结论必须标记 blocked。
- 验证命令：`python VllmWiki\scripts\validate_vllmwiki.py`。
- 迭代命令：`python VllmWiki\scripts\run_vllmwiki_iteration.py`。
- 提升标准：一条 bitwise measure 必须写清 divergence path、fix mechanism、verification contract、scope boundary 和缺失证据状态。

## 立即缺口

- 本地数据有 issue/PR 正文，但缺少 issue 评论正文。
- PR changed files 和 commit diff 通常不在本地。
- 很多宽泛 pattern hit 噪声较高，应保持 `candidate`。
- bitwise 机制页结构已经较强，但每条 claim 仍需要更细的 source excerpt 和 ledger state，才能完全称为 `curated`。
