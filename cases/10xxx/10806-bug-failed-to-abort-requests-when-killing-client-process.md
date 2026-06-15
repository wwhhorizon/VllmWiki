# vllm-project/vllm#10806: [Bug]: Failed to abort requests when killing client process.

| 字段 | 值 |
| --- | --- |
| Issue | [#10806](https://github.com/vllm-project/vllm/issues/10806) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to abort requests when killing client process.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The vllm server seems to fail to abort the requests sent by interrupted processes. ### How to reproduce the bug First, I started a vllm server: ```bash vllm serve "Qwen/Qwen2.5-Coder-0.5B-Instruct" ``` Then I run the following code: ```python import subprocess import time curl_command = [ "curl", "-X", "POST", "http://localhost:8000/v1/chat/completions", "-H", "Content-Type: application/json", "--data", '''{ "model": "Qwen/Qwen2.5-Coder-0.5B-Instruct", "messages": [ { "role": "user", "content": "Tell me the lyrics of `Hey Jude`." } ], "ignore_eos": true }''' ] try: process = subprocess.Popen(curl_command) print(f"Started process with PID: {process.pid}") time.sleep(1) process.terminate() print(f"Killed process with PID: {process.pid}") except Exception as e: print(f"An error occurred: {e}") ``` I got outputs: ``` INFO 12-01 16:04:14 logger.py:37] Received request chatcmpl-64bca667923f403ba97baef4fd4ea0cd: prompt: ' system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant. \n user\nTell me the lyrics of `Hey Jude`. \n assistant\n', params: SamplingParams(n=1, presence_penalty=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: en2.5-Coder-0.5B-Instruct" ``` Then I run the following code: ```python import subprocess import time curl_command = [ "curl", "-X", "POST", "http://localhost:8000/v1/chat/completions", "-H", "Content-Type: application/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ts when killing client process. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The vllm server seems to fail to abort the requests sent by interrupted processes. ### How to r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Failed to abort requests when killing client process. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The vllm server seems to fail to abort the requests sent by interr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 923f403ba97baef4fd4ea0cd. INFO 12-01 16:04:15 metrics.py:460] Avg prompt throughput: 6.2 tokens/s, Avg generation throughput: 0.2 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
