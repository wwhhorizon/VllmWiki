# vllm-project/vllm#23527: [Bug]: Score API encounter Internal Server Error occasionally

| 字段 | 值 |
| --- | --- |
| Issue | [#23527](https://github.com/vllm-project/vllm/issues/23527) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Score API encounter Internal Server Error occasionally

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deploy an embedding model via: ```bash vllm serve intfloat/multilingual-e5-large-instruct -dp 2 --port 5001 ``` I call the score api and it sometimes return 500 error: ```python import requests payload ={ "text_1": "What is the capital of France?", "text_2": [ "The capital of Brazil is Brasilia.", "The capital of France is Paris.", "Horses and cows are both animals" ] } requests.post("http://localhost:5001/score",json=payload).json() ``` ```text {'error': {'message': 'EngineCore encountered an issue. See stack trace (above) for the root cause.', 'type': 'Internal Server Error', 'param': None, 'code': 500}} ``` sometimes it works well: ```text {'id': 'score-a3e8c20809eb4443b8044a48179dfe63', 'object': 'list', 'created': 1756104548, 'model': 'intfloat/multilingual-e5-large-instruct', 'data': [{'index': 0, 'object': 'score', 'score': 0.8375727534294128}, {'index': 1, 'object': 'score', 'score': 0.936454713344574}, {'index': 2, 'object': 'score', 'score': 0.7501654028892517}], 'usage': {'prompt_tokens': 59, 'total_tokens': 59, 'completion_tokens': 0, 'prompt_tokens_details': None}} ``` ### Before submitting a new issue... - [x] Mak...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 01 ``` I call the score api and it sometimes return 500 error: ```python import requests payload ={ "text_1": "What is the capital of France?", "text_2": [ "The capital of Brazil is Brasilia.", "The capital of France is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ur current environment ### 🐛 Describe the bug I deploy an embedding model via: ```bash vllm serve intfloat/multilingual-e5-large-instruct -dp 2 --port 5001 ``` I call the score api and it sometimes return 500 error: ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: I call the score api and it sometimes return 500 error: ```python import requests payload ={ "text_1": "What is the capital of France?", "text_2": [ "The capital of Brazil is Brasilia.", "The capital of France is Paris....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
