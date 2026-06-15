# vllm-project/vllm#7751: [Usage]: How do I configure Phi-3-vision for high throughput?

| 字段 | 值 |
| --- | --- |
| Issue | [#7751](https://github.com/vllm-project/vllm/issues/7751) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How do I configure Phi-3-vision for high throughput?

### Issue 正文摘录

### How would you like to use vllm I want to run Phi-3-vision with VLLM to support parallel calls with high throughput. In my setup (openai compatible 0.5.4 VLLM server on HuggingFace Inference Endpoints with Nvidia-L4 24GB GPU), I have set up Phi-3-vision with the following parameters: ``` DISABLE_SLIDING_WINDOW=true DTYPE=bfloat16 ENFORCE_EAGER=true # Tried both true/false GPU_MEMORY_UTILIZATION=0.98 # Tried 0.6-0.99 MAX_MODEL_LEN=3072 # Smallest token length that supports my work MAX_NUM_BATCHED_TOKENS=12288 # Tried 3072-12288 MAX_NUM_SEQS=16 # Tried 2-32 QUANTIZATION=fp8 # Tried fp8 and None TRUST_REMOTE_CODE=true VLLM_ATTENTION_BACKEND=FLASH_ATTN ``` I am running into the issue that no matter what settings I use, adding more concurrent calls is increasing the total inference time linearly; the batching parallelism is not working. For example, running 4 concurrent requests takes 12 seconds, but 1 request by itself takes 3 seconds. The logs show: ``` Avg prompt throughput: 3461 tokens/s, Avg generation throughput: 39.4 tokens/s, Running: 12 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 68.3%, CPU KV cache usage: 0.0% Avg prompt throughput: 0 tokens/s, Avg generati...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: -3-vision with the following parameters: ``` DISABLE_SLIDING_WINDOW=true DTYPE=bfloat16 ENFORCE_EAGER=true # Tried both true/false GPU_MEMORY_UTILIZATION=0.98 # Tried 0.6-0.99 MAX_MODEL_LEN=3072 # Smallest token length...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How do I configure Phi-3-vision for high throughput? usage;stale ### How would you like to use vllm I want to run Phi-3-vision with VLLM to support parallel calls with high throughput. In my setup (openai compa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How do I configure Phi-3-vision for high throughput? usage;stale ### How would you like to use vllm I want to run Phi-3-vision with VLLM to support parallel calls with high throughput. In my setup (openai compa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: TIZATION=fp8 # Tried fp8 and None TRUST_REMOTE_CODE=true VLLM_ATTENTION_BACKEND=FLASH_ATTN ``` I am running into the issue that no matter what settings I use, adding more concurrent calls is increasing the total inferen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: alse GPU_MEMORY_UTILIZATION=0.98 # Tried 0.6-0.99 MAX_MODEL_LEN=3072 # Smallest token length that supports my work MAX_NUM_BATCHED_TOKENS=12288 # Tried 3072-12288 MAX_NUM_SEQS=16 # Tried 2-32 QUANTIZATION=fp8 # Tried fp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
