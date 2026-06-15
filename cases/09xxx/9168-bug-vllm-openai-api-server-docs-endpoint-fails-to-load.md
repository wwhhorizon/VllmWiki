# vllm-project/vllm#9168: [Bug]: vLLM OpenAI-api server `/docs` endpoint fails to load

| 字段 | 值 |
| --- | --- |
| Issue | [#9168](https://github.com/vllm-project/vllm/issues/9168) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM OpenAI-api server `/docs` endpoint fails to load

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Simply run `vllm serve facebook/opt-125m --enforce-eager` and navigate to `http://localhost:8000/docs` I can replicate this on the last several releases and using latest main: The last release where the endpoint works properly is `vllm==0.5.4`. The following image is the expected result on page load. In both cases, the server reports that the GET requests were successful: ``` INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit) INFO: 127.0.0.1:49758 - "GET /docs HTTP/1.1" 200 OK INFO: 127.0.0.1:49758 - "GET /openapi.json HTTP/1.1" 200 OK ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vLLM OpenAI-api server `/docs` endpoint fails to load bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Simply run `vllm serve facebook/opt-125m --enforce-eager` an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s` endpoint fails to load bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Simply run `vllm serve facebook/opt-125m --enforce-eager` and navigate to `http://localhost:800...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
