# vllm-project/vllm#40350: [Bug]: Qwen3.5-397B-A17B-NVFP4 engine hangs (Running≥1, 0 tok/s) under high concurrency on Blackwell GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#40350](https://github.com/vllm-project/vllm/issues/40350) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;fp8;moe;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-397B-A17B-NVFP4 engine hangs (Running≥1, 0 tok/s) under high concurrency on Blackwell GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Under high-concurrency load, the V1 engine silently stops generating tokens for the last in-flight request and never recovers. The API server stays healthy (`/metrics` keeps returning 200 OK), but no new tokens are produced and the request hangs forever until the job is killed externally. **This is NVFP4-specific.** The FP8 build of the same model on the same GPUs never hangs; only the NVFP4 build does. The hang was observed on B200, B300, GB200, and GB300. #### Reproducer ```bash python3 -m vllm.entrypoints.openai.api_server \ --model nvidia/Qwen3.5-397B-A17B-NVFP4 \ --tensor-parallel-size 4 \ --kv-cache-dtype fp8_e4m3 \ --trust-remote-code \ --max-model-len 3072 \ --no-enable-prefix-caching \ --language-model-only \ --async-scheduling \ --attention-backend FLASHINFER \ --enable-expert-parallel \ --quantization modelopt \ --compilation_config.max_cudagraph_capture_size 2048 \ --speculative_config.method mtp \ --speculative_config.num_speculative_tokens 3 \ --host 0.0.0.0 --port 60000 ``` ```bash vllm bench serve \ --backend openai-chat \ --endpoint /v1/chat/completions \ --model nvidia/Qwen3.5-397B-A17B-NVFP4 \ --dataset-name ra...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: d, the V1 engine silently stops generating tokens for the last in-flight request and never recovers. The API server stays healthy (`/metrics` keeps returning 200 OK), but no new tokens are produced and the request hangs...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen3.5-397B-A17B-NVFP4 engine hangs (Running≥1, 0 tok/s) under high concurrency on Blackwell GPUs bug ### Your current environment ### 🐛 Describe the bug Under high-concurrency load, the V1 engine silently stops...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: B-A17B-NVFP4 engine hangs (Running≥1, 0 tok/s) under high concurrency on Blackwell GPUs bug ### Your current environment ### 🐛 Describe the bug Under high-concurrency load, the V1 engine silently stops generating tokens...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: st hangs forever until the job is killed externally. **This is NVFP4-specific.** The FP8 build of the same model on the same GPUs never hangs; only the NVFP4 build does. The hang was observed on B200, B300, GB200, and G...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5-397B-A17B-NVFP4 engine hangs (Running≥1, 0 tok/s) under high concurrency on Blackwell GPUs bug ### Your current environment ### 🐛 Describe the bug Under high-concurrency load, the V1 engine silently stops...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
