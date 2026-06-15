# vllm-project/vllm#4884: [Bug]: Too strict version requirement on `tiktoken`

| 字段 | 值 |
| --- | --- |
| Issue | [#4884](https://github.com/vllm-project/vllm/issues/4884) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Too strict version requirement on `tiktoken`

### Issue 正文摘录

### Your current environment _environment not relevant here_ ### 🐛 Describe the bug VLLM has a [strict requirement on using `tiktoken==0.6.0`](https://github.com/vllm-project/vllm/blob/33e0823de583819f39e88c39ea3f7dd4e07c3990/requirements-common.txt#L17), to cater to the DBRX tokeniser. However, this means that we cannot use vLLM in the same environment as the newest `tiktoken`, which includes support for OpenAI's GPT-4o model. Is there a reason for this strict requirement, or could it be relaxed to `>=0.6.0` instead?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Too strict version requirement on `tiktoken` bug ### Your current environment _environment not relevant here_ ### 🐛 Describe the bug VLLM has a [strict requirement on using `tiktoken==0.6.0`](https://github.com/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ent as the newest `tiktoken`, which includes support for OpenAI's GPT-4o model. Is there a reason for this strict requirement, or could it be relaxed to `>=0.6.0` instead?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
