# vllm-project/vllm#9633: [Usage]: Multimodal content with benchmark_serving.py

| 字段 | 值 |
| --- | --- |
| Issue | [#9633](https://github.com/vllm-project/vllm/issues/9633) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Multimodal content with benchmark_serving.py

### Issue 正文摘录

### Your current environment I am running vllm serve with a multimodal (Phi3.5K). How to I run benchmark_serving.py to test the multimodal? In benchmark_serving.py file I see following but test_mm_content is None ``` test_prompt, test_prompt_len, test_output_len, test_mm_content = ( input_requests[0]) ``` ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Multimodal content with benchmark_serving.py usage;stale ### Your current environment I am running vllm serve with a multimodal (Phi3.5K). How to I run benchmark_serving.py to test the multimodal? In benchmark_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: Multimodal content with benchmark_serving.py usage;stale ### Your current environment I am running vllm serve with a multimodal (Phi3.5K). How to I run benchmark_serving.py to test the multimodal? In benchmark_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Multimodal content with benchmark_serving.py usage;stale ### Your current environment I am running vllm serve with a multimodal (Phi3.5K). How to I run benchmark_serving.py to test the multimodal? In benchmark_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
