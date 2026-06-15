# vllm-project/vllm#39479: [torch.compile] config hashing refactor follow-ups

| 字段 | 值 |
| --- | --- |
| Issue | [#39479](https://github.com/vllm-project/vllm/issues/39479) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [torch.compile] config hashing refactor follow-ups

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### MOTIVATION. [PR #26468](https://github.com/vllm-project/vllm/pull/26468) moved vLLM config hashing toward an opt-out model so new compilation-relevant config fields are less likely to be accidentally omitted from torch.compile cache keys. This issue tracks the follow-ups and to-dos. ## TODOs 1. Refactor all locations of `compute_hash` to `compile_factors`. `compute_hash` isn’t the right name because real computation of the hash is actually done by `utils.hash_factors`. 2. before calling `normalize value` in `get_compile_factors`, it needs to check if .compile_factors exists on the subobject. This allows us to avoid handling `PassConfig` specially as in the case for compilation.py 4. Uniform use of `normalize_value` & `hash_factors` across configs with a compute_hash function. 5. address this comment: [comment here](https://github.com/vllm-project/vllm/pull/26468#discussion_r2545031784) 6. Create a shared helper instead of inlining both `_compute_code_hash` and `compilation_config_hash_factors` 7. Refactor all locations of `compute_hash` to `compile_factors` 8. Follow up on docstrings not being up-to date in the opt-out configs 9. typing...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [torch.compile] config hashing refactor follow-ups help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch ### MOTIVATION. [PR #26468](https://github.com/vllm-project/vllm/pull/26468) moved...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [torch.compile] config hashing refactor follow-ups help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch ### MOTIVATION. [PR #26468](https://github.com/vllm-project/vllm/pull/26468) moved...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: always print hashed configs into cache_key_factors.json ## CC List. @ProExpertProg @zou3519 @hmellor ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make su...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: config hashing refactor follow-ups help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch ### MOTIVATION. [PR #26468](https://github.com/vllm-project/vllm/pull/26468) moved vLLM config hash...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
