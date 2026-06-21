# VllmWiki 维护说明

状态：长期维护文档。  
作用：统一说明 VllmWiki 的仓库边界、证据规则、静态质量门和机制页模板。过去分散在 `METHODOLOGY.md`、`QUALITY_GATE.md`、`ITERATION_PROTOCOL.md`、`WIKI_REFINEMENT_FLOW.md`、`KERNELWIKI_REFINEMENT_NOTES.md` 中的长期规则已合并到本文。

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

原始数据与 targeted evidence 放在仓库外的 source layer。公开文档只记录逻辑层级，不记录个人机器上的绝对路径：

```text
source/raw
source/tables
source/targeted/<topic>
```

这样做的目的不是丢弃证据，而是让 GitHub 仓库保持为“结论 wiki”，避免大规模机器生成页面造成维护噪声。

## KernelWiki 对齐

VllmWiki 效仿 KernelWiki 的核心是知识组织和证据约束：

| KernelWiki 概念 | VllmWiki 对应 |
| --- | --- |
| `sources/` raw/source layer | 仓库外 source layer 与本地生成 `cases/` |
| `wiki/` synthesized layer | `curated/` 下的专题入口和机制页 |
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

不要把大段原始 issue 正文放进机制页。机制页应该保留短摘录、issue/PR URL、证据来源标识和结论解释；公开文档不记录个人机器上的绝对路径。

## 与 Agent Loop 的分工

本文只维护静态契约：仓库哪些层可以提交、什么证据可以支撑 claim、机制页应保持什么模板、提交前质量门检查什么。

每轮 agent 如何选题、如何深读 issue/PR/comment/diff、如何处理 `stable` / `include_with_boundary` / `unresolved_review_risk` / `defer_blocked`，统一维护在 [Agent_loop.md](Agent_loop.md)。如果动态流程需要调整，只改 `Agent_loop.md`，避免同一条 promotion 规则在两份文档里分叉。

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
- 早期一次性证据综合文档已移除；稳定结论应直接维护在 `curated/<topic>/` 的专题入口、机制页和 next queue 中。
