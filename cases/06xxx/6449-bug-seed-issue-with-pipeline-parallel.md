# vllm-project/vllm#6449: [Bug]: Seed issue with Pipeline Parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#6449](https://github.com/vllm-project/vllm/issues/6449) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Seed issue with Pipeline Parallel

### Issue 正文摘录

### Your current environment v0.5.1 ### 🐛 Describe the bug OpenAI API specifies that you can provide a seed: https://platform.openai.com/docs/api-reference/chat/create#chat-create-seed This allows reproducibility for example with non-zero temperature parameter. Currently, any state information is stored/advanced on the driver process only. We need to extend this to the worker actually doing the sampling.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Your current environment v0.5.1 ### 🐛 Describe the bug OpenAI API specifies that you can provide a seed: https://platform.openai.com/docs/api-reference/chat/create#chat-create-seed This allows reproducibility for exampl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: for example with non-zero temperature parameter. Currently, any state information is stored/advanced on the driver process only. We need to extend this to the worker actually doing the sampling.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
