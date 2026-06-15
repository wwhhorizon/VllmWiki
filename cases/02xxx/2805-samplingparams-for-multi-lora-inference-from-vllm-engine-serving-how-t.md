# vllm-project/vllm#2805: SamplingParams for multi-lora inference from vllm engine serving: how to use?

| 字段 | 值 |
| --- | --- |
| Issue | [#2805](https://github.com/vllm-project/vllm/issues/2805) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> SamplingParams for multi-lora inference from vllm engine serving: how to use?

### Issue 正文摘录

Hi, I'm using multi-lora inference with command `tritonserver --model-store /workspace/vllm_workspace/model_repository` and `model.json` config like this: ``` { "model":"/path/to/backbone/", "disable_log_requests": "true", "gpu_memory_utilization": 0.8, "tensor_parallel_size": 2, "block_size": 16, "enable_lora": "true", "max_lora_rank": 16, "max_tokens":512 } ``` I want to increase my generate length, how should I use this and other `SamplingParams`?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: to use? Hi, I'm using multi-lora inference with command `tritonserver --model-store /workspace/vllm_workspace/model_repository` and `model.json` config like this: ``` { "model":"/path/to/backbone/", "disable_log_request...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ne serving: how to use? Hi, I'm using multi-lora inference with command `tritonserver --model-store /workspace/vllm_workspace/model_repository` and `model.json` config like this: ``` { "model":"/path/to/backbone/", "dis...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , "gpu_memory_utilization": 0.8, "tensor_parallel_size": 2, "block_size": 16, "enable_lora": "true", "max_lora_rank": 16, "max_tokens":512 } ``` I want to increase my generate length, how should I use this and other `Sa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: fig like this: ``` { "model":"/path/to/backbone/", "disable_log_requests": "true", "gpu_memory_utilization": 0.8, "tensor_parallel_size": 2, "block_size": 16, "enable_lora": "true", "max_lora_rank": 16, "max_tokens":512...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
