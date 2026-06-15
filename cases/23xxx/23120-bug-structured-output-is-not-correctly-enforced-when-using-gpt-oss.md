# vllm-project/vllm#23120: [Bug]: Structured output is not correctly enforced when using GPT-OSS

| 字段 | 值 |
| --- | --- |
| Issue | [#23120](https://github.com/vllm-project/vllm/issues/23120) |
| 状态 | open |
| 标签 | bug;stale;gpt-oss |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Structured output is not correctly enforced when using GPT-OSS

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Structured output is not correctly applied with GPT-OSS in cases where messages are sent on non-final channels, or in cases where the message is on the `final` channel but with additional commentary. Works correctly ``` user Can you generate an image of a dog for me? assistant analysis The user asks: "Can you generate an image of a dog for me?" ...more reasoning content... assistant final { ...output that conforms to the schema I supply... } ``` Does not work correctly ``` user Can you generate an image of a dog for me? assistant analysis The user asks: "Can you generate an image of a dog for me?" ...more reasoning content... assistant final ReplyAction { ...output that doesn't conform to the schema I supply... } ``` Does not work correctly ``` user Can you generate an image of a dog for me? assistant analysis The user asks: "Can you generate an image of a dog for me?" ...more reasoning content... assistant commentary to=functions.ReplyAction { ...output that doesn't conform to the schema I supply... } ``` I think [the state machine that terminates reasoning parsing for GPT-OSS](https://github.com/vllm-project/vllm/blob/main/vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;trit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Structured output is not correctly enforced when using GPT-OSS bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Structured output is not correctly applied with GPT-OSS in cases where messages...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: issed here. Also not 100% clear this is the root cause since I'm not an expert in the vLLM codebase. Let me know. I can contribute a fix here, if required. ### Before submitting a new issue... - [x] Make sure you alread...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: Structured output is not correctly enforced when using GPT-OSS bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Structured output is not correctly applied with GPT-OSS in cases where messages...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
