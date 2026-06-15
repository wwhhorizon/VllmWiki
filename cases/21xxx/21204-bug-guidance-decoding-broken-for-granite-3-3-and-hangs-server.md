# vllm-project/vllm#21204: [Bug]: Guidance decoding broken for Granite 3.3 and hangs server

| 字段 | 值 |
| --- | --- |
| Issue | [#21204](https://github.com/vllm-project/vllm/issues/21204) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Guidance decoding broken for Granite 3.3 and hangs server

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using the `guidance` backend with IBM Granite 3.3 can casue the backend to hang and stop responding to all subsequent requests. I observed the same behavior with v0.9.2 and an install of of `main` (`vllm-0.9.2rc2.dev340+g0f199f197`). To reproduce, I'm running the OpenAI server with: ``` vllm serve ibm-granite/granite-3.3-8b-instruct --max-num-seqs 4 --max-model-len 32768 --guided-decoding-backend guidance ``` then sending a request like: ``` curl --request POST 'http://localhost:8000/v1/chat/completions' -H 'Content-Type: application/json' -H 'Accept: application/json' --data-raw '{ "model": "ibm-granite/granite-3.3-8b-instruct", "stream": true, "response_format": {"type": "json_object"}, "messages": [ { "role": "user", "content": [ { "type": "text", "text": "Generate a sample JSON document." } ] } ] }' ``` The request just hangs and the server logs print this obscure error: ``` thread ' ' panicked at toktrie/src/toktree.rs:1101:13: assertion failed: num_parents ", line 6, in __init__ File "/tmp/home/my-vllm/lib64/python3.12/site-packages/vllm/v1/structured_output/backend_guidance.py", line 66, in __post_init__ self.ll_tokenizer...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: `` vllm serve ibm-granite/granite-3.3-8b-instruct --max-num-seqs 4 --max-model-len 32768 --guided-decoding-backend guidance ``` then sending a request like: ``` curl --request POST 'http://localhost:8000/v1/chat/complet...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Guidance decoding broken for Granite 3.3 and hangs server bug;stale ### Your current environment ### 🐛 Describe the bug Using the `guidance` backend with IBM Granite 3.3 can casue the backend to hang and stop res...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: our current environment ### 🐛 Describe the bug Using the `guidance` backend with IBM Granite 3.3 can casue the backend to hang and stop responding to all subsequent requests. I observed the same behavior with v0.9.2 and...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 9.2 and an install of of `main` (`vllm-0.9.2rc2.dev340+g0f199f197`). To reproduce, I'm running the OpenAI server with: ``` vllm serve ibm-granite/granite-3.3-8b-instruct --max-num-seqs 4 --max-model-len 32768 --guided-d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: all subsequent requests. I observed the same behavior with v0.9.2 and an install of of `main` (`vllm-0.9.2rc2.dev340+g0f199f197`). To reproduce, I'm running the OpenAI server with: ``` vllm serve ibm-granite/granite-3.3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
