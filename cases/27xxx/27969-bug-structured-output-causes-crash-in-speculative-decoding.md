# vllm-project/vllm#27969: [Bug]: Structured output causes crash in speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#27969](https://github.com/vllm-project/vllm/issues/27969) |
| 状态 | closed |
| 标签 | bug;structured-output;speculative-decoding |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Structured output causes crash in speculative decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When vllm gets a structured output request (e.g. `json_object: true`), and the speculative decoder outputs a token that doesn't fit the structure, it causes vllm to crash. Server: `vllm serve meta-llama/Llama-3.1-8B-Instruct -tp 8 --speculative-config '{"method": "eagle3", "model": "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", "num_speculative_tokens": 4, "max_model_len": 2048}'` Client: ```python from concurrent.futures import ThreadPoolExecutor, wait import requests URL = "http://localhost:8000/v1/chat/completions" HEADERS = { "Authorization": "Bearer EMPTY", "Content-Type": "application/json", } PAYLOAD = { "model": "meta-llama/Llama-3.1-8B-Instruct", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": [{"type": "text", "text": "Say hello world 500 times"}]} ], "structured_outputs": {"json_object": True}, } CONCURR = 30 def do_request(): return requests.post(URL, headers=HEADERS, json=PAYLOAD) with ThreadPoolExecutor(max_workers=CONCURR) as executor: while True: futures =[executor.submit(do_request) for _ in range(CONCURR)] wait(futures) ``` ### Before submitting a new issue... - [...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 't fit the structure, it causes vllm to crash. Server: `vllm serve meta-llama/Llama-3.1-8B-Instruct -tp 8 --speculative-config '{"method": "eagle3", "model": "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", "num_speculative_token...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Structured output causes crash in speculative decoding bug;structured-output;speculative-decoding ### Your current environment ### 🐛 Describe the bug When vllm gets a structured output request (e.g. `json_object:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: : 4, "max_model_len": 2048}'` Client: ```python from concurrent.futures import ThreadPoolExecutor, wait import requests URL = "http://localhost:8000/v1/chat/completions" HEADERS = { "Authorization": "Bearer EMPTY", "Con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
