# vllm-project/vllm#9841: [Bug]: Incosistent logprobs across multiple runs

| 字段 | 值 |
| --- | --- |
| Issue | [#9841](https://github.com/vllm-project/vllm/issues/9841) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incosistent logprobs across multiple runs

### Issue 正文摘录

### Your current environment H100 80GB ### Model Input Dumps _No response_ ### 🐛 Describe the bug Even when setting the `seed` in both `LLM` and `SamplingParams`, the logprobs differ across runs. Tried with both stable and nightly. Is there any way to get consistent logprobs? ``` from vllm import LLM, SamplingParams sampling_params = SamplingParams( temperature=0, max_tokens=100, logprobs=10, seed=0 ) llm = LLM(model="path/to/downloaded/model", seed=0) ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt logprobs across multiple runs bug;stale ### Your current environment H100 80GB ### Model Input Dumps _No response_ ### 🐛 Describe the bug Even when setting the `seed` in both `LLM` and `SamplingParams`, the logprobs...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and nightly. Is there any way to get consistent logprobs? ``` from vllm import LLM, SamplingParams sampling_params = SamplingParams( temperature=0, max_tokens=100, logprobs=10, seed=0 ) llm = LLM(model="path/to/download...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: oss multiple runs bug;stale ### Your current environment H100 80GB ### Model Input Dumps _No response_ ### 🐛 Describe the bug Even when setting the `seed` in both `LLM` and `SamplingParams`, the logprobs differ across r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Incosistent logprobs across multiple runs bug;stale ### Your current environment H100 80GB ### Model Input Dumps _No response_ ### 🐛 Describe the bug Even when setting the `seed` in both `LLM` and `SamplingParams...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
