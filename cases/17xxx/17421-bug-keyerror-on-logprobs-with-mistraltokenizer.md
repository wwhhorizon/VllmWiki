# vllm-project/vllm#17421: [Bug]: KeyError on logprobs with MistralTokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#17421](https://github.com/vllm-project/vllm/issues/17421) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KeyError on logprobs with MistralTokenizer

### Issue 正文摘录

### Your current environment I confirmed that it still fails on [current main at the time of writing](https://github.com/vllm-project/vllm/commit/7489ec0bab2904dcc4001af59a942a16756fdbbc). See below for reproduction instructions: ### 🐛 Describe the bug We found an edge-case that causes requests to error out when using the MistralTokenizer with a model. example serving command using the MistralTokenizer (with a model using the Tekken tokenizer): ``` vllm serve mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tokenizer-mode mistral --config-format mistral --load-format mistral ``` simplified reproduction case: ``` curl -s -X POST \ -H "Content-Type: application/json" \ "http://localhost:8000/v1/chat/completions" \ --data-binary @- << _EOF { "model": "mistralai/Mistral-Small-3.1-24B-Instruct-2503", "logprobs": true, "top_logprobs": 2, "messages": [ { "role": "user", "content": " " } ], "guided_json": {"properties": {}} } _EOF ``` The relevant part of the stacktrace ``` ... File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 477, in create_chat_completion generator = await handler.create_chat_completion(request, raw_request) ^^^^^^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: that causes requests to error out when using the MistralTokenizer with a model. example serving command using the MistralTokenizer (with a model using the Tekken tokenizer): ``` vllm serve mistralai/Mistral-Small-3.1-24...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: th a model using the Tekken tokenizer): ``` vllm serve mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tokenizer-mode mistral --config-format mistral --load-format mistral ``` simplified reproduction case: ``` curl -s -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: instructions: ### 🐛 Describe the bug We found an edge-case that causes requests to error out when using the MistralTokenizer with a model. example serving command using the MistralTokenizer (with a model using the Tekke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: From my investigation, this occurs when all of the top logprobs are special tokens. For this case with MistralTokenizer [`decoded_tokens`](https://github.com/vllm-project/vllm/blob/7489ec0bab2904dcc4001af59a942a16756fdb...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
