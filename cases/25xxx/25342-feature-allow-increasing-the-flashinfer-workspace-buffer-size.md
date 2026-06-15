# vllm-project/vllm#25342: [Feature]: Allow increasing the flashinfer workspace buffer size

| 字段 | 值 |
| --- | --- |
| Issue | [#25342](https://github.com/vllm-project/vllm/issues/25342) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow increasing the flashinfer workspace buffer size

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The flashinfer workspace buffer size is hard coded as `FLASHINFER_WORKSPACE_BUFFER_SIZE = 256 * 1024 * 1024` but I'm seeing buffer overflows: ``` site-packages/flashinfer/data/include/flashinfer/allocator.h:49: Buffer overflow when allocating memory for batch_prefill_tmp_v with size 283115520 and alignment 16, but only 268435456 bytes available in AlignedAllocator. Increase the workspace buffer size. ``` My vllm invocation: ``` VLLM_ATTENTION_BACKEND=FLASHINFER vllm serve cpatonn/GLM-4.5-Air-AWQ \ --dtype float16 \ --rope-scaling '{"rope_type": "yarn", "factor": 2.0, "original_max_position_embeddings": 131072}' \ --max-model-len 262144 \ --kv-cache-dtype fp8_e4m3 \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --kv-cache-memory=26403578572 \ --enable-auto-tool-choice ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: LLM_ATTENTION_BACKEND=FLASHINFER vllm serve cpatonn/GLM-4.5-Air-AWQ \ --dtype float16 \ --rope-scaling '{"rope_type": "yarn", "factor": 2.0, "original_max_position_embeddings": 131072}' \ --max-model-len 262144 \ --kv-c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Allow increasing the flashinfer workspace buffer size feature request;stale ### 🚀 The feature, motivation and pitch The flashinfer workspace buffer size is hard coded as `FLASHINFER_WORKSPACE_BUFFER_SIZE = 25...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Allow increasing the flashinfer workspace buffer size feature request;stale ### 🚀 The feature, motivation and pitch The flashinfer workspace buffer size is hard coded as `FLASHINFER_WORKSPACE_BUFFER_SIZE = 25...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: iginal_max_position_embeddings": 131072}' \ --max-model-len 262144 \ --kv-cache-dtype fp8_e4m3 \ --tool-call-parser glm45 \ --reasoning-parser glm45 \ --kv-cache-memory=26403578572 \ --enable-auto-tool-choice ``` ### Al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
