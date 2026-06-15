# vllm-project/vllm#29531: [Bug]: FP8 KV Cache fails for google/gemma-3-1b-it on Hopper with backend FlashInfer

| 字段 | 值 |
| --- | --- |
| Issue | [#29531](https://github.com/vllm-project/vllm/issues/29531) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 KV Cache fails for google/gemma-3-1b-it on Hopper with backend FlashInfer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash VLLM_ATTENTION_BACKEND=FLASHINFER vllm bench latency --model google/gemma-3-1b-it --enforce-eager --kv-cache-dtype fp8 ``` Brief summary of the environment: - vLLM: 0.11.2 - flashinfer: 0.5.2 - cuda: 12.8 - torch: 2.9.0 [error.log](https://github.com/user-attachments/files/23778443/error.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: FP8 KV Cache fails for google/gemma-3-1b-it on Hopper with backend FlashInfer bug;stale ### Your current environment ### 🐛 Describe the bug ```bash VLLM_ATTENTION_BACKEND=FLASHINFER vllm bench latency --model goo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 KV Cache fails for google/gemma-3-1b-it on Hopper with backend FlashInfer bug;stale ### Your current environment ### 🐛 Describe the bug ```bash VLLM_ATTENTION_BACKEND=FLASHINFER vllm bench latency --model goo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: FP8 KV Cache fails for google/gemma-3-1b-it on Hopper with backend FlashInfer bug;stale ### Your current environment ### 🐛 Describe the bug ```bash VLLM_ATTENTION_BACKEND=FLASHINFER vllm bench latency --model goo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: FP8 KV Cache fails for google/gemma-3-1b-it on Hopper with backend FlashInfer bug;stale ### Your current environment ### 🐛 Describe the bug ```bash VLLM_ATTENTION_BACKEND=FLASHINFER vllm bench latency --model goo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
