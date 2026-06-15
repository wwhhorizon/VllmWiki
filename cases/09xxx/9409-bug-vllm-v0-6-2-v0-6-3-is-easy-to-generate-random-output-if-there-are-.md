# vllm-project/vllm#9409: [Bug]: vllm v0.6.2/v0.6.3 is easy to generate random output if there are many symbols(not words) in prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#9409](https://github.com/vllm-project/vllm/issues/9409) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm v0.6.2/v0.6.3 is easy to generate random output if there are many symbols(not words) in prompt

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have an observation: If there are many symbols(non-words) in prompt, like following cases, v0.6.x is much easier to generate random output: * markdown table symbo "|" * yaml in json value * json in json One output is as following: ``` I have been changed to be | Mandatory. | | | | | | | | | | | | Mandatory (SIP...-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP-SIP | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. | Mandatory. |" ``` If I switch back to 0.5.4, this issue will be gone....

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: bols(not words) in prompt bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have an observation: If there are many symbols(non-words) in prompt, like following cases, v0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: enerate random output if there are many symbols(not words) in prompt bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have an observation: If there are many symbols(non...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
