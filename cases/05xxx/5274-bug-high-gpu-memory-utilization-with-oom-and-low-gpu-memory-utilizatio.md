# vllm-project/vllm#5274: [Bug]: high gpu_memory_utilization with 'OOM' and low gpu_memory_utilization with 'No available memory for the cache blocks'

| 字段 | 值 |
| --- | --- |
| Issue | [#5274](https://github.com/vllm-project/vllm/issues/5274) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: high gpu_memory_utilization with 'OOM' and low gpu_memory_utilization with 'No available memory for the cache blocks'

### Issue 正文摘录

### Your current environment v100 32G * 8 ### 🐛 Describe the bug I tried to run a 32B model with lora adapters and test different GPU_MEMORY_UTILIZATION. When `gpu_memory_utilization = 0.9` , it came with OOM. When `gpu_memory_utilization = 0.8` , it came with 'No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine.' Does it mean that I need to find a suitable value for `gpu_memory_utilization` or is there any other things going wrong?

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: high gpu_memory_utilization with 'OOM' and low gpu_memory_utilization with 'No available memory for the cache blocks' bug;stale ### Your current environment v100 32G * 8 ### 🐛 Describe the bug I tried to run a 32...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ' and low gpu_memory_utilization with 'No available memory for the cache blocks' bug;stale ### Your current environment v100 32G * 8 ### 🐛 Describe the bug I tried to run a 32B model with lora adapters and test differen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: environment v100 32G * 8 ### 🐛 Describe the bug I tried to run a 32B model with lora adapters and test different GPU_MEMORY_UTILIZATION. When `gpu_memory_utilization = 0.9` , it came with OOM. When `gpu_memory_utilizati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: u_memory_utilization with 'No available memory for the cache blocks' bug;stale ### Your current environment v100 32G * 8 ### 🐛 Describe the bug I tried to run a 32B model with lora adapters and test different GPU_MEMORY...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ## 🐛 Describe the bug I tried to run a 32B model with lora adapters and test different GPU_MEMORY_UTILIZATION. When `gpu_memory_utilization = 0.9` , it came with OOM. When `gpu_memory_utilization = 0.8` , it came with '...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
