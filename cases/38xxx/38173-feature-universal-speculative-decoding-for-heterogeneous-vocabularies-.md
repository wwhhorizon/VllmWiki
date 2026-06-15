# vllm-project/vllm#38173: [Feature]: Universal Speculative Decoding for Heterogeneous Vocabularies (TLI / Token-Level Intersection)

| 字段 | 值 |
| --- | --- |
| Issue | [#38173](https://github.com/vllm-project/vllm/issues/38173) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Universal Speculative Decoding for Heterogeneous Vocabularies (TLI / Token-Level Intersection)

### Issue 正文摘录

### The feature, motivation and pitch ## The feature, motivation and pitch This feature adds support for **speculative decoding with heterogeneous (mismatched) vocabularies**, enabling any two models from different families — or even different tokenizer versions — to be paired as target + draft without requiring identical vocabularies. ### The Problem Today vLLM currently requires the draft model to share the exact same vocabulary as the target model. This severely limits drafter selection and often necessitates training a dedicated draft model from scratch. ### Proposed Solution: Token-Level Intersection (TLI) We implement the **TLI (Token-Level Intersection)** algorithm from the ICML 2025 oral paper: > **Accelerating LLM Inference with Lossless Speculative Decoding Algorithms for Heterogeneous Vocabularies** > Nadav Timor, Jonathan Mamou, Daniel Korat, Moshe Berchansky, Gaurav Jain, Oren Pereg, Moshe Wasserblat, David Harel > https://arxiv.org/abs/2502.05202 The key idea: 1. Compute the **token-level intersection** between the target and draft vocabularies via text normalization 2. Constrain the draft model to only propose tokens present in the intersection 3. Map proposed token...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: laries**, enabling any two models from different families — or even different tokenizer versions — to be paired as target + draft without requiring identical vocabularies.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Universal Speculative Decoding for Heterogeneous Vocabularies (TLI / Token-Level Intersection) feature request ### The feature, motivation and pitch ## The feature, motivation and pitch
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ing any two models from different families — or even different tokenizer versions — to be paired as target + draft without requiring identical vocabularies.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: This feature adds support for **speculative decoding with heterogeneous (mismatched) vocabularies**, enabling any two models from different families — or even different tokenizer versions — to be
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is feature adds support for **speculative decoding with heterogeneous (mismatched) vocabularies**, enabling any two models from different families — or even different tokenizer versions — to be

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
