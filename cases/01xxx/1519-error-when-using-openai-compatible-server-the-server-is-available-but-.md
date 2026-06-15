# vllm-project/vllm#1519: Error:  When using OpenAI-Compatible Server, the server is available but cannot be accessed from the same terminal.

| 字段 | 值 |
| --- | --- |
| Issue | [#1519](https://github.com/vllm-project/vllm/issues/1519) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error:  When using OpenAI-Compatible Server, the server is available but cannot be accessed from the same terminal.

### Issue 正文摘录

I'm using this perfect framework to build up an on-air api server for my local LLM. Specifically, I had run this command in my linux terminal: `python -m vllm.entrypoints.openai.api_server --model /home/XXX/baichuan2 --trust-remote-code --tensor-parallel-size 1 --host 10.201.1.181 --port 8000` Note that /baichuan2 is a directory containing the fine-tuned model derived from baichuan-inc/Baichuan2-13B-Base. And I get: `INFO: Started server process [448902] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://10.201.1.181:8000 (Press CTRL+C to quit)` To test whether the server is ready or not, I used `telnet 10.201.1.181 8000` in another shell, which returned `Trying 10.201.1.181... Connected to 10.201.1.181. Escape character is '^]'.` So I suppose the server is running properly. But when I attempt to call this server via python scripts as documented : `import openai openai.api_key = "0.0.0.0" openai.api_base = 'http://10.201.1.181:8000/v1' response = openai.Completion.create(model='/home/XXX/baichuan2', prompt=prompt, temperature = 0.8, do_sample = True, max_tokens = 512) ` The program will report errors after a long-time pausing...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: be accessed from the same terminal. I'm using this perfect framework to build up an on-air api server for my local LLM. Specifically, I had run this command in my linux terminal: `python -m vllm.entrypoints.openai.api_s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: B-Base. And I get: `INFO: Started server process [448902] INFO: Waiting for application startup. INFO: Application startup complete. INFO: Uvicorn running on http://10.201.1.181:8000 (Press CTRL+C to quit)` To test whet...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: in my linux terminal: `python -m vllm.entrypoints.openai.api_server --model /home/XXX/baichuan2 --trust-remote-code --tensor-parallel-size 1 --host 10.201.1.181 --port 8000` Note that /baichuan2 is a directory containin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Uvicorn running on http://10.201.1.181:8000 (Press CTRL+C to quit)` To test whether the server is ready or not, I used `telnet 10.201.1.181 8000` in another shell, which returned `Trying 10.201.1.181... Connected to 10....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
