# vllm-project/vllm#11805: [Bug]: preemptmode recompute

| 字段 | 值 |
| --- | --- |
| Issue | [#11805](https://github.com/vllm-project/vllm/issues/11805) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: preemptmode recompute

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My task needs structured json output, so I met this problem and I'm not sure whether it's bug or not. The scheduler will trigger preemption when the load is high: 1. enable prefix caching, prompt mode == recompute, the output structure is unstable; 2. enable prefix caching, prompt mode == swap , the output structure is stable; 3. disable prefix caching, prompt mode == recompute, the output stucture is stable. I did serveral experiments and it always happened. I didn't look deep into the code so im not sure whether there is something missing or a confict between prefix caching and preemption? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory;speculative_decoding cuda;operator;triton build_error env_dependency...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: preemptmode recompute bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My task needs structured json output, so I met this problem and I'm not sure whether it's bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: orting;model_support;scheduler_memory;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g]: preemptmode recompute bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My task needs structured json output, so I met this problem and I'm not sure whether it's bug o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
