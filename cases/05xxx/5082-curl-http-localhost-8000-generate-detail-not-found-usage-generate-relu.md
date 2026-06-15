# vllm-project/vllm#5082: curl http://localhost:8000/generate {"detail":"Not Found"}[Usage] generate relu can not ues

| 字段 | 值 |
| --- | --- |
| Issue | [#5082](https://github.com/vllm-project/vllm/issues/5082) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 41; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> curl http://localhost:8000/generate {"detail":"Not Found"}[Usage] generate relu can not ues

### Issue 正文摘录

run with python -m vllm.entrypoints.openai.api_server --model vicuna-7b-v1.5 --trust-remote-code curl http://localhost:8000/generate -d '{"prompt": "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:write a bubble sort using python\n\n### Response:","max_tokens":256}' INFO: 127.0.0.1:55766 - "POST /generate HTTP/1.1" 404 Not Found INFO 05-28 15:37:03 metrics.py:334] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO: 127.0.0.1:45622 - "GET /generate HTTP/1.1" 404 Not Found python cli.py Prompt: 'San Francisco is a' Traceback (most recent call last): File "/root/autodl-tmp/chat-main/vllm_cli.py", line 79, in output = get_response(response) File "/root/autodl-tmp/chat-main/vllm_cli.py", line 46, in get_response output = data["text"] KeyError: 'text' ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: "GET /generate HTTP/1.1" 404 Not Found python cli.py Prompt: 'San Francisco is a' Traceback (most recent call last): File "/root/autodl-tmp/chat-main/vllm_cli.py", line 79, in output = get_response(response) File "/root...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO: 127.0.0.1:45622 - "GET /generate HTTP/1.1" 404 Not Found python cli.py Prompt: 'San Francisco...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: an not ues usage run with python -m vllm.entrypoints.openai.api_server --model vicuna-7b-v1.5 --trust-remote-code curl http://localhost:8000/generate -d '{"prompt": "Below is an instruction that describes a task. Write...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hat describes a task. Write a response that appropriately completes the request.\n\n### Instruction:write a bubble sort using python\n\n### Response:","max_tokens":256}' INFO: 127.0.0.1:55766 - "POST /generate HTTP/1.1"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e HTTP/1.1" 404 Not Found INFO 05-28 15:37:03 metrics.py:334] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
