# vllm-project/vllm#8358: [Bug]: MistralTokenizer object has no attribute 'get_vocab'

| 字段 | 值 |
| --- | --- |
| Issue | [#8358](https://github.com/vllm-project/vllm/issues/8358) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MistralTokenizer object has no attribute 'get_vocab'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to use `guided_json` or `response_format` in request via vLLM server with `Mistral-Nemo-Instruct-2407` and `--tokenizer-mode mistral` but get an `AttributeError` : `AttributeError: 'MistralTokenizer' object has no attribute 'get_vocab'` Launch the server : ```shell vllm serve /path/to/model/Mistral-Nemo-Instruct-2407 --tokenizer-mode mistral --max-model-len 4096 --host 127.0.0.1 --port 6379 ``` Request in python with `response_format`: ```python import requests url = "http://127.0.0.1:6379" endpoints = "/v1/completions" data = { "prompt": "Describe Ada Lovelace. Your answer should be in form of a json with the keywords name, age, is_alive, height_in_meters, names_of_children.", "model": "Mistral-Nemo-Instruct-2407", "temperature": 0.0, "repetition_penalty": 1, "top_p": 0.8, "max_tokens": 150, "response_format": { "type": "json_object" } } response = requests.post(url+endpoints, json=data) response.json() ``` Same with `guided_json` : ```python import requests url = "http://127.0.0.1:6379" endpoints = "/v1/completions" data = { "prompt": "Describe Ada Lovelace.", "model": "Mistral-Nemo-Instruct-2407", "temperature": 0.0, "re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .1 --port 6379 ``` Request in python with `response_format`: ```python import requests url = "http://127.0.0.1:6379" endpoints = "/v1/completions" data = { "prompt": "Describe Ada Lovelace. Your answer should be in form...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: File "path/to/venv/venv_happyvllm/lib/python3.11/site-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "path/to/venv/venv_happyvllm/lib/python3.11/site-package...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ment ### 🐛 Describe the bug I try to use `guided_json` or `response_format` in request via vLLM server with `Mistral-Nemo-Instruct-2407` and `--tokenizer-mode mistral` but get an `AttributeError` : `AttributeError: 'Mis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: # 🐛 Describe the bug I try to use `guided_json` or `response_format` in request via vLLM server with `Mistral-Nemo-Instruct-2407` and `--tokenizer-mode mistral` but get an `AttributeError` : `AttributeError: 'MistralTok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
