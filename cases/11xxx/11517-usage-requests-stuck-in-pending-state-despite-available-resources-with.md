# vllm-project/vllm#11517: [Usage]: Requests stuck in pending state despite available resources with tensor parallel size 8

| 字段 | 值 |
| --- | --- |
| Issue | [#11517](https://github.com/vllm-project/vllm/issues/11517) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Requests stuck in pending state despite available resources with tensor parallel size 8

### Issue 正文摘录

### Your current environment ### Description I'm experiencing an issue where requests are getting stuck in the pending state despite having available GPU resources. The metrics show a consistent pattern where only 1 request is running while 3 requests remain pending, with very low GPU KV cache usage (around 3-4%). ### Environment - vLLM version: [please specify] - Model: Custom model at `/Qwen/Qwen2.5-32B-Instruct` - Hardware: [please specify GPU configuration] - Command used: ```python python3 -m vllm.entrypoints.openai.api_server \ --port 7071 \ --model /Qwen/Qwen2.5-32B-Instruct \ --trust-remote-code \ --tensor-parallel-size 8 \ --gpu-memory-utilization 0.8 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --max-model-len 32768 \ --enable-lora \ --max-seq-len-to-capture 32768 \ --max-lora-rank 64 2024-12-20 15:18:19 - vllm.executor.distributed_gpu_executor - INFO - # GPU blocks: 50231, # CPU blocks: 8192 2024-12-20 15:18:19 - vllm.executor.distributed_gpu_executor - INFO - Maximum concurrency for 32768 tokens per request: 24.53x 2024-12-23 18:28:10 - vllm.engine.metrics - INFO - Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 45.7 tokens/s, Running: 1 re...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: usage (around 3-4%). ### Environment - vLLM version: [please specify] - Model: Custom model at `/Qwen/Qwen2.5-32B-Instruct` - Hardware: [please specify GPU configuration] - Command used: ```python python3 -m vllm.entryp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l size 8 usage ### Your current environment ### Description I'm experiencing an issue where requests are getting stuck in the pending state despite having available GPU resources. The metrics show a consistent pattern w...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 1 request is running while 3 requests remain pending, with very low GPU KV cache usage (around 3-4%). ### Environment - vLLM version: [please specify] - Model: Custom model at `/Qwen/Qwen2.5-32B-Instruct` - Hardware: [p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 4-12-20 15:18:19 - vllm.executor.distributed_gpu_executor - INFO - # GPU blocks: 50231, # CPU blocks: 8192 2024-12-20 15:18:19 - vllm.executor.distributed_gpu_executor - INFO - Maximum concurrency for 32768 tokens per r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Requests stuck in pending state despite available resources with tensor parallel size 8 usage ### Your current environment ### Description I'm experiencing an issue where requests are getting stuck in the pendi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
