# vllm-project/vllm#10878: [Feature]: Publish vllm-tpu image to dockerhub

| 字段 | 值 |
| --- | --- |
| Issue | [#10878](https://github.com/vllm-project/vllm/issues/10878) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Publish vllm-tpu image to dockerhub

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Users of the TPU image must currently manually build their own image. Similar ask to https://github.com/vllm-project/vllm/issues/4771 but for TPU image. Ideally CI/CD would automatically push the image on vllm release cuts and nightly (or vllm-tpu release cadence). Existing TPU ci test https://github.com/vllm-project/vllm/blob/main/.buildkite/run-tpu-test.sh ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: Publish vllm-tpu image to dockerhub feature request ### 🚀 The feature, motivation and pitch Users of the TPU image must currently manually build their own image. Similar ask to https://github.com/vllm-project...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Publish vllm-tpu image to dockerhub feature request ### 🚀 The feature, motivation and pitch Users of the TPU image must currently manually build their own image. Similar ask to https://github.com/vllm-project...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: release cuts and nightly (or vllm-tpu release cadence). Existing TPU ci test https://github.com/vllm-project/vllm/blob/main/.buildkite/run-tpu-test.sh ### Alternatives _No response_ ### Additional context _No response_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
