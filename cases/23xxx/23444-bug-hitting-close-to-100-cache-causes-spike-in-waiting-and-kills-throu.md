# vllm-project/vllm#23444: [Bug]: Hitting close to 100% cache causes spike in waiting and kills throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#23444](https://github.com/vllm-project/vllm/issues/23444) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hitting close to 100% cache causes spike in waiting and kills throughput

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Above is a screenshot of monitoring the metrics. I have users submitting API requests hitting vLLM. Once vLLM cache reaches close to 100%, then the num waiting starts spiking and the prompt throughput goes to 0. This indicates that the cache is either not evicting or something is deadlocking preventing new prompts to process. Here is another view of the issue. You can see that the system seems to just stop processing prompts: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Hitting close to 100% cache causes spike in waiting and kills throughput bug;unstale ### Your current environment ### 🐛 Describe the bug Above is a screenshot of monitoring the metrics. I have users submitting AP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Hitting close to 100% cache causes spike in waiting and kills throughput bug;unstale ### Your current environment ### 🐛 Describe the bug Above is a screenshot of monitoring the metrics. I have users submitting AP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
