# vllm-project/vllm#16262: [Feature]: ray logs too large

| 字段 | 值 |
| --- | --- |
| Issue | [#16262](https://github.com/vllm-project/vllm/issues/16262) |
| 状态 | closed |
| 标签 | feature request;ray;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: ray logs too large

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, I run docker version of vllm with following environment parametrs: -e RAY_ROTATION_MAX_BYTES=10241024 -e RAY_ROTATION_BACKUP_COUNT=1 but this doesn't help and still ray logs take up too much space ![Image](https://github.com/user-attachments/assets/7ddabb74-7069-4e6a-bdce-768d315876e9) what I should add more to parameters? is it possible to turn off this logging? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: re request;ray;stale ### 🚀 The feature, motivation and pitch Hi, I run docker version of vllm with following environment parametrs: -e RAY_ROTATION_MAX_BYTES=10241024 -e RAY_ROTATION_BACKUP_COUNT=1 but this doesn't help...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: ray logs too large feature request;ray;stale ### 🚀 The feature, motivation and pitch Hi, I run docker version of vllm with following environment parametrs: -e RAY_ROTATION_MAX_BYTES=10241024 -e RAY_ROTATION_B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
