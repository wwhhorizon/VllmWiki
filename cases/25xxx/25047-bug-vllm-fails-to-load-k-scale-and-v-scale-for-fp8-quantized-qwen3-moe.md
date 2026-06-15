# vllm-project/vllm#25047: [Bug]: vLLM fails to load k_scale and v_scale for FP8 quantized Qwen3-MOE models

| 字段 | 值 |
| --- | --- |
| Issue | [#25047](https://github.com/vllm-project/vllm/issues/25047) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;moe;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM fails to load k_scale and v_scale for FP8 quantized Qwen3-MOE models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Bug Description When loading a `Qwen3-30B-A3B` model that has been quantized to FP8 (W8A8 weights + FP8 KV cache) using `llm-compressor` (v0.7.1), vLLM fails to correctly load the `k_scale` and `v_scale` tensors from the checkpoint. As a result, vLLM issues warnings indicating that it is falling back to a default KV cache scaling factor of 1.0, which can negatively impact model accuracy. **Observed Warnings:** ```text (VllmWorker TP0 pid=170681) WARNING 09-16 19:47:32 [kv_cache.py:86] Checkpoint does not provide a q scaling factor. Setting it to k_scale. This only m atters for the flash-attn backend. (VllmWorker TP0 pid=170681) WARNING 09-16 19:47:32 [kv_cache.py:99] Using KV cache scaling factor 1.0 for fp8_e4m3. This may cause accuracy issues. Please make sure k/v_scale scaling factors are available in the fp8 checkpoint. ```` ### Steps to Reproduce 1. Quantize the `Qwen/Qwen3-30B-A3B--e34b3e9-C10` model using `llm-compressor==0.7.1` with `FP8 W8A8` and `FP8 KV cache` enabled. 2. Launch the vLLM OpenAI API server with the quantized model using the following command: ```shell python3 -m vllm.entrypoints.openai.api_server \ -...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: vLLM fails to load k_scale and v_scale for FP8 quantized Qwen3-MOE models bug;stale ### Your current environment ### 🐛 Describe the bug ### Bug Description When loading a `Qwen3-30B-A3B` model that has been quant...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization cache;cuda;fp8;moe;quantization;triton build_error dtyp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ing factor. Setting it to k_scale. This only m atters for the flash-attn backend. (VllmWorker TP0 pid=170681) WARNING 09-16 19:47:32 [kv_cache.py:99] Using KV cache scaling factor 1.0 for fp8_e4m3. This may cause accura...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: efault KV cache scaling factor of 1.0, which can negatively impact model accuracy. **Observed Warnings:** ```text (VllmWorker TP0 pid=170681) WARNING 09-16 19:47:32 [kv_cache.py:86] Checkpoint does not provide a q scali...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
