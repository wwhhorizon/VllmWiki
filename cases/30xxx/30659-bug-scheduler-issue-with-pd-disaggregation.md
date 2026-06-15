# vllm-project/vllm#30659: [Bug]: scheduler issue with PD disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#30659](https://github.com/vllm-project/vllm/issues/30659) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: scheduler issue with PD disaggregation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I got an issue of scheduler when deploying with PD disaggregation: Since current scheduling strategy doesn't free blocks occupied by requests with WAITING_FOR_REMOTE_KVS state, will the server stuck in certain scenarios? For example, in step 4, the secheduler will allocate blocks for request 1 fisrt since it was put back to the front of the waiting queue in step 3. Then request 2 will never get into running queue since it requires more blocks for next token and the scheduler will get stuck in the loop from step 2 to step 4. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: scheduler issue with PD disaggregation bug;stale ### Your current environment ### 🐛 Describe the bug Hello, I got an issue of scheduler when deploying with PD disaggregation: Since current scheduling strategy doe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g with PD disaggregation: Since current scheduling strategy doesn't free blocks occupied by requests with WAITING_FOR_REMOTE_KVS state, will the server stuck in certain scenarios? For example, in step 4, the secheduler...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
