# VllmWiki

VllmWiki 是一个从 `vllm-project/vllm` issue 与 PR 语料炼化出的中文工程知识库。它效仿 KernelWiki 的知识组织方式：原始材料留在本地，GitHub 仓库只保存可阅读、可维护、可追溯的结论层文档。

当前主线是 **bitwise / deterministic**：解释 vLLM 中 deterministic decoding、bitwise equality、batch invariance、prefix-cache equivalence、KV cache identity、dtype/quantization drift 等问题为什么会发生、如何修复、怎样验证。

## 项目如何迭代

VllmWiki 的核心不是一次性报告，而是持续炼化流程：

1. 在仓库外保留 raw issue/PR、表格索引和 targeted evidence，作为可回溯 source layer。
2. 从本地证据生成候选索引、review queue、source-adjacent 页面和自动聚类结果。
3. 把值得复核的 claim 写入 [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv)，标记 `include`、`defer` 或 `exclude`。
4. 逐条阅读 issue、PR、comment、diff 或 targeted JSON，区分观察现象、根因机制、修复方式和验证契约。
5. 只有证据足够稳定的结论才下沉到 [curated/bitwise/](curated/bitwise/) 机制页。
6. README 只保留项目概览和阅读路线；细节规则、质量门和模板放在 [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md)。

这意味着仓库里的 `curated/` 是结论层，`candidates/` 是决策账本；本地生成的 `cases/`、`patterns/`、`domains/`、`indexes/`、`evidence/` 只作为迭代材料，不作为 GitHub 结论发布。持续迭代时，ledger 会先给出高优先级风险项，自动复核循环只生成本地 audit 草稿；人工精读后才决定是否更新机制页、ledger 和下一轮补证队列。

## 阅读入口

| 文档 | 作用 |
| --- | --- |
| [BITWISE_DETERMINISTIC.md](BITWISE_DETERMINISTIC.md) | 当前主线总览，说明问题边界、阅读顺序和六个机制页 |
| [curated/bitwise_determinism.md](curated/bitwise_determinism.md) | bitwise/deterministic 的机制总览与优化手段索引 |
| [curated/bitwise/](curated/bitwise/) | 六个稳定机制页，按问题族组织长期结论 |
| [BITWISE_EVIDENCE_SYNTHESIS.md](BITWISE_EVIDENCE_SYNTHESIS.md) | 第一轮 targeted GitHub evidence 的综合结论 |
| [BITWISE_NEXT.md](BITWISE_NEXT.md) | 下一轮补证队列，只记录缺口和复核顺序 |
| [candidates/bitwise_ledger.csv](candidates/bitwise_ledger.csv) | 重点 claim 的 include/defer/exclude 账本 |
| [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md) | 仓库结构、证据规则、质量门和迭代协议 |

## 文件树分工

```text
VllmWiki/
├── README.md                         # 项目概览、迭代流程和阅读路线
├── BITWISE_DETERMINISTIC.md          # bitwise/deterministic 主线入口
├── BITWISE_EVIDENCE_SYNTHESIS.md     # 第一轮证据综合
├── BITWISE_NEXT.md                   # 下一轮补证队列
├── WIKI_IMPLEMENTATION.md            # 维护规范、质量门与机制页模板
├── curated/
│   ├── bitwise_determinism.md        # bitwise 总览页
│   └── bitwise/                      # 六个可维护机制页
├── candidates/
│   └── bitwise_ledger.csv            # claim 决策账本
├── data/                             # schema、tag、alias、version claim
├── audit/
│   └── manifest.md                   # 数据快照说明
└── scripts/                          # 抓取、抽取、查询、验证脚本
```

仓库外的 `E:\Vllm-Issue\all` 保存 raw / targeted evidence。仓库内被忽略的 `cases/`、`patterns/`、`domains/`、`indexes/`、`evidence/`、`curated/bitwise_review_queue.*`、`audit/iteration_*` 是本地可再生材料，不进入 GitHub 结论层。

## Bitwise 机制页

- [Prefix Cache 等价](curated/bitwise/prefix_cache_equivalence.md)
- [Batch Invariance 与 Kernel Geometry](curated/bitwise/batch_invariance_kernel_geometry.md)
- [并发下的 KV Cache Identity](curated/bitwise/kv_cache_identity_concurrency.md)
- [量化与 Dtype 数值语义](curated/bitwise/quant_dtype_numerical_semantics.md)
- [Deterministic Dispatch 与 Reduction Control](curated/bitwise/deterministic_dispatch_reduction.md)
- [Bitwise 工作的验证契约](curated/bitwise/verification_contracts.md)

## 维护原则

- README 只说明项目整体和迭代方式，不承载完整操作手册。
- `curated/` 中的结论必须能回链到 issue、PR、评论、diff 或本地 targeted evidence。
- `candidates/bitwise_ledger.csv` 记录尚未 fully curated 的 claim，避免候选结论混入机制页。
- 后续新增结论优先更新机制页和 ledger，不新增一次性根目录文档。
