# vllm-project/vllm#16402: [Bug]: CPU version cant run python3 with non-root user

| 字段 | 值 |
| --- | --- |
| Issue | [#16402](https://github.com/vllm-project/vllm/issues/16402) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CPU version cant run python3 with non-root user

### Issue 正文摘录

### Your current environment Use kubernetes with non-root user. Run vllm on CPU. ### 🐛 Describe the bug Same issue as [#15174](https://github.com/vllm-project/vllm/issues/15174) I'm using k8s to run vllm on CPU with non-root user. Use docker/Dockerfile.cpu to build the image, and here is the error message: Error: failed to create containerd task: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "python3": executable file not found in $PATH: unknown ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: CPU version cant run python3 with non-root user bug ### Your current environment Use kubernetes with non-root user. Run vllm on CPU. ### 🐛 Describe the bug Same issue as [#15174](https://github.com/vllm-project/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: own ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
