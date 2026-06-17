# VllmWiki 维护说明

状态：长期维护文档。  
作用：统一说明 VllmWiki 的组织方式、证据规则、质量门和迭代协议。过去分散在 `METHODOLOGY.md`、`QUALITY_GATE.md`、`ITERATION_PROTOCOL.md`、`WIKI_REFINEMENT_FLOW.md`、`KERNELWIKI_REFINEMENT_NOTES.md` 中的长期规则已合并到本文。

## 一句话设计

VllmWiki 是一个 source-backed、持续 curated 的 vLLM issue/PR 工程知识库。它效仿 KernelWiki 的知识库构建方式，而不是复刻 KDA 的 kernel/算子优化流程。

所有 wiki claim 在原始 issue、PR、评论、diff 或本地 targeted evidence 被阅读前，都只能算 `candidate`，不能当作最终结论。

## 仓库边界

GitHub 仓库保存结论层与维护契约：

| 层 | 目录/文件 | 是否提交 | 作用 |
| --- | --- | --- | --- |
| 入口层 | `README.md`、`Agent_loop.md` | 是 | 项目入口和 agent 自主迭代规划 |
| 结论层 | `curated/` | 是 | 人工/agent 复核后的机制知识 |
| 决策层 | `candidates/bitwise_ledger.csv` | 是 | 记录 include/defer/exclude 与下一步动作 |
| 控制层 | `data/*.yaml` | 是 | schema、tag、alias、version claim |
| 审计层 | `audit/manifest.md` | 是 | 数据快照和已知限制 |
| 工具层 | `scripts/` | 是 | 抓取、抽取、查询、验证脚本 |
| 本地 source/index 层 | `cases/`、`patterns/`、`domains/`、`indexes/`、`evidence/`、review queue、iteration audit | 否 | 可再生候选页、索引表和过程材料 |

原始数据与 targeted evidence 放在仓库外：

```text
E:\Vllm-Issue\all\data\raw
E:\Vllm-Issue\all\data\tables
E:\Vllm-Issue\all\data\targeted\bitwise
```

这样做的目的不是丢弃证据，而是让 GitHub 仓库保持为“结论 wiki”，避免大规模机器生成页面造成维护噪声。

## KernelWiki 对齐

VllmWiki 效仿 KernelWiki 的核心是知识组织和证据约束：

| KernelWiki 概念 | VllmWiki 对应 |
| --- | --- |
| `sources/` raw/source layer | 仓库外 `all/data/**` 与本地生成 `cases/` |
| `wiki/` synthesized layer | `curated/` 和根目录主线综合文档 |
| `queries/` generated index layer | 本地生成 `indexes/`、`evidence/` 与查询脚本 |
| `data/schemas.yaml` | `data/schemas.yaml` |
| `data/tags.yaml` / `aliases.yaml` | `data/tags.yaml`、`data/aliases.yaml` |
| `data/version-claims.yaml` | 数据快照、评论缺口和参考来源声明 |
| `candidates/` ledger | `candidates/bitwise_ledger.csv` |
| validator | `scripts/validate_vllmwiki.py` |

VllmWiki 不在文档中引入 KDA 的 kernel 优化流程；KDA/KernelWiki 只作为 wiki 构建方式的参考。

## 知识状态

| 状态 | 含义 | 允许用途 |
| --- | --- | --- |
| `candidate` | 来自 raw body、表格提示、关键词或自动分类 | 导航、排队、ledger |
| `reviewed` | 已阅读 issue body 和 linked PR body | 机制 seed，必须标注缺口 |
| `curated` | 根因、修复、验证和边界都有证据支持 | 稳定 wiki lesson |
| `blocked` | 缺少评论、PR detail、diff 或外部证据 | backlog，不作为最终结论 |
| `defer` | 相关但证据不足或范围未拆清 | 保留在 ledger，等待下一轮 |

## 证据规则

- 表格字段和自动分类是路由提示，不是真相。
- `root_cause_hint` 不是 confirmed root cause。
- `closed` 不等于 fixed。
- linked PR 在检查正文、closure language、changed files 或 maintainer comment 前，不能被完全信任。
- 缺少评论正文时，如果 resolution 可能在评论里，必须保持 `candidate`、`defer` 或 `blocked`。
- 每条优化手段必须回答：改了什么、为什么修复、适用边界、如何验证。
- bitwise/deterministic 结论必须声明验证对象：tensor bit equality、KV identity、logits/token equality、strict numeric tolerance，还是 semantic answer equivalence。

## 机制页模板

`curated/bitwise/*.md` 应尽量使用同一套结构：

```markdown
# 机制名称

状态：curated / reviewed / candidate。  
范围：该机制覆盖和不覆盖什么。

## 问题定义

## 典型触发条件

## 代表证据

## 根因机制

## 修复方式

## 验证契约

## 适用边界

## 仍需补证
```

不要把大段原始 issue 正文放进机制页。机制页应该保留短摘录、issue/PR URL、本地 evidence 路径和结论解释。

## 迭代协议

每一轮只围绕一个明确 lane 推进。当前 lane 是 `bitwise-determinism`。

标准循环：

1. 明确本轮要回答的问题。
2. 从 `candidates/bitwise_ledger.csv` 或本地 review queue 选 bounded item。
3. 读取对应 issue、PR、评论、diff 或 targeted JSON。
4. 对 claim 执行 `include`、`defer` 或 `exclude`。
5. 更新对应 `curated/bitwise/*.md` 和 ledger。
6. 运行 `python scripts\validate_vllmwiki.py`。
7. 提交前确认没有把 raw/generated 数据重新加入 Git。

Promotion 条件：

- `candidate -> reviewed`：已读 issue body；有 linked PR 时已读 PR body；源文本支持机制；验证方式或缺失项已说明。
- `reviewed -> curated`：root cause、fix、verification、scope boundary 都有证据；评论或 PR detail 缺口已关闭，或明确说明为什么不阻塞结论。

## Codex Agent 迭代协议

bitwise 主线的持续迭代由 Codex agent 执行，而不是由脚本自动 promotion。每轮迭代先读取 `candidates/bitwise_ledger.csv`，优先选择 `priority=high` 且 `risk_status != stable` 的条目，再精读仓库外 `E:\Vllm-Issue\all\data\targeted\bitwise` 中的本地 targeted evidence。

每轮 agent 必须完成三件事：

- 根据 ledger 选择有限数量的对象，说明为什么本轮读这些对象。
- 精读 issue/PR body、changed files、patch、review comments、reviews、issue comments 和 timeline，区分观察现象、根因、修复、验证契约和边界。
- 对每个对象给出明确处理：下沉到机制页、更新 ledger/专题 next queue 的阻塞原因，或保持现有状态。

每轮 agent 明确不能做三件事：

- 不能只凭标题、自动摘要或表格字段 promotion。
- 不能把 review comment 暴露的风险写成已修复事实，除非 patch/test/maintainer resolution 已闭环。
- 不能把仓库外 raw/generated evidence 重新加入 GitHub 结论层。

`risk_status` 用来驱动复核策略：

| risk_status | 复核含义 |
| --- | --- |
| `stable` | 已进入稳定结论层，除非出现新证据，否则不进入默认复核队列。 |
| `include_with_boundary` | 结论可 include，但边界仍需写清楚，尤其要确认 review risk 是否已有 patch/test 闭环。 |
| `unresolved_review_risk` | PR body 或初始 patch 有价值，但 review comment 暴露的 correctness 风险尚未闭环。 |
| `defer_blocked` | 缺 linked fix PR、changed files、test 或 maintainer resolution，不能 promotion。 |

持续迭代的推荐节奏是：Codex agent 先按 ledger 选题，再深读对应原始 JSON、patch 和评论；只有当证据同时支撑根因、修复、验证契约和适用边界时，才更新机制页。如果只是发现新风险或缺口，应更新专题 next queue 和 ledger 的 `blocking_reason`，保持 `defer` 或边界化 include。

## 质量门

提交前至少检查：

```powershell
python scripts\validate_vllmwiki.py
git status --short
git ls-files cases patterns domains indexes evidence curated/bitwise_review_queue.csv curated/bitwise_review_queue.md
```

期望：

- validator 通过。
- `git status` 只包含本轮有意修改。
- `git ls-files ...` 不输出 raw/generated 目录。
- 新增文档为中文；上游 issue/PR 标题和引用可以保留英文原文。
- 根目录文档保持少量稳定入口，不新增一次性过程文档。

## 当前已知限制

- 早期全量数据仍有大量 issue 缺评论正文；bitwise targeted evidence 已补齐一批评论和 PR detail，但不能外推到所有问题族。
- 自动生成的 `patterns/`、`domains/`、`cases/` 只适合本地导航，不代表 curated 结论。
- `curated/bitwise/evidence_synthesis.md` 是 bitwise 第一轮证据综合，后续稳定结论应继续下沉到 `curated/bitwise/*.md`。
