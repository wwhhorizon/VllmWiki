# vllm-project/vllm#9651: [Performance]: Low GPU utilization - is it normal?

| 字段 | 值 |
| --- | --- |
| Issue | [#9651](https://github.com/vllm-project/vllm/issues/9651) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Low GPU utilization - is it normal?

### Issue 正文摘录

### Proposal to improve performance Hi thanks for the library! When using it with llama 3.2 1B to generate some text, I find the GPU has low utilization as below: The computation is roughly ~60% utilization, and memory bandwidth is also ~60%. Then from my naive thoughts, this may not be bounded by core computation or memory, thus maybe we can improve it. I am happy to provide more information or PR. ![image](https://github.com/user-attachments/assets/1b0ba3f8-b66b-4a6d-bae8-824bdc74ac3e) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: al to improve performance Hi thanks for the library! When using it with llama 3.2 1B to generate some text, I find the GPU has low utilization as below: The computation is roughly ~60% utilization, and memory bandwidth...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: /assets/1b0ba3f8-b66b-4a6d-bae8-824bdc74ac3e) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Low GPU utilization - is it normal? performance;stale ### Proposal to improve performance Hi thanks for the library! When using it with llama 3.2 1B to generate some text, I find the GPU has low utilizati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
