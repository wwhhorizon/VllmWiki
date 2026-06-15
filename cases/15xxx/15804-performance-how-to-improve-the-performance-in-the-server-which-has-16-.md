# vllm-project/vllm#15804: [Performance]: how to improve the performance in the server which has 16*T4?

| 字段 | 值 |
| --- | --- |
| Issue | [#15804](https://github.com/vllm-project/vllm/issues/15804) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: how to improve the performance in the server which has 16*T4?

### Issue 正文摘录

### Proposal to improve performance I used the server (16*T4) to run vllm on model deepseer r1 32b. I found that the performance did not improve when the config from "tp=8,pp=1" to "tp=8,pp=2". That's why? I have to use "tp=8,pp=2" because tp=16 is not usable, the sevcie will not start normally. Could you please tell how to do ? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: roposal to improve performance I used the server (16*T4) to run vllm on model deepseer r1 32b. I found that the performance did not improve when the config from "tp=8,pp=1" to "tp=8,pp=2". That's why? I have to use "tp=...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: normally. Could you please tell how to do ? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The out...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hat's why? I have to use "tp=8,pp=2" because tp=16 is not usable, the sevcie will not start normally. Could you please tell how to do ? ### Report of performance regression _No response_ ### Misc discussion on performan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ow to improve the performance in the server which has 16*T4? performance;stale ### Proposal to improve performance I used the server (16*T4) to run vllm on model deepseer r1 32b. I found that the performance did not imp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
