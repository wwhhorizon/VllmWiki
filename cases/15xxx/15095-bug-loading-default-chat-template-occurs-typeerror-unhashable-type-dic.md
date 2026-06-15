# vllm-project/vllm#15095: [Bug]: loading default chat template occurs TypeError: unhashable type: 'dict'

| 字段 | 值 |
| --- | --- |
| Issue | [#15095](https://github.com/vllm-project/vllm/issues/15095) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: loading default chat template occurs TypeError: unhashable type: 'dict'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use vLLM with docker compose, upgrade v0.8.0 from v0.7.3, to deploy LLM ```CohereForAI/c4ai-command-r7b-12-2024``` from hugging face. I test structured output api, get this 400 response. ``` {"object":"error","message":"unhashable type: 'dict'","type":"BadRequestError","param":null,"code":400} ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Your current environment ### 🐛 Describe the bug I use vLLM with docker compose, upgrade v0.8.0 from v0.7.3, to deploy LLM ```CohereForAI/c4ai-command-r7b-12-2024``` from hugging face. I test structured output api, g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory attention;cache;cuda;quantization;triton crash dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: se. ``` {"object":"error","message":"unhashable type: 'dict'","type":"BadRequestError","param":null,"code":400} ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and aske...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _support;quantization;scheduler_memory attention;cache;cuda;quantization;triton crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
