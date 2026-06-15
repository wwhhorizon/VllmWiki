# vllm-project/vllm#29166: [Bug]: Granite Speech Illegal Memory Accesses in Parallel Vocab w/ LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#29166](https://github.com/vllm-project/vllm/issues/29166) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Granite Speech Illegal Memory Accesses in Parallel Vocab w/ LoRA

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We have been seeing illegal memory access issues coming out of the call that `VocabParallelEmbeddingWithLoRA` makes to the underlying `_lora_expand_kernel` when some granite speech models, e.g., `ibm-granite/granite-speech-3.3-8b` are run online with chat completions - these models always use a LoRA when audio is present, so in our test runs, LoRA is always used. From initial testing, my current best guess is there may be an edge case somewhere with a specific grid configuration and the multimodal ` ` token somewhere, which is causing things to go out of bounds when it sets the output pointer within the triton kernel, or maybe an edge case with higher lora rank. It's also worth noting that if an example breaks things, it appears to depend on the sequence of requests before it - running the request by itself does not seem to crash the server, but it _does_ seem to put stuff in a bad state by causing outputs after it to be empty, at least in the repro case I have. My current most isolated repro case is: start server with: ```bash VLLM_LOGGING_LEVEL=ERROR CUDA_LAUNCH_BLOCKING=1 vllm serve "ibm-granite/granite-speech-3.3-8b" \ --api-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ` makes to the underlying `_lora_expand_kernel` when some granite speech models, e.g., `ibm-granite/granite-speech-3.3-8b` are run online with chat completions - these models always use a LoRA when audio is present, so...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: , my current best guess is there may be an edge case somewhere with a specific grid configuration and the multimodal ` ` token somewhere, which is causing things to go out of bounds when it sets the output pointer withi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: g]: Granite Speech Illegal Memory Accesses in Parallel Vocab w/ LoRA bug;stale ### Your current environment ### 🐛 Describe the bug We have been seeing illegal memory access issues coming out of the call that `VocabParal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lated repro case is: start server with: ```bash VLLM_LOGGING_LEVEL=ERROR CUDA_LAUNCH_BLOCKING=1 vllm serve "ibm-granite/granite-speech-3.3-8b" \ --api-key "token-abc123" \ --max-model-len 16384 \ --port 8003 \ --enable-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ng things to go out of bounds when it sets the output pointer within the triton kernel, or maybe an edge case with higher lora rank. It's also worth noting that if an example breaks things, it appears to depend on the s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
