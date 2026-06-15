# vllm-project/vllm#21054: [Usage]: How to do expert parallel on MoE model?

| 字段 | 值 |
| --- | --- |
| Issue | [#21054](https://github.com/vllm-project/vllm/issues/21054) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to do expert parallel on MoE model?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I tried to initialize a moe model in the tp way, and midified it with tp_size=1, dp_size=2 (I use 2 GPUs), and set enable_expert_parallel=True. Then I added requests to the LLMengine and executed the step function normally. But only `add_request` can be executed, while the `step` function hangs. And I can only see `EngineCore_0` executing the prepare input operation. I want to know if it is correct to initialize an expert parallel model in this way? By the way, I set export `VLLM_LOGGING_LEVEL=DEBUG`, but I still can only see INFO level information. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to do expert parallel on MoE model? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I tried to initialize a moe model in the tp way, a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Usage]: How to do expert parallel on MoE model? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I tried to initialize a moe model in the tp way, a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: size=2 (I use 2 GPUs), and set enable_expert_parallel=True. Then I added requests to the LLMengine and executed the step function normally. But only `add_request` can be executed, while the `step` function hangs. And I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
