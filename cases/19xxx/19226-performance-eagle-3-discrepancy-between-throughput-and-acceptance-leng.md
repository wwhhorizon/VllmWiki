# vllm-project/vllm#19226: [Performance]: EAGLE-3: Discrepancy Between Throughput and Acceptance Length Improvements

| 字段 | 值 |
| --- | --- |
| Issue | [#19226](https://github.com/vllm-project/vllm/issues/19226) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: EAGLE-3: Discrepancy Between Throughput and Acceptance Length Improvements

### Issue 正文摘录

### Proposal to improve performance We performed the benchmarking using both the official LLaMA 3 70B EAGLE-2 head (yuhuili/EAGLE-LLaMA3-Instruct-70B) and the LLaMA 3.3 70B EAGLE-3 head (yuhuili/EAGLE3-LLaMA3.3-Instruct-70B). In the case of the 70B EAGLE-3 head, despite a ~50% reduction in total model parameters, the OTPS (Output Tokens Per Second) gain is roughly proportional to the acceptance length gain. I believe there are still gaps in the current EAGLE-3 implementation that, if addressed, could lead to further performance improvements. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: EAGLE-3: Discrepancy Between Throughput and Acceptance Length Improvements performance;stale ### Proposal to improve performance We performed the benchmarking using both the official LLaMA 3 70B EAGLE-2 h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: prove performance We performed the benchmarking using both the official LLaMA 3 70B EAGLE-2 head (yuhuili/EAGLE-LLaMA3-Instruct-70B) and the LLaMA 3.3 70B EAGLE-3 head (yuhuili/EAGLE3-LLaMA3.3-Instruct-70B). In the case...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: to improve performance We performed the benchmarking using both the official LLaMA 3 70B EAGLE-2 head (yuhuili/EAGLE-LLaMA3-Instruct-70B) and the LLaMA 3.3 70B EAGLE-3 head (yuhuili/EAGLE3-LLaMA3.3-Instruct-70B). In the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: epancy Between Throughput and Acceptance Length Improvements performance;stale ### Proposal to improve performance We performed the benchmarking using both the official LLaMA 3 70B EAGLE-2 head (yuhuili/EAGLE-LLaMA3-Ins...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
