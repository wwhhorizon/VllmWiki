# vllm-project/vllm#19285: [Bug]: continue_final_message + echo + prefix-caching + V0 crash the server

| 字段 | 值 |
| --- | --- |
| Issue | [#19285](https://github.com/vllm-project/vllm/issues/19285) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: continue_final_message + echo + prefix-caching + V0 crash the server

### Issue 正文摘录

Start vLLM with (in example): ```bash VLLM_USE_V1=0 vllm serve Qwen/Qwen3-0.6B --enable-prefix-caching ``` Then run this code twice: ```python import requests endpoint = "http://localhost:8000/v1" url = f"{endpoint}/chat/completions" payload = { "model": "Qwen/Qwen3-0.6B", "messages": [ {"role": "user", "content": "write a poem"}, {"role": "assistant", "content": "This is a song about vLLM"}, ], "add_generation_prompt": False, "continue_final_message": True, "echo": True, "max_tokens": 128, } r = requests.post(url, json=payload) r.raise_for_status() print(r.json()["choices"][0]["message"]["content"]) ``` vLLM server crashes with this stack-trace: ```python INFO 06-06 16:37:27 [engine.py:316] Added request chatcmpl-b497edd0f9084462810cdd8126699707. INFO: 127.0.0.1:38366 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR 06-06 16:37:27 [engine.py:164] AssertionError() ERROR 06-06 16:37:27 [engine.py:164] Traceback (most recent call last): ERROR 06-06 16:37:27 [engine.py:164] File "/home/user/code/debug/.venv/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 162, in start ERROR 06-06 16:37:27 [engine.py:164] self.run_engine_loop() ERROR 06-...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: continue_final_message + echo + prefix-caching + V0 crash the server bug;stale Start vLLM with (in example): ```bash VLLM_USE_V1=0 vllm serve Qwen/Qwen3-0.6B --enable-prefix-caching ``` Then run this code twice: ```pyth...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: bug;stale Start vLLM with (in example): ```bash VLLM_USE_V1=0 vllm serve Qwen/Qwen3-0.6B --enable-prefix-caching ``` Then run this code twice: ```python import requests endpoint = "http://localhost:8000/v1" url = f"{end...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n3-0.6B --enable-prefix-caching ``` Then run this code twice: ```python import requests endpoint = "http://localhost:8000/v1" url = f"{endpoint}/chat/completions" payload = { "model": "Qwen/Qwen3-0.6B", "messages": [ {"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nt": "This is a song about vLLM"}, ], "add_generation_prompt": False, "continue_final_message": True, "echo": True, "max_tokens": 128, } r = requests.post(url, json=payload) r.raise_for_status() print(r.json()["choices"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
