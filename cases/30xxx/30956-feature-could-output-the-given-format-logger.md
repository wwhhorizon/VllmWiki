# vllm-project/vllm#30956: [Feature]: could output the given format logger ?

| 字段 | 值 |
| --- | --- |
| Issue | [#30956](https://github.com/vllm-project/vllm/issues/30956) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: could output the given format logger ?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hi,dear , i have def the logger from py scripts ,etc, logger_utils.py and could i use shell run the command with the logger, such as , `vllm serve qwen3-embedding-0.6b --logger_file logger_utils.py ` thx i really need your help SOS ,thx ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: could output the given format logger ? feature request;stale ### 🚀 The feature, motivation and pitch hi,dear , i have def the logger from py scripts ,etc, logger_utils.py and could i use shell run the command...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: could output the given format logger ? feature request;stale ### 🚀 The feature, motivation and pitch hi,dear , i have def the logger from py scripts ,etc, logger_utils.py and could i use shell run the command...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
