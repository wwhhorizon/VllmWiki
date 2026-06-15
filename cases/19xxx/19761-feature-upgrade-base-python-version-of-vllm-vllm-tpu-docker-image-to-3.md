# vllm-project/vllm#19761: [Feature]: Upgrade base Python version of vllm/vllm-tpu docker image to 3.11+

| 字段 | 值 |
| --- | --- |
| Issue | [#19761](https://github.com/vllm-project/vllm/issues/19761) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Upgrade base Python version of vllm/vllm-tpu docker image to 3.11+

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Summary Please upgrade the default Python version in the vllm/vllm-tpu Docker image from Python 3.10 to at least Python 3.11. Motivation Python 3.11 includes substantial performance improvements and new language features such as typing.Self, which is now used by many modern Python projects and ML frameworks. The current Python 3.10 base causes compatibility issues and requires users to manage Python versions manually within the container. Benefits • Unlocks performance benefits from CPython 3.11 optimizations • Enables use of newer typing features (e.g., Self) • Reduces friction for users relying on Python 3.11+ packages • Aligns with broader ecosystem migration trends (e.g., PyTorch, JAX, Hugging Face) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Upgrade base Python version of vllm/vllm-tpu docker image to 3.11+ feature request;stale ### 🚀 The feature, motivation and pitch Summary Please upgrade the default Python version in the vllm/vllm-tpu Docker i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: grade base Python version of vllm/vllm-tpu docker image to 3.11+ feature request;stale ### 🚀 The feature, motivation and pitch Summary Please upgrade the default Python version in the vllm/vllm-tpu Docker image from Pyt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
