# vllm-project/vllm#30922: [Bug]: Use the offical doucment  vllm online method deploy DeepSeek-OCR，the result is very bad . but I ust the offline method the result is normal. why ?

| 字段 | 值 |
| --- | --- |
| Issue | [#30922](https://github.com/vllm-project/vllm/issues/30922) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Use the offical doucment  vllm online method deploy DeepSeek-OCR，the result is very bad . but I ust the offline method the result is normal. why ?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use https://github.com/vllm-project/recipes/blob/main/DeepSeek/DeepSeek-OCR.md the offline and online mehtod is work, run ok。 but the same picture in offline is better than online, I can't find the reason what happend ? can someone help me ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ment ### 🐛 Describe the bug I use https://github.com/vllm-project/recipes/blob/main/DeepSeek/DeepSeek-OCR.md the offline and online mehtod is work, run ok。 but the same picture in offline is better than online, I can't...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: very bad . but I ust the offline method the result is normal. why ? bug;stale ### Your current environment ### 🐛 Describe the bug I use https://github.com/vllm-project/recipes/blob/main/DeepSeek/DeepSeek-OCR.md the offl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
