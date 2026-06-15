# vllm-project/vllm#40002: [Bug]: Inconsistent KV Cache reporting and system hang on long context requests (Gemma-4 26B AWQ Int4)

| 字段 | 值 |
| --- | --- |
| Issue | [#40002](https://github.com/vllm-project/vllm/issues/40002) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inconsistent KV Cache reporting and system hang on long context requests (Gemma-4 26B AWQ Int4)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi vLLM team! I encountered two interrelated issues when using the [`gemma-4-26B-A4B-it-AWQ-4bit`](https://huggingface.co/cyankiwi/gemma-4-26B-A4B-it-AWQ-4bit) model with the official Docker image. ### 1. Inconsistent KV Cache Reporting In `vllm/v1/core/kv_cache_utils.py`, there is a discrepancy between the reported `GPU KV cache size` and the `Maximum concurrency` calculation. (not sure whether the issue is caused by swa) **Logs:** ```log vllm | (EngineCore pid=171) INFO 04-15 09:11:57 [kv_cache_utils.py:1319] GPU KV cache size: 79,002 tokens vllm | (EngineCore pid=171) INFO 04-15 09:11:57 [kv_cache_utils.py:1324] Maximum concurrency for 262,144 tokens per request: 3.24x ``` ### 2. System Hang on Long Context Requests When submitting a request with a sequence length of approximately 170k tokens (which is within the max-model-len of 262,144 but exceeds the actual GPU KV cache size of 79,002), the engine hangs: CPU usage spikes to 100% (pinned to a single core) while GPU utilization remains at 0%. Increasing `--renderer-num-workers 12` does not resolve the issue; the workload remains stuck on a single core. --- ### Reproduction (w...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /huggingface.co/cyankiwi/gemma-4-26B-A4B-it-AWQ-4bit) model with the official Docker image. ### 1. Inconsistent KV Cache Reporting In `vllm/v1/core/kv_cache_utils.py`, there is a discrepancy between the reported `GPU KV...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ache reporting and system hang on long context requests (Gemma-4 26B AWQ Int4) bug ### Your current environment ### 🐛 Describe the bug Hi vLLM team! I encountered two interrelated issues when using the [`gemma-4-26B-A4B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nconsistent KV Cache reporting and system hang on long context requests (Gemma-4 26B AWQ Int4) bug ### Your current environment ### 🐛 Describe the bug Hi vLLM team! I encountered two interrelated issues when using the [...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: nconsistent KV Cache reporting and system hang on long context requests (Gemma-4 26B AWQ Int4) bug ### Your current environment ### 🐛 Describe the bug Hi vLLM team! I encountered two interrelated issues when using the [...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Inconsistent KV Cache reporting and system hang on long context requests (Gemma-4 26B AWQ Int4) bug ### Your current environment ### 🐛 Describe the bug Hi vLLM team! I encountered two interrelated issues when usi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
