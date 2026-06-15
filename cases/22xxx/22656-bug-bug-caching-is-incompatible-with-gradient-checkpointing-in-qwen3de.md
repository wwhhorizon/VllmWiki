# vllm-project/vllm#22656: [Bug]: [Bug]: Caching is incompatible with gradient checkpointing in Qwen3DecoderLayer. Setting `past_key_value=None`.

| 字段 | 值 |
| --- | --- |
| Issue | [#22656](https://github.com/vllm-project/vllm/issues/22656) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Bug]: Caching is incompatible with gradient checkpointing in Qwen3DecoderLayer. Setting `past_key_value=None`.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Ever since I upgraded from vllm 0.9.1 to vllm 0.10.0, I have been getting the warning Caching is incompatible with gradient checkpointing in Qwen3DecoderLayer. Setting `past_key_value=None`. spammed on all my training scripts which used to work a week ago, and they no longer train (in fact, the model completely deteriorates immediately and becomes gibberish). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [Bug]: Caching is incompatible with gradient checkpointing in Qwen3DecoderLayer. Setting `past_key_value=None`. bug;stale ### Your current environment ### 🐛 Describe the bug Ever since I upgraded from vllm 0.9.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: [Bug]: Caching is incompatible with gradient checkpointing in Qwen3DecoderLayer. Setting `past_key_value=None`. bug;stale ### Your current environment ### 🐛 Describe the bug Ever since I upgraded from vllm 0.9.1 t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
