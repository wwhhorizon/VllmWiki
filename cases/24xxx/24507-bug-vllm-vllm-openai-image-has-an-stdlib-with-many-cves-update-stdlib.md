# vllm-project/vllm#24507: [Bug]: vllm/vllm-openai image has an stdlib with many CVEs, update stdlib

| 字段 | 值 |
| --- | --- |
| Issue | [#24507](https://github.com/vllm-project/vllm/issues/24507) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm-openai image has an stdlib with many CVEs, update stdlib

### Issue 正文摘录

### Your current environment Please upgrade stdlib. ### 🐛 Describe the bug CVE-2022-41715, CVE-2022-30633, CVE-2023-45287, CVE-2022-30632, CVE-2022-2879, CVE-2023-24534, CVE-2025-47907, CVE-2022-30631, CVE-2022-2880, CVE-2024-24790, CVE-2023-24540, CVE-2023-24539, CVE-2023-29400, CVE-2022-41724, CVE-2022-41720, CVE-2023-29403, CVE-2023-24537, CVE-2022-30630, CVE-2024-34156, CVE-2022-41725, CVE-2022-41716, CVE-2022-41723, CVE-2023-39325, CVE-2022-30580, CVE-2022-27664, CVE-2022-29804, CVE-2022-41722, CVE-2022-30634, CVE-2022-32189, CVE-2023-45283, CVE-2022-28131, CVE-2023-24536, CVE-2022-30635, CVE-2023-24538 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 538 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : vllm/vllm-openai image has an stdlib with many CVEs, update stdlib bug;stale ### Your current environment Please upgrade stdlib. ### 🐛 Describe the bug CVE-2022-41715, CVE-2022-30633, CVE-2023-45287, CVE-2022-30632, C...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
