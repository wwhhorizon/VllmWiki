# vllm-project/vllm#2752: vLLM ignores my requests when I increase the number of concurrent requests

| 字段 | 值 |
| --- | --- |
| Issue | [#2752](https://github.com/vllm-project/vllm/issues/2752) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM ignores my requests when I increase the number of concurrent requests

### Issue 正文摘录

I am using a runpod container to run vLLM. Template: runpod/pytorch:2.1.1-py3.10-cuda12.1.1-devel-ubuntu22.04 GPU Cloud: 1 x RTX 3090 | 12 vCPU 31 GB RAM It works perfectly fine when I send 9 concurrent requests but it starts to hang when I increase it to 10. `python -m vllm.entrypoints.openai.api_server --model openchat/openchat_3.5 --tensor-parallel-size 1` ``` ... INFO: 127.0.0.1:46228 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:46230 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 02-05 04:53:20 async_llm_engine.py:111] Finished request cmpl-672a8058f6cb4d1d8f5ba5397af93575. INFO 02-05 04:53:20 async_llm_engine.py:111] Finished request cmpl-4314994fe17a4b708bdbc0570668107b. INFO 02-05 04:53:20 async_llm_engine.py:111] Finished request cmpl-85089ac09b6241f781d49b2b05fec1c6. INFO 02-05 04:53:20 async_llm_engine.py:111] Finished request cmpl-b66387e22ebb4b33a010835b5d31f499. INFO 02-05 04:53:21 llm_engine.py:706] Avg prompt throughput: 1137.2 tokens/s, Avg generation throughput: 193.7 tokens/s, Running: 5 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 4.2%, CPU KV cache usage: 0.0% INFO 02-05 04:53:21 async_llm_engine.py:111] Finished request cmp...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng a runpod container to run vLLM. Template: runpod/pytorch:2.1.1-py3.10-cuda12.1.1-devel-ubuntu22.04 GPU Cloud: 1 x RTX 3090 | 12 vCPU 31 GB RAM It works perfectly fine when I send 9 concurrent requests but it starts t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: vLLM ignores my requests when I increase the number of concurrent requests I am using a runpod container to run vLLM. Template: runpod/pytorch:2.1.1-py3.10-cuda12.1.1-devel-ubuntu22.04 GPU Cloud: 1 x RTX 3090 | 12 vCPU...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _parallel;frontend_api;model_support;scheduler_memory cache slowdown env_dependency I am using a runpod container to run vLLM.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: : 193.7 tokens/s, Running: 5 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 4.2%, CPU KV cache usage: 0.0% INFO 02-05 04:53:21 async_llm_engine.py:111] Finished request cmpl-e9f50d97a01148308ccb3e8626b6feb6...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: en I increase it to 10. `python -m vllm.entrypoints.openai.api_server --model openchat/openchat_3.5 --tensor-parallel-size 1` ``` ... INFO: 127.0.0.1:46228 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
