# vllm-project/vllm#24508: [Bug]: vllm/vllm-openai image has an linux-libc-dev with many CVEs, update linux-libc-dev

| 字段 | 值 |
| --- | --- |
| Issue | [#24508](https://github.com/vllm-project/vllm/issues/24508) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm-openai image has an linux-libc-dev with many CVEs, update linux-libc-dev

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CVE-2024-56658, CVE-2024-53150, CVE-2024-56551, CVE-2024-56608, CVE-2024-56598, CVE-2024-57798, CVE-2022-0995, CVE-2024-35864, CVE-2024-50047, CVE-2025-21887, CVE-2023-52927, CVE-2024-56593, CVE-2024-26928, CVE-2024-53140, CVE-2023-52664, CVE-2024-56596, CVE-2024-57850, CVE-2024-56595, CVE-2024-53171, CVE-2024-53197, CVE-2024-53168 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 168 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ai image has an linux-libc-dev with many CVEs, update linux-libc-dev bug;stale ### Your current environment ### 🐛 Describe the bug CVE-2024-56658, CVE-2024-53150, CVE-2024-56551, CVE-2024-56608, CVE-2024-56598, CVE-2024...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
