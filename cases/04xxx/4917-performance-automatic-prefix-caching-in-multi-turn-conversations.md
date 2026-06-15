# vllm-project/vllm#4917: [Performance]: Automatic Prefix Caching in multi-turn conversations

| 字段 | 值 |
| --- | --- |
| Issue | [#4917](https://github.com/vllm-project/vllm/issues/4917) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Automatic Prefix Caching in multi-turn conversations

### Issue 正文摘录

I'm interested in the automatic prefix caching feature for multi-turn conversations but I can't seem to observe a performance improvement when prefix caching is enabled. [This tweet](https://x.com/vllm_project/status/1776283245665304929/photo/1) from @vllm_project indicates that automatic prefix caching should benefit this use case. I am using the following commands to start the vLLM server: ```console python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf --port 7001 --gpu-memory-utilization 0.5 --disable-log-requests --enforce-eager python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf --port 7001 --gpu-memory-utilization 0.5 --disable-log-requests --enforce-eager --enable-prefix-caching ``` And the following script to simulate a multi turn conversation from a user: ```python import time from openai import OpenAI user_messages = [ "Tell me your ten favourite films", "Who directed each of these films?", "Which director has the most experience?", "What other films has this director directed?", "Do these films have anything in common?", "Which of those films is the oldest?", "How old was the director when this was released?",...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vLLM server: ```console python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf --port 7001 --gpu-memory-utilization 0.5 --disable-log-requests --enforce-eager python -m vllm.entrypoints.opena...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing script to simulate a multi turn conversation from a user: ```python import time from openai import OpenAI user_messages = [ "Tell me your ten favourite films", "Who directed each of these films?", "Which director ha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lama-2-7b-chat-hf --port 7001 --gpu-memory-utilization 0.5 --disable-log-requests --enforce-eager python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf --port 7001 --gpu-memory-utilization 0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ``` With automatic prefix caching disabled I see: ```console $ python test.py CompletionUsage(completion_tokens=598, prompt_tokens=16, total_tokens=614) CompletionUsage(completion_tokens=238, prompt_tokens=629, total_to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
