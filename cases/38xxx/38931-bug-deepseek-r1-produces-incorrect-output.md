# vllm-project/vllm#38931: [Bug]: Deepseek R1 produces incorrect output

| 字段 | 值 |
| --- | --- |
| Issue | [#38931](https://github.com/vllm-project/vllm/issues/38931) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deepseek R1 produces incorrect output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-R1 --trust-remote-code --tensor-parallel-size 8 ``` ``` import requests import json # 1. Update the URL to the chat endpoint url = "http://localhost:8000/v1/chat/completions" # 2. Structure the payload with roles payload = { # "model": "Qwen/Qwen2.5-1.5B-Instruct", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Who won the world series in 2025?"} ], "max_tokens": 1000, "temperature": 0, "stream": True } response = requests.post(url, json=payload, stream=True) ``` Output ``` You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assistant. You are a helpful assi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t/completions" # 2. Structure the payload with roles payload = { # "model": "Qwen/Qwen2.5-1.5B-Instruct", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Who won...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eek-ai/DeepSeek-R1 --trust-remote-code --tensor-parallel-size 8 ``` ``` import requests import json # 1. Update the URL to the chat endpoint url = "http://localhost:8000/v1/chat/completions" # 2. Structure the payload w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: DeepSeek-R1 --trust-remote-code --tensor-parallel-size 8 ``` ``` import requests import json # 1. Update the URL to the chat endpoint url = "http://localhost:8000/v1/chat/completions" # 2. Structure the payload with rol...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
