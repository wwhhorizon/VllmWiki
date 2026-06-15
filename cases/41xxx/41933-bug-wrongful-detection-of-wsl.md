# vllm-project/vllm#41933: [Bug]: Wrongful detection of WSL

| 字段 | 值 |
| --- | --- |
| Issue | [#41933](https://github.com/vllm-project/vllm/issues/41933) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Wrongful detection of WSL

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The [current detection of WSL system](https://github.com/vllm-project/vllm/blob/v0.20.1/vllm/platforms/interface.py#L33-L35) is done as : ```python "microsoft" in " ".join(platform.uname()).lower() ``` This means in particular that a system whose hostname contains `microsoft` is detected as WSL. However, it's quite common to have Pods whose names contain `microsoft` in Kubernetes for example. Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
