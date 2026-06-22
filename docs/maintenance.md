# VllmWiki 维护规则

状态：single source of truth。
作用：统一承载仓库边界、证据层、状态机、promotion 条件、质量门和隐私边界。

## 仓库边界

VllmWiki 是一个从 vLLM issue/PR 中提炼工程机制的中文知识库。GitHub 仓库只保存 curated 结论层文档、公开可追溯摘要、维护规则和索引；不保存 raw evidence、本地分析材料、个人隐私文件或 issue/PR 全量抓取内容。

| 层级 | 路径 | 是否提交 | 用途 |
| --- | --- | --- | --- |
| 入口层 | `README.md`、`docs/` | 是 | 读者入口和维护规则 |
| 结论层 | `curated/` | 是 | 人工/agent 复核后的机制知识 |
| 决策层 | `candidates/bitwise_ledger.csv`、`candidates/notes/` | 是 | 候选状态、阻塞原因和下一步 |
| 控制层 | `data/*.yaml` | 是 | schema、tag、alias、version claim |
| 审计摘要 | `audit/manifest.md` | 是 | 数据快照和已知限制 |
| 本地 source/index 层 | `cases/`、`patterns/`、`domains/`、`indexes/`、`evidence/`、review queue、iteration audit | 否 | raw/generated/source layer，不进入 GitHub |

本地 source layer 可以保存 raw issue/PR、抓取表格、targeted evidence 和过程材料。公开文档只记录逻辑来源、上游 URL、case id 和可复核摘要，不记录个人机器绝对路径。

## 知识状态机

| 状态 | 含义 | 允许用途 |
| --- | --- | --- |
| `candidate` | 来自 raw body、表格提示、关键词或自动分类，尚未精读 | 导航、排队、ledger |
| `reviewed` | 已阅读 issue body 和 linked PR body，但证据链未闭环 | 机制 seed，必须标注缺口 |
| `curated` | 根因、修复、验证和边界都有证据支持 | 稳定 wiki lesson |
| `defer` | 相关但证据不足、范围过宽或主线缺口未闭环 | 保留在 ledger/next queue |
| `blocked` | 缺少评论、PR detail、diff 或外部证据 | backlog，不作为最终结论 |

## Promotion 条件

可以进入机制页稳定结论的 claim 必须同时具备：

- source evidence：issue、PR、评论、diff、测试或公开可追溯摘要。
- root cause：能解释现象，而不只是关键词命中。
- fix pattern、workaround 或 scope gate：说明修复或收口方式。
- verification contract：声明保护对象，例如 bit-identical、strict tolerance、logprob ranking、token equality、KV identity、metadata identity 或 semantic only。
- applicable boundary：说明硬件、backend、模型、版本、测试矩阵和不能外推的范围。

不能 promotion 的情况：

- 只有关键词命中或自动分类。
- 只有 closed state；closed 不等于 fixed。
- 只有 issue body，没有 linked fix、patch、maintainer resolution 或复现闭环。
- open PR 仍有 unresolved review risk；open PR 不等于 landed mechanism。
- 只能证明 semantic answer 相似，不能证明 tensor、KV、logits、token 或 metadata identity。
- umbrella issue 没有拆到具体 PR、具体机制或具体验证契约。

## 机制页结构

`curated/bitwise/*.md` 统一使用以下轻量结构：

```markdown
# 标题

## TL;DR

## 机制解释

## 稳定证据

## 边界与反例

## Evidence appendix
```

稳定证据使用短 evidence card，优先保留 3-5 个代表性 case。长表格、验证矩阵和公开证据摘要放入 `curated/bitwise/evidence_appendix/`，机制页只链接。

## 质量门

提交前至少检查：

```powershell
python scripts\validate_vllmwiki.py
git status --short
git ls-files cases patterns domains indexes evidence raw raw_data private_evidence source_layer targeted_evidence
```

期望：

- validator 通过，或明确说明失败原因。
- `git status` 只包含本轮有意修改。
- `git ls-files ...` 不输出 raw/generated/private 目录。
- README 只保留入口，不承载完整维护规则。
- promotion 条件、状态机和质量门只在本文完整展开。
- 新增公开文档不包含 raw evidence 全文、私有路径、`.env`、secrets 或个人隐私数据。

## 隐私与 Raw Data 边界

以下内容不得提交到 GitHub：

- raw issue/PR 全量抓取、评论全文批量镜像、targeted JSON、过程性 evidence dump。
- 本地分析材料、个人机器绝对路径、隐私文件、secrets、`.env`。
- 可再生 source/index 层：`cases/`、`patterns/`、`domains/`、`indexes/`、`evidence/`、`curated/bitwise_review_queue.*`、`audit/iteration_*`。

这些材料只可作为本地复核来源。公开仓库只保留 curated 结论层、公开可追溯摘要、维护规则和索引。
