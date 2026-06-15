# vllm-project/vllm#31961: [Performance]: EPD Disaggregation Performance Testing Scripts

| 字段 | 值 |
| --- | --- |
| Issue | [#31961](https://github.com/vllm-project/vllm/issues/31961) |
| 状态 | open |
| 标签 | performance |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: EPD Disaggregation Performance Testing Scripts

### Issue 正文摘录

### Proposal to improve performance Hi, I noticed that epd disaggregation is now ready in vLLM. And the [blog](https://blog.vllm.ai/2025/12/15/vllm-epd.html) shows encouraging results. But we failed to get the expected performance improvement and want to troubleshoot the potential errors. Could you please provide complete testing scripts for reproduction? Thanks in advance. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: EPD Disaggregation Performance Testing Scripts performance ### Proposal to improve performance Hi, I noticed that epd disaggregation is now ready in vLLM. And the [blog](https://blog.vllm.ai/2025/12/15/vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
