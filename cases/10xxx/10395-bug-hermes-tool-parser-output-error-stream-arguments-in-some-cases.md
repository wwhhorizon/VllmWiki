# vllm-project/vllm#10395: [Bug]: Hermes tool parser output error stream arguments in some cases.

| 字段 | 值 |
| --- | --- |
| Issue | [#10395](https://github.com/vllm-project/vllm/issues/10395) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hermes tool parser output error stream arguments in some cases.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The `extract_tool_calls_streaming` component of the Hermes tool parser generates error arguments during the parsing of streaming tool function outputs when the LLM produces a specific output content. ### LLM `Qwen2.5-72B-Instruct-AWQ` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: he parsing of streaming tool function outputs when the LLM produces a specific output content. ### LLM `Qwen2.5-72B-Instruct-AWQ` ### Before submitting a new issue... - [X] Make sure you already searched for relevant is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ction outputs when the LLM produces a specific output content. ### LLM `Qwen2.5-72B-Instruct-AWQ` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot livi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ng_logits;speculative_decoding cache;cuda;operator;quantization;sampling;triton build_error;crash;import_error;slowdown env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda;operator;quantization;sampling;triton build_error;crash;import_error;slowdown env_dep...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
