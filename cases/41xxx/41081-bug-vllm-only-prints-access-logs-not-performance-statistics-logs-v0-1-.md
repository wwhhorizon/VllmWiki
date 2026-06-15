# vllm-project/vllm#41081: [Bug]:  vLLM only prints access logs, not performance statistics logs (v0.1.dev15830+g8d599d76a with deepseek-V4-flash)

| 字段 | 值 |
| --- | --- |
| Issue | [#41081](https://github.com/vllm-project/vllm/issues/41081) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;fp8;moe |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  vLLM only prints access logs, not performance statistics logs (v0.1.dev15830+g8d599d76a with deepseek-V4-flash)

### Issue 正文摘录

### Your current environment Environment Information: • vLLM version: 0.1.dev15830+g8d599d76a • Model: deepseek-V4-flash • CUDA version: cu129 • GPU: H800 ### 🐛 Describe the bug Description: When I run the vLLM API server with version 0.1.dev15830+g8d599d76a and the deepseek-V4-flash model, the logs only show basic access logs like INFO: 127.0.0.1:32768 0 "POST v1/completions HTTP/1.1" 200 OK But I'm not seeing the periodic performance statistics logs that include throughput, GPU KV cache usage, etc., for example: 13:57:45 Avg prompt throughput: 2598.6 tokens/s, Avg generation throughput: 1684.2 tokens/s, Running: 2 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.3%, Prefix cache hit rate: 96.9% 13:57:55 Avg prompt throughput: 83.6 tokens/s, Avg generation throughput: 1.8 tokens/s, Running: 11 reqs, Waiting: 0 reqs, GPU KV cache usage: 1.3%, Prefix cache hit rate: 96.9% 13:58:05 Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 11 reqs, Waiting: 0 reqs, GPU KV cache usage: 1.3%, Prefix cache hit rate: 96.9% start code: VLLM_ENGINE_READY_TIMEOUT_S=1200 nohup vllm serve /mnt/algorithms/DeepSeek-V4-Flash --port 8000 --served-model-name DEEPSEEK-V4-28...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: flash) bug ### Your current environment Environment Information: • vLLM version: 0.1.dev15830+g8d599d76a • Model: deepseek-V4-flash • CUDA version: cu129 • GPU: H800 ### 🐛 Describe the bug Description: When I run the vL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ed-model-name DEEPSEEK-V4-284B-FLASH-TEST --trust-remote-code --kv-cache-dtype fp8 --block-size 256 --enable-expert-parallel --data-parallel-size 8 --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE","custom_op...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ng the periodic performance statistics logs that include throughput, GPU KV cache usage, etc., for example: 13:57:45 Avg prompt throughput: 2598.6 tokens/s, Avg generation throughput: 1684.2 tokens/s, Running: 2 reqs, W...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: with deepseek-V4-flash) bug ### Your current environment Environment Information: • vLLM version: 0.1.dev15830+g8d599d76a • Model: deepseek-V4-flash • CUDA version: cu129 • GPU: H800 ### 🐛 Describe the bug Description:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 6 tokens/s, Avg generation throughput: 1684.2 tokens/s, Running: 2 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.3%, Prefix cache hit rate: 96.9% 13:57:55 Avg prompt throughput: 83.6 tokens/s, Avg generation throughput:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
