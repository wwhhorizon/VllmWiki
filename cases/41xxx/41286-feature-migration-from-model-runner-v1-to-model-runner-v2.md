# vllm-project/vllm#41286: [Feature]: Migration from Model Runner v1 to Model Runner v2

| 字段 | 值 |
| --- | --- |
| Issue | [#41286](https://github.com/vllm-project/vllm/issues/41286) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Migration from Model Runner v1 to Model Runner v2

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are going to migrate from model runner v1 to model runner v2 gradually, here is the roadmap: - Start with dense model, namely "Qwen/Qwen3-0.6B" and "facebook/opt-125m" as they covered most of the CI tests - Then, with moe model, like "deepseek-ai/DeepSeek-V2-lite" - Finally, test with popular model, like "deepseek-ai/DeepSeek-V4-Pro" Tasks: - [x] https://github.com/vllm-project/vllm/pull/39337 - [x] https://github.com/vllm-project/vllm/pull/39353 - [x] https://github.com/vllm-project/vllm/pull/39937 - [x] https://github.com/vllm-project/vllm/pull/40559 - [x] https://github.com/vllm-project/vllm/pull/40648 - [x] https://github.com/vllm-project/vllm/pull/41285 - [ ] ~https://github.com/vllm-project/vllm/pull/41667~ We temporally block this as there would be a big refactor for torch compile stuff recently - [x] https://github.com/vllm-project/vllm/pull/41761 - [x] https://github.com/vllm-project/vllm/pull/42538 @njhill - [ ] https://github.com/vllm-project/vllm/pull/43458 @njhill - [x] https://github.com/vllm-project/vllm/pull/42673 - [x] https://github.com/vllm-project/vllm/pull/42676 - [x] https://github.com/vllm-project/vllm/pull/42778 -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ly "Qwen/Qwen3-0.6B" and "facebook/opt-125m" as they covered most of the CI tests - Then, with moe model, like "deepseek-ai/DeepSeek-V2-lite" - Finally, test with popular model, like "deepseek-ai/DeepSeek-V4-Pro" Tasks:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Migration from Model Runner v1 to Model Runner v2 feature request ### 🚀 The feature, motivation and pitch We are going to migrate from model runner v1 to model runner v2 gradually, here is the roadmap: - Star...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: - [ ] ~https://github.com/vllm-project/vllm/pull/41667~ We temporally block this as there would be a big refactor for torch compile stuff recently - [x] https://github.com/vllm-project/vllm/pull/41761 - [x] https://gith...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: nd "facebook/opt-125m" as they covered most of the CI tests - Then, with moe model, like "deepseek-ai/DeepSeek-V2-lite" - Finally, test with popular model, like "deepseek-ai/DeepSeek-V4-Pro" Tasks: - [x] https://github....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
