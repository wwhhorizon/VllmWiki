# vllm-project/vllm#19270: [Bug]: guided_regex parsing error crashes the server

| 字段 | 值 |
| --- | --- |
| Issue | [#19270](https://github.com/vllm-project/vllm/issues/19270) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: guided_regex parsing error crashes the server

### Issue 正文摘录

Seems that similar issues (https://github.com/vllm-project/vllm/issues/17248 https://github.com/vllm-project/vllm/issues/17313) were reported and fixed a month ago (https://github.com/vllm-project/vllm/pull/17623) however this still crashes vLLM 0.9.0.1: in example, start vLLM with: ``` vllm serve meta-llama/Llama-3.2-3B-Instruct --max-model-len 8192 ``` and run: ```python import requests endpoint = "http://localhost:8000/v1" url = f"{endpoint}/chat/completions" payload = { "model": "meta-llama/Llama-3.2-3B-Instruct", "messages": [ {"role": "user", "content": "write a poem"}, ], "guided_regex": "foo**", "max_tokens": 128, } r = requests.post(url, json=payload) r.raise_for_status() print(r.json()["choices"][0]["message"]["content"]) ``` This will crash the server, with this stacktrace: ```python INFO 06-06 13:52:49 [async_llm.py:261] Added request chatcmpl-af33f030d2544c3a97ff066adfd9e6bd. ERROR 06-06 13:52:49 [core.py:502] EngineCore encountered a fatal error. ERROR 06-06 13:52:49 [core.py:502] Traceback (most recent call last): ERROR 06-06 13:52:49 [core.py:502] File "/home/user/code/debug/.venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 493, in run_engine_core ER...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: crashes vLLM 0.9.0.1: in example, start vLLM with: ``` vllm serve meta-llama/Llama-3.2-3B-Instruct --max-model-len 8192 ``` and run: ```python import requests endpoint = "http://localhost:8000/v1" url = f"{endpoint}/cha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lama-3.2-3B-Instruct --max-model-len 8192 ``` and run: ```python import requests endpoint = "http://localhost:8000/v1" url = f"{endpoint}/chat/completions" payload = { "model": "meta-llama/Llama-3.2-3B-Instruct", "messa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: llama/Llama-3.2-3B-Instruct --max-model-len 8192 ``` and run: ```python import requests endpoint = "http://localhost:8000/v1" url = f"{endpoint}/chat/completions" payload = { "model": "meta-llama/Llama-3.2-3B-Instruct",...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _async_create_grammar ERROR 06-06 13:52:49 [core.py:502] return self.backend.compile_grammar(request_type, grammar_spec) ERROR 06-06 13:52:49 [core.py:502] File "/home/user/code/debug/.venv/lib/python3.10/site-packages/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
