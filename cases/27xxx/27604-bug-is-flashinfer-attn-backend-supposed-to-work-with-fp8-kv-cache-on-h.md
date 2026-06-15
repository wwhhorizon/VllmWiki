# vllm-project/vllm#27604: [Bug]: Is Flashinfer Attn backend supposed to work with FP8 KV cache on Hopper?

| 字段 | 值 |
| --- | --- |
| Issue | [#27604](https://github.com/vllm-project/vllm/issues/27604) |
| 状态 | open |
| 标签 | bug;stale;nvidia |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Is Flashinfer Attn backend supposed to work with FP8 KV cache on Hopper?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using FlashInfer Attn backend works well with BF16 KV Cache, but it fails when using FP8. Is this supposed to work on SM90, or was this never supported? Example ``` export VLLM_ATTENTION_BACKEND="FLASHINFER" python -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-3.1-8B-Instruct \ --kv-cache-dtype "fp8" ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Is Flashinfer Attn backend supposed to work with FP8 KV cache on Hopper? bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug Using FlashInfer Attn backend works well with BF16 KV Cache, but it fa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Is Flashinfer Attn backend supposed to work with FP8 KV cache on Hopper? bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug Using FlashInfer Attn backend works well with BF16 KV Cache, but it fa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Is Flashinfer Attn backend supposed to work with FP8 KV cache on Hopper? bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug Using FlashInfer Attn backend works well with BF16 KV Cache, but it fa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculativ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lashinfer Attn backend supposed to work with FP8 KV cache on Hopper? bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug Using FlashInfer Attn backend works well with BF16 KV Cache, but it fails when us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
