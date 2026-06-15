# vllm-project/vllm#22407: [Bug]: gpt oss 401 unauthorized error

| 字段 | 值 |
| --- | --- |
| Issue | [#22407](https://github.com/vllm-project/vllm/issues/22407) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt oss 401 unauthorized error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Ran openai-oss-120b and getting 401 unauthorized errors (despite not setting an api key) Command used to start the server: ```bash vllm serve openai/gpt-oss-120b --tensor-parallel-size 2 --async-scheduling ``` Request: ```bash curl -X 'POST' \ 'http://localhost:8000/v1/chat/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "messages": [ { "content": "who are you?", "role": "user" } ], "model": "openai/gpt-oss-120b" }' ``` This is also the case even to list models: ```bash curl -X 'GET' \ 'http://localhost:8000/v1/models' \ -H 'accept: application/json' ``` Response from server: (APIServer pid=3999075) INFO: 127.0.0.1:46686 - "GET /v1/chat/completions HTTP/1.1" 401 Unauthorized ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;samp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rve openai/gpt-oss-120b --tensor-parallel-size 2 --async-scheduling ``` Request: ```bash curl -X 'POST' \ 'http://localhost:8000/v1/chat/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: zed ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: an api key) Command used to start the server: ```bash vllm serve openai/gpt-oss-120b --tensor-parallel-size 2 --async-scheduling ``` Request: ```bash curl -X 'POST' \ 'http://localhost:8000/v1/chat/completions' \ -H 'ac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
