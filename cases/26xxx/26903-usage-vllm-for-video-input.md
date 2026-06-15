# vllm-project/vllm#26903: [Usage]: vLLM for video input

| 字段 | 值 |
| --- | --- |
| Issue | [#26903](https://github.com/vllm-project/vllm/issues/26903) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM for video input

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of qwen2.5-vl or qwen2.5-omni. When I convert the video to base64 for api calls (e.g. openai format), I found that vLLM seems to use all the video frames by checking the number of prompt tokens. Is there any parameter similar to fps to control the sampling rate? Or do I need to sample the video externally well in advance, save it as video and then convert to base64? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .py` ``` ### How would you like to use vllm I want to run inference of qwen2.5-vl or qwen2.5-omni. When I convert the video to base64 for api calls (e.g. openai format), I found that vLLM seems to use all the video fram...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 64? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vLLM for video input usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of qwen2.5-vl or qwen2.5-omni. When I c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
