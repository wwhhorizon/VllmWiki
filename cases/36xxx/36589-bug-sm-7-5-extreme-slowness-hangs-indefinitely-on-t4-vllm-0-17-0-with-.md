# vllm-project/vllm#36589: [Bug]: SM 7.5 extreme slowness hangs indefinitely on T4 (vllm 0.17.0 with Qwen3.5-27B)

| 字段 | 值 |
| --- | --- |
| Issue | [#36589](https://github.com/vllm-project/vllm/issues/36589) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SM 7.5 extreme slowness hangs indefinitely on T4 (vllm 0.17.0 with Qwen3.5-27B)

### Issue 正文摘录

### Your current environment vllm 0.17.0 qwen3.5-27B tesla T4 x 4 ### 🐛 Describe the bug After applying the suggested fix from [#36357](https://github.com/vllm-project/vllm/issues/36357) (fallback to TORCH_SDPA for multimodal encoder on SM ```text qwen3.5-27b | (APIServer pid=1) INFO: Started server process [1] qwen3.5-27b | (APIServer pid=1) INFO: Waiting for application startup. qwen3.5-27b | (APIServer pid=1) INFO: Application startup complete. qwen3.5-27b | (APIServer pid=1) INFO: 172.21.0.1:55138 - "POST /v1/chat/completions HTTP/1.1" 200 OK qwen3.5-27b | (APIServer pid=1) INFO 03-10 02:33:38 [loggers.py:259] Engine 000: Avg prompt throughput: 1.7 tokens/s, Avg generation throughput: 5.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 10.3%, Prefix cache hit rate: 0.0% qwen3.5-27b | (APIServer pid=1) INFO 03-10 02:33:48 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 23.4 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 10.3%, Prefix cache hit rate: 0.0% qwen3.5-27b | (APIServer pid=1) INFO 03-10 02:33:58 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 23.4...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Bug]: SM 7.5 extreme slowness hangs indefinitely on T4 (vllm 0.17.0 with Qwen3.5-27B) bug ### Your current environment vllm 0.17.0 qwen3.5-27B tesla T4 x 4 ### 🐛 Describe the bug After applying the suggested fix from [#...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: SM 7.5 extreme slowness hangs indefinitely on T4 (vllm 0.17.0 with Qwen3.5-27B) bug ### Your current environment vllm 0.17.0 qwen3.5-27B tesla T4 x 4 ### 🐛 Describe the bug After applying the suggested fix from [...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 5.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 10.3%, Prefix cache hit rate: 0.0% qwen3.5-27b | (APIServer pid=1) INFO 03-10 02:33:48 [loggers.py:259] Engine 000: Avg prompt thr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -10 02:38:31 [shm_broadcast.py:548] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Started server process [1] qwen3.5-27b | (APIServer pid=1) INFO: Waiting for application startup. qwen3.5-27b | (APIServer pid=1) INFO: Application startup complete. qwen3.5-27b | (APIServer pid=1) INFO: 172.21.0.1:5513...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
