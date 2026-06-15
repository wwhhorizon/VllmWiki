# vllm-project/vllm#13580: [Bug]: Has the official docker image not been scanned for vulnerabilities?

| 字段 | 值 |
| --- | --- |
| Issue | [#13580](https://github.com/vllm-project/vllm/issues/13580) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Has the official docker image not been scanned for vulnerabilities?

### Issue 正文摘录

### Your current environment docker pull vllm/vllm-openai:v0.7.2,Has the official docker image not been scanned for vulnerabilities?Whether the FRP carried in it is required for multi-machine deployment。After enabling image deployment, the server was attacked, and when tracing the cause, it was found that the FRP in the docker image was exploited. ![Image](https://github.com/user-attachments/assets/c0ee47d7-c157-4661-84da-78cb51d43fd2) I feel like this can be a hidden danger, so bring this up to avoid it. ### 🐛 Describe the bug I feel like this can be a hidden danger, so bring this up to avoid it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Has the official docker image not been scanned for vulnerabilities? bug ### Your current environment docker pull vllm/vllm-openai:v0.7.2,Has the official docker image not been scanned for vulnerabilities?Whether...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
