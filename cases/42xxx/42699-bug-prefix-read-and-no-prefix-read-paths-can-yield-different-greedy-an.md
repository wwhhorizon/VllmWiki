# vllm-project/vllm#42699: [Bug]: Prefix-read and no-prefix-read paths can yield different greedy answers for the same prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#42699](https://github.com/vllm-project/vllm/issues/42699) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix-read and no-prefix-read paths can yield different greedy answers for the same prompt

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a deterministic wrong-answer issue in a reproducible default-backend `Qwen2` setup. With the same visible prompt text and the same deterministic engine settings, changing only whether the probe request is allowed to read from the prefix cache can flip the model's first lexical interpretation between: - `A` = `herring` - `B` = `her ring` Here `A` and `B` are not analyst labels. They are the exact two answer choices embedded in the probe prompt: ```text Choices: A = the fish word herring B = the jewelry phrase her ring Respond with A or B only. Answer: ``` The important point is that the visible probe text stays the same, but the probe request switches between a prefix-read path and a no-prefix-read full-recompute path. In this reproduced default-backend case, that difference lands near the `her | ring` word boundary, so the first greedy sampled wordform flips between `herring` and `her ring`. That lexical split is not cosmetic. In the fuller semantic reproduction notes, it propagates i...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: the same deterministic engine settings, changing only whether the probe request is allowed to read from the prefix cache can flip the model's first lexical interpretation between: - `A` = `herring` - `B` = `her ring` He...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: be the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a deterministic wrong-answer issue in a reproducible default-backend `Qwen2` se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a deterministic wrong-a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: .1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a deterministic wrong-answer issue in a reproducible default-backend `Qwen2` setup. With the same visible pro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a deterministic wrong-answer issue in a reproduc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
