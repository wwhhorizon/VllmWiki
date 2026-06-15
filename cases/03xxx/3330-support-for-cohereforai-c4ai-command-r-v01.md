# vllm-project/vllm#3330: support for CohereForAI/c4ai-command-r-v01

| 字段 | 值 |
| --- | --- |
| Issue | [#3330](https://github.com/vllm-project/vllm/issues/3330) |
| 状态 | closed |
| 标签 | help wanted |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> support for CohereForAI/c4ai-command-r-v01

### Issue 正文摘录

[CohereForAI/c4ai-command-r-v01](https://huggingface.co/CohereForAI/c4ai-command-r-v01) is a large language model with open weights optimized for a variety of use cases including reasoning, summarization, and question answering. Command-R has the capability for multilingual generation evaluated in 10 languages and highly performant RAG capabilities.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: /c4ai-command-r-v01 help wanted [CohereForAI/c4ai-command-r-v01](https://huggingface.co/CohereForAI/c4ai-command-r-v01) is a large language model with open weights optimized for a variety of use cases including reasonin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ding reasoning, summarization, and question answering. Command-R has the capability for multilingual generation evaluated in 10 languages and highly performant RAG capabilities.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tion answering. Command-R has the capability for multilingual generation evaluated in 10 languages and highly performant RAG capabilities.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
