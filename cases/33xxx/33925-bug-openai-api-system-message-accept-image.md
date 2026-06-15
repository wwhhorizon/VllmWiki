# vllm-project/vllm#33925: [Bug]: OpenAI API: system message accept image

| 字段 | 值 |
| --- | --- |
| Issue | [#33925](https://github.com/vllm-project/vllm/issues/33925) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OpenAI API: system message accept image

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using vllm version `0.15.1` Serving command: ``` vllm serve openai/gpt-oss-20b --host 0.0.0.0 --port 8000 --tensor-parallel-size 1 --max-num-seqs 256 --gpu_memory_utilization 0.97 --enable-auto-tool-choice --tool-call-parser=openai --async-scheduling --enable-chunked-prefill --no-enable-prefix-caching --attention-backend TRITON_ATTN --stream-interval 20 --max-cudagraph-capture-size 2048 --max-num-batched-tokens 8192 ``` The OpenAI API accepts images in system prompts. Here is the example input: ```bash #!/bin/bash curl -X 'POST' \ 'http://localhost:8000/v1/chat/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "max_tokens": 128, "messages": [ { "content": [{"type": "image_url", "image_url": {"url": "some_url"}}], "role": "system" } ], "model": "openai/gpt-oss-20b", "n": 1, "stop": [ "###" ], "temperature": 0.7 }' ``` Output: ``` { "id": "chatcmpl-9f5f8c2eb0ce3164", "object": "chat.completion", "created": 1770307926, "model": "openai/gpt-oss-20b", "choices": [ { "index": 0, "message": { "role": "assistant", "content": null, "refusal": null, "annotations": null, "audio": null, "function_call...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nable-chunked-prefill --no-enable-prefix-caching --attention-backend TRITON_ATTN --stream-interval 20 --max-cudagraph-capture-size 2048 --max-num-batched-tokens 8192 ``` The OpenAI API accepts images in system prompts....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: bug ### Your current environment ### 🐛 Describe the bug Using vllm version `0.15.1` Serving command: ``` vllm serve openai/gpt-oss-20b --host 0.0.0.0 --port 8000 --tensor-parallel-size 1 --max-num-seqs 256 --gpu_m
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n-backend TRITON_ATTN --stream-interval 20 --max-cudagraph-capture-size 2048 --max-num-batched-tokens 8192 ``` The OpenAI API accepts images in system prompts. Here is the example input: ```bash #!/bin/bash curl -X 'POS...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sion `0.15.1` Serving command: ``` vllm serve openai/gpt-oss-20b --host 0.0.0.0 --port 8000 --tensor-parallel-size 1 --max-num-seqs 256 --gpu_memory_utilization 0.97 --enable-auto-tool-choice --tool-ca
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -tool-call-parser=openai --async-scheduling --enable-chunked-prefill --no-enable-prefix-caching --attention-backend TRITON_ATTN --stream-interval 20 --max-cudagraph-capture-size 2048 --max-num-batched-tokens 8192 ``` Th...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
