# vllm-project/vllm#20987: [Feature]: Being able to explicitly ask vllm instance to RAM-offload or release to the driver used VRAM (KV cache, model weights, etc)

| 字段 | 值 |
| --- | --- |
| Issue | [#20987](https://github.com/vllm-project/vllm/issues/20987) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Being able to explicitly ask vllm instance to RAM-offload or release to the driver used VRAM (KV cache, model weights, etc)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This can be useful in setups where vllm instance is run a separate process co-located on the same GPU with the main learning GRPO process: - https://github.com/vllm-project/vllm/pull/15354#issuecomment-3073492044 For avoiding OOMs it's useful to be able to control the amount of VRAM taken by the vllm instance host process and be able to RAM-offload or directly replace with "meta"-device: 1. Model weights 2. KV cache E.g. being able to do sth in the style `myvllm = vllm.LLM(...); ...; myvllm.offload_model_weights_to_ram(); myvllm.deallocate_kv_cache()` (and being able to do the same commands via RPC) --- Also, in these settings it's very useful to be able to query exactly the VRAM usage (maybe in the style of https://github.com/vllm-project/vllm/pull/17538/files) And maybe even return some info on used VRAM/caches in the generation responses. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Feature]: Being able to explicitly ask vllm instance to RAM-offload or release to the driver used VRAM (KV cache, model weights, etc) feature request;stale ### 🚀 The feature, motivation and pitch This can be useful in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r release to the driver used VRAM (KV cache, model weights, etc) feature request;stale ### 🚀 The feature, motivation and pitch This can be useful in setups where vllm instance is run a separate process co-located on the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Being able to explicitly ask vllm instance to RAM-offload or release to the driver used VRAM (KV cache, model weights, etc) feature request;stale ### 🚀 The feature, motivation and pitch This can be useful in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lm instance to RAM-offload or release to the driver used VRAM (KV cache, model weights, etc) feature request;stale ### 🚀 The feature, motivation and pitch This can be useful in setups where vllm instance is run a separa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
