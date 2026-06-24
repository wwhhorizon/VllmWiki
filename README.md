# VllmWiki

VllmWiki 是一个从 vLLM issue/PR 中提炼工程机制的中文知识库。

## 工作流概览

VllmWiki 的工作流是从上游证据到稳定机制结论的持续炼化流程：

1. **采集 source layer**：本地保存 vLLM issue、PR、评论、diff、review、测试和 targeted evidence；raw evidence 不进入公开仓库。
2. **生成候选与索引**：脚本生成 review queue、候选索引和初始页面骨架，只用于发现可能有价值的条目。
3. **进入 ledger / note**：候选写入 `candidates/bitwise_ledger.csv` 与 `candidates/notes/`，记录状态、证据摘要、阻塞原因和下一步。
4. **Agent 精读复核**：每轮选择 1-3 个 bounded item，精读 issue body、comments、linked PR、changed files、review comments 和 tests。
5. **Promotion 判断**：只有同时具备 source evidence、root cause、fix/workaround/scope gate、verification contract 和 applicable boundary 的 claim，才进入稳定机制页。
6. **沉淀 curated 机制页**：稳定结论写入 `curated/bitwise/`，未闭环但有价值的条目留在 `curated/bitwise/next.md` 或候选 note。
7. **质量门**：提交前运行 validator、检查链接和 raw/generated/private 泄漏，确保公开仓库只保留可复核的结论层与维护规则。

## 与 KernelWiki 工作流对比

VllmWiki 借鉴 KDA 中 KernelWiki 的分层炼化方式，但面向的是 vLLM serving correctness / deterministic 机制，而不是 GPU kernel 优化知识。

| 维度 | KernelWiki | VllmWiki |
| --- | --- | --- |
| 核心目标 | 把 GPU kernel 优化资料炼化成可检索、可复用的优化知识库 | 把 vLLM issue/PR 炼化成可复核的工程机制知识库 |
| 原始材料 | `sources/`：PR、官方文档、博客、contest、代码片段 | 本地 source layer：issue/PR JSON、comments、diff、review、tests、targeted evidence |
| 候选层 | `candidates/*.yaml` 记录各 repo PR 的 include/defer/exclude 决策 | `candidates/bitwise_ledger.csv` 与 `candidates/notes/` 记录 candidate/reviewed/curated/defer/blocked/exclude |
| 综合层 | `wiki/` 下按 hardware、techniques、patterns、kernels、languages、migration 组织 | `curated/bitwise/` 下按 verification contracts、prefix cache、KV identity、batch invariance、dispatch、dtype 组织 |
| 索引入口 | `queries/` 自动生成 by-problem、by-technique、by-repo、by-hardware 等索引 | 专题 README、`next.md`、ledger 与查询脚本共同承担导航 |
| 证据资产 | `artifacts/` 保存 diff、kernel files、derived assets，并用 `PROVENANCE.yaml` 固定来源 | raw/generated/private 材料不进入公开仓库；公开文档只保留上游 URL、case id 和可复核摘要 |
| Promotion 标准 | 关注 confidence、reproducibility、performance claims、official-doc + upstream-code evidence | 关注 root cause、fix/workaround、verification contract、applicable boundary、merged/review/test 证据闭环 |
| 质量门 | schema/link 校验、verbatim asset 校验、repo size、version-sensitive claim registry | wiki 结构、链接、ledger、claim boundary 和 raw/private 泄漏检查 |

简言之，KernelWiki 问的是“这个 kernel 优化知识能不能复用”；VllmWiki 问的是“这个 vLLM 工程结论能不能被证据闭环地写成稳定机制”。

## 仓库内容边界

**公开仓库仅包含**：
- ` curated/ `：稳定机制页，每条结论须有上游证据链
- ` candidates/ `：候选 note（状态记录、决策依据）与 ledger
- ` docs/ `：维护规则、agent loop 规范、术语表
- ` scripts/ `：验证器、迭代 runner、证据抽取等工具脚本
- ` .github/workflows/ `：CI 治理检查

**公开仓库不包含**：
- raw evidence、source layer、私有数据
- artifacts、generated 层、临时审计产物
- 本地实验日志、模型输出

完整维护规则见 [docs/maintenance.md](docs/maintenance.md)。

## 读者入口

- bitwise / deterministic 机制入口：[curated/bitwise/README.md](curated/bitwise/README.md)
- 稳定机制页：[curated/bitwise/](curated/bitwise/)
- 当前未闭环队列：[curated/bitwise/next.md](curated/bitwise/next.md)

## 维护者入口

- 维护规则：[docs/maintenance.md](docs/maintenance.md)
- Agent loop：[docs/agent_loop.md](docs/agent_loop.md)
- 术语表：[docs/glossary.md](docs/glossary.md)
