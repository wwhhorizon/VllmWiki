# vllm-project/vllm#6376: [Bug]: llava model gets stuck with RuntimeError: Please increase the max_chunk_bytes parameter.

| 字段 | 值 |
| --- | --- |
| Issue | [#6376](https://github.com/vllm-project/vllm/issues/6376) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | crash;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llava model gets stuck with RuntimeError: Please increase the max_chunk_bytes parameter.

### Issue 正文摘录

### Your current environment I have the following docker compose service running vLLM and llava-hf/llava-v1.6-mistral-7b-hf ``` llava: image: vllm/vllm-openai:latest container_name: vllm-llava runtime: nvidia deploy: resources: reservations: devices: - capabilities: [gpu] volumes: - /data/.cache/huggingface:/root/.cache/huggingface env_file: - .env ports: - "8002:8000" ipc: host command: --model llava-hf/llava-v1.6-mistral-7b-hf --tensor-parallel-size 4 --enforce-eager --gpu-memory-utilization 0.35 ``` I have a service sending 5 parallel requests on the exposed `/v1/chat/completions`, which will seize it with the following error: ``` RuntimeError: len(serialized_obj)=14904693 larger than the allowed value 4194304, Please increase the max_chunk_bytes parameter. ``` After which the container is stuck in a state with 5 requests, where it doesnt accept any new requests: ``` Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 5 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 3.9%, CPU KV cache usage: 0.0%. ``` I must completely tear down the container and start it again to unstuck it. If I adjust my service to be more gentle - sending just...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: llava model gets stuck with RuntimeError: Please increase the max_chunk_bytes parameter. bug ### Your current environment I have the following docker compose service running vLLM and llava-hf/llava-v1.6-mistral-7...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _bytes parameter. bug ### Your current environment I have the following docker compose service running vLLM and llava-hf/llava-v1.6-mistral-7b-hf ``` llava: image: vllm/vllm-openai:latest container_name: vllm-llava runt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: gpu-memory-utilization 0.35 ``` I have a service sending 5 parallel requests on the exposed `/v1/chat/completions`, which will seize it with the following error: ``` RuntimeError: len(serialized_obj)=14904693 larger tha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: -hf/llava-v1.6-mistral-7b-hf ``` llava: image: vllm/vllm-openai:latest container_name: vllm-llava runtime: nvidia deploy: resources: reservations: devices: - capabilities: [gpu] volumes: - /data/.cache/huggingface:/root...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: BgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
