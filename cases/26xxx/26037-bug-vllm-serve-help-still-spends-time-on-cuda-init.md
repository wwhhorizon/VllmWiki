# vllm-project/vllm#26037: [Bug]: `vllm serve --help` still spends time on CUDA init

| 字段 | 值 |
| --- | --- |
| Issue | [#26037](https://github.com/vllm-project/vllm/issues/26037) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `vllm serve --help` still spends time on CUDA init

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug This takes about 10 seconds to complete: ```bash $ vllm serve --help INFO 10-01 17:53:11 [__init__.py:216] Automatically detected platform cuda. ``` I propose that default help option bypasses CUDA init / CUDA libraries loading / platform detection and instead prints the usage options fast ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: `vllm serve --help` still spends time on CUDA init bug;stale ### Your current environment N/A ### 🐛 Describe the bug This takes about 10 seconds to complete: ```bash $ vllm serve --help INFO 10-01 17:53:11 [__ini...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: `vllm serve --help` still spends time on CUDA init bug;stale ### Your current environment N/A ### 🐛 Describe the bug This takes about 10 seconds to complete: ```bash $ vllm serve --help INFO 10-01 17:53:11 [__ini...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
