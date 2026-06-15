# vllm-project/vllm#22621: [Bug]: Latency spikes Issue

| 字段 | 值 |
| --- | --- |
| Issue | [#22621](https://github.com/vllm-project/vllm/issues/22621) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;fp8;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Latency spikes Issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have used model **meta-llama/Meta-Llama-3-3B-Instruct** customization for our TTS model. but problem when i load test using fixed character length sentence(165 character) then sudden latency spikes and another run latency remaining same i have tested vllm version 0.8.3 and 0.9.2 also. but same problem found. here i have share my configuration of vllm, ``` python max_model_len = 1280 min_tokens=10 frequency_penalty = 0.3 local_files_only = False engine_kwargs = { # quantization: Enables FP8 quantization for model weights. While 'fp8' can reduce memory and increase speed, # simple per-tensor FP8 might not yield optimal performance or could degrade quality due to dynamic scale calculations or outlier issues.[9, 10] # For optimal quality, consider calibrated scales or PTPC-FP8 (on AMD ROCm).[11, 12] "quantization": "fp8", #kv_cache_dtype: Storing Key-Value (KV) cache data in FP8 significantly enhances memory efficiency, # effectively doubling the maximum token capacity within the same memory footprint.[6, 7, 8] # This directly boosts the number of concurrent requests. Supported on CUDA 11.8+ and ROCm.[7] "kv_cache_dtype": "fp8", "g...

## 现有链接修复摘要

#4096 [Frontend] Entrypoint for hosting local Kobold Lite chat interface

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: nalty = 0.3 local_files_only = False engine_kwargs = { # quantization: Enables FP8 quantization for model weights. While 'fp8' can reduce memory and increase speed, # simple per-tensor FP8 might not yield optimal perfor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: latency spikes and another run latency remaining same i have tested vllm version 0.8.3 and 0.9.2 also. but same problem found. here i have share my configuration of vllm, ``` python max_model_len = 1280 min_tokens=10 fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: # For optimal quality, consider calibrated scales or PTPC-FP8 (on AMD ROCm).[11, 12] "quantization": "fp8", #kv_cache_dtype: Storing Key-Value (KV) cache data in FP8 significantly enhances memory efficiency, # effective...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: le ### Your current environment ### 🐛 Describe the bug I have used model **meta-llama/Meta-Llama-3-3B-Instruct** customization for our TTS model. but problem when i load test using fixed character length sentence(165 ch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Latency spikes Issue bug;stale ### Your current environment ### 🐛 Describe the bug I have used model **meta-llama/Meta-Llama-3-3B-Instruct** customization for our TTS model. but problem when i load test using fix...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4096](https://github.com/vllm-project/vllm/pull/4096) | mentioned | 0.45 | [Frontend] Entrypoint for hosting local Kobold Lite chat interface | ptimal throughput.[15] "max_num_batched_tokens":8192, # 8192, #4096, # set to a value > 2048 # tokenizer_mode: controls the tokenizer implementation. "auto" attempts to |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
