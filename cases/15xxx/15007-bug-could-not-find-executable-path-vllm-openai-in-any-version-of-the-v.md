# vllm-project/vllm#15007: [Bug]: could not find executable path vllm-openai in any version of the vllm/vllm-openai:latestimage

| 字段 | 值 |
| --- | --- |
| Issue | [#15007](https://github.com/vllm-project/vllm/issues/15007) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: could not find executable path vllm-openai in any version of the vllm/vllm-openai:latestimage

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [Bug]: could not find executable path vllm-openai in any version of the vllm/vllm-openai:latestimage docker run -it --entrypoint /bin/bash vllm/vllm-openai:latest find / -name vllm-openai how to get this path/ please fix it, getting below error while executing it docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "vllm-openai": executable file not found in $PATH: unknown. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: could not find executable path vllm-openai in any version of the vllm/vllm-openai:latestimage bug ### Your current environment ### 🐛 Describe the bug [Bug]: could not find executable path vllm-openai in any versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: wn. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ind executable path vllm-openai in any version of the vllm/vllm-openai:latestimage bug ### Your current environment ### 🐛 Describe the bug [Bug]: could not find executable path vllm-openai in any version of the vllm/vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
