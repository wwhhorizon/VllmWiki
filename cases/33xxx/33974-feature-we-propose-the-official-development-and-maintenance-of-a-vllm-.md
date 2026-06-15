# vllm-project/vllm#33974: [Feature]: We propose the official development and maintenance of a VLLM integration or plugin within Dify.

| 字段 | 值 |
| --- | --- |
| Issue | [#33974](https://github.com/vllm-project/vllm/issues/33974) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: We propose the official development and maintenance of a VLLM integration or plugin within Dify.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We propose the official development and maintenance of a VLLM integration or plugin within Dify.Currently, the vLLM plugin in Dify only supports text-only LLMs. We currently require support for VL, Embedding, Rerank, VL-Embedding, and VL-Rerank, and hope that the official team can take over the maintenance of the vLLM plugin in Dify. https://github.com/vllm-project/vllm/issues/17454 https://github.com/yangyaofei/dify-vllm-provider/issues/4#issuecomment-2756218076 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: We propose the official development and maintenance of a VLLM integration or plugin within Dify. feature request ### 🚀 The feature, motivation and pitch We propose the official development and maintenance of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ent and maintenance of a VLLM integration or plugin within Dify. feature request ### 🚀 The feature, motivation and pitch We propose the official development and maintenance of a VLLM integration or plugin within Dify.Cu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
