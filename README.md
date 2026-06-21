# VllmWiki

VllmWiki 是一个从 `vllm-project/vllm` issue 与 PR 语料炼化出的中文工程知识库。它效仿 KernelWiki 的知识组织方式：原始材料留在本地，GitHub 仓库只保存可阅读、可维护、可追溯的结论层文档。

当前已经完成第一条专题线：vLLM 中 deterministic / bitwise 相关问题的机制化整理。它只是项目的一部分，专题内容统一放在 [curated/bitwise/](curated/bitwise/)。

## 项目如何迭代

VllmWiki 的核心不是一次性报告，而是持续炼化流程：

1. 在仓库外保留 raw issue/PR、表格索引和 targeted evidence，作为可回溯 source layer。
2. 从本地证据生成候选索引、review queue、source-adjacent 页面和自动聚类结果。
3. 把值得复核的 claim 写入 `candidates/` 下的 ledger，标记 `include`、`defer` 或 `exclude`。
4. 逐条阅读 issue、PR、comment、diff 或 targeted JSON，区分观察现象、根因机制、修复方式和验证契约。
5. 只有证据足够稳定的结论才下沉到 `curated/` 下对应专题页。
6. README 只保留项目概览和阅读路线；细节规则、质量门和模板放在 [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md)。

持续迭代时，Codex agent 先根据 ledger 选择高优先级风险项，再精读本地 evidence，最后决定是否更新机制页、ledger 和下一轮补证队列。具体 agent loop 写在 [Agent_loop.md](Agent_loop.md)。

## 阅读入口

| 文档 | 作用 |
| --- | --- |
| [Agent_loop.md](Agent_loop.md) | Codex agent 自主迭代规划 |
| [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md) | 仓库边界、证据规则、静态质量门和机制页模板 |
| [curated/bitwise/README.md](curated/bitwise/README.md) | 当前 bitwise 专题入口 |
| [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv) | 当前专题 claim 的 include/defer/exclude 账本 |

## 文件树分工

```text
VllmWiki/
├── README.md                         # 项目概览、迭代流程和阅读路线
├── Agent_loop.md                     # Codex 自主迭代规划
├── WIKI_IMPLEMENTATION.md            # 仓库边界、证据规则、质量门与机制页模板
├── curated/                          # 人工/agent 复核后的结论层
│   └── bitwise/                      # 当前 bitwise 专题
├── candidates/                       # claim 决策账本
├── data/                             # schema、tag、alias、version claim
├── audit/                            # 数据快照说明；机器生成审计文件本地忽略
└── scripts/                          # 抓取、抽取、查询、验证脚本
```

仓库外 source layer 保存 raw / targeted evidence。仓库内被忽略的 `cases/`、`patterns/`、`domains/`、`indexes/`、`evidence/`、`curated/bitwise_review_queue.*`、`audit/iteration_*` 是本地可再生材料，不进入 GitHub 结论层。公开文档不记录个人机器上的绝对路径。

## 维护原则

- README 只说明项目整体和迭代方式，不承载完整操作手册。
- `curated/` 中的结论必须能回链到 issue、PR、评论、diff 或本地 targeted evidence。
- `candidates/` 记录尚未 fully curated 的 claim，避免候选结论混入机制页。
- 后续新增专题时，应优先在 `curated/<topic>/` 下形成入口、机制页和补证队列，不在根目录增加一次性专题文档。
