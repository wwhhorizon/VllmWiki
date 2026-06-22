# Glossary

状态：single source of truth。
作用：统一定义 VllmWiki 中反复出现的维护术语和 bitwise/deterministic 术语。

## 维护状态

| 术语 | 定义 |
| --- | --- |
| `candidate` | 来自 raw body、表格提示、关键词或自动分类，尚未精读，不能当作最终结论。 |
| `reviewed` | 已阅读 issue/PR 主要材料，但根因、修复、验证或边界仍有缺口。 |
| `curated` | 根因、修复、验证和边界都有证据支撑，可作为稳定 wiki lesson。 |
| `defer` | 相关但证据不足、范围过宽或还缺 direct closure，等待后续复核。 |
| `blocked` | 缺少评论、PR detail、diff、测试或外部证据，当前无法 promotion。 |
| `include_with_boundary` | 机制方向可用，但 landed 状态、review risk、测试矩阵或适用边界仍需显式保留。 |
| `unresolved_review_risk` | PR 或 patch 有未闭环 review 风险，只能作为边界或待复核项。 |

## Bitwise / Deterministic 术语

| 术语 | 定义 |
| --- | --- |
| `deterministic` | 在声明的输入、配置、硬件和执行路径下，行为可重复；不必天然等于跨 batch bitwise invariant。 |
| `bitwise` | 输出在 bit 层完全一致，例如 `torch.equal`、bit-view equality、`rtol=0, atol=0`。 |
| `batch-invariant` | 同一请求的输出不因同 batch 的其他请求、batch size、M 维或调度组合改变。通常比普通 deterministic 更严格。 |
| `semantic equivalence` | 最终回答语义相似或可接受；只能作为补充，不能单独支撑 bitwise/deterministic claim。 |
| `strict tolerance` | 使用明确的数值容忍度比较张量，适合部分低精度路径，但不能自动升级为 bitwise equality。 |
| `token equality` | `temperature=0` 等条件下输出 token 序列一致，可作为用户可见 correctness gate。 |
| `logprob ranking` | logits/logprobs 的排序或 beam ranking 稳定；文本相同不代表 ranking 一定稳定。 |
| `KV identity` | KV cache 内容、block table、slot mapping、metadata 和生命周期身份必须匹配对应请求。 |
| `metadata identity` | CUDA graph/persistent buffer、attention metadata、adapter id、cache key 等非 tensor payload 的身份必须稳定。 |

## 固定原则

固定维护原则只在 [维护规则](maintenance.md) 中完整展开。本文只维护术语定义，避免规则在多处漂移。
