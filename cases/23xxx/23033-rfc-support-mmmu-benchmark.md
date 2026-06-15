# vllm-project/vllm#23033: [RFC]: Support mmmu benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#23033](https://github.com/vllm-project/vllm/issues/23033) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support mmmu benchmark

### Issue 正文摘录

### Motivation. Supports MMMU benchmark. ### Proposed Change. This task will be divided into the following three pr - [ ] Support MMMU accuracy benchmark https://github.com/vllm-project/vllm/pull/23034 - [ ] Support MMMU accuracy check between `hf` and `vllm` in CI/CD - [ ] Support MMMU in `vllm bench` ### Feedback Period. _No response_ ### CC List. @ywang96 @DarkLight1337 ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [RFC]: Support mmmu benchmark RFC;stale ### Motivation. Supports MMMU benchmark. ### Proposed Change. This task will be divided into the following three pr - [ ] Support MMMU accuracy benchmark https://github.com/vllm-p...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: This task will be divided into the following three pr - [ ] Support MMMU accuracy benchmark https://github.com/vllm-project/vllm/pull/23034 - [ ] Support MMMU accuracy check between `hf` and `vllm` in CI/CD - [ ] Suppor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /pull/23034 - [ ] Support MMMU accuracy check between `hf` and `vllm` in CI/CD - [ ] Support MMMU in `vllm bench` ### Feedback Period. _No response_ ### CC List. @ywang96 @DarkLight1337 ### Any Other Things. _No respons...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /vllm-project/vllm/pull/23034 - [ ] Support MMMU accuracy check between `hf` and `vllm` in CI/CD - [ ] Support MMMU in `vllm bench` ### Feedback Period. _No response_ ### CC List. @ywang96 @DarkLight1337 ### Any Other T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
