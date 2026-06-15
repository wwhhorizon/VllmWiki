# vllm-project/vllm#15538: [Usage]: How to get "num_gpu_blocks" in V1？

| 字段 | 值 |
| --- | --- |
| Issue | [#15538](https://github.com/vllm-project/vllm/issues/15538) |
| 状态 | closed |
| 标签 | help wanted;good first issue;usage;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to get "num_gpu_blocks" in V1？

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm In V0, I can get "num_gpu_blocks" through "llm.llm_engine.cache_config.num_gpu_blocks". But in V1, LLM and EngineCore are in different processes. How can I get "num_gpu_blocks"? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s"? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Usage]: How to get "num_gpu_blocks" in V1？ help wanted;good first issue;usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm In V0, I can get "nu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: se vllm In V0, I can get "num_gpu_blocks" through "llm.llm_engine.cache_config.num_gpu_blocks". But in V1, LLM and EngineCore are in different processes. How can I get "num_gpu_blocks"? ### Before submitting a new issue...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: How to get "num_gpu_blocks" in V1？ help wanted;good first issue;usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm In V0, I can get "num_gpu_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
