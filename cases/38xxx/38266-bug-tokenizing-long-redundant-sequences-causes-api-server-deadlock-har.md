# vllm-project/vllm#38266: [Bug]: tokenizing long redundant sequences causes API server deadlock (harmony and others)

| 字段 | 值 |
| --- | --- |
| Issue | [#38266](https://github.com/vllm-project/vllm/issues/38266) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tokenizing long redundant sequences causes API server deadlock (harmony and others)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, It seems there is a critical issue with the tokenization implementation in the web server When submitting a query with a lots of redundant characters, the server takes a lot of time to process the query and become unresponsive. While focusing on the v0.17.0 version, I reproduce the same behavior with the v0.18.0 and the `VLLM_USE_V2_MODEL_RUNNER=1` env. There are 2 separate issue I want to emphasis - The tokenizer runtime for a given HTTP query should not impact serving other concurrent requests, currently that is the case and it cause unavailability of the service - High processing time caused by long sequence of similar characters can be problematic: depending on the [tokenizer implementation](https://github.com/openai/harmony/blob/main/src/tiktoken.rs#L45) it can be quite slow, for instance in harmony cases, up to 10m for 1M characters, 5s for 100k characters.. Taking the gpt-oss model (120b/20b) as example, when performing a call to `/v1/chat/completions` this [method](https://github.com/vllm-project/vllm/blob/v0.17.0/vllm/entrypoints/openai/chat_completion/serving.py#L1984) is called to perform the tokenization. This...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rocess the query and become unresponsive. While focusing on the v0.17.0 version, I reproduce the same behavior with the v0.18.0 and the `VLLM_USE_V2_MODEL_RUNNER=1` env. There are 2 separate issue I want to emphasis - T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: tokenizing long redundant sequences causes API server deadlock (harmony and others) bug ### Your current environment ### 🐛 Describe the bug Hello, It seems there is a critical issue with the tokenization implemen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n"` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ion, I reproduce the same behavior with the v0.18.0 and the `VLLM_USE_V2_MODEL_RUNNER=1` env. There are 2 separate issue I want to emphasis - The tokenizer runtime for a given HTTP query should not impact serving other...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
