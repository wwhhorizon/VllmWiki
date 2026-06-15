# vllm-project/vllm#3403: [Feature] Cohere Command-R support

| 字段 | 值 |
| --- | --- |
| Issue | [#3403](https://github.com/vllm-project/vllm/issues/3403) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Cohere Command-R support

### Issue 正文摘录

Hi, Command-R has 128K context, RAG support with Grounded generation and multilingual It seems a strong 35B model, especially in summarization of long texts, middle east languages and more. The model code is copied from Llama2 with minor modifications. Would it be possible to support it in VLLM ? Thanks,

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: support with Grounded generation and multilingual It seems a strong 35B model, especially in summarization of long texts, middle east languages and more. The model code is copied from Llama2 with minor modifications. Wo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: h Grounded generation and multilingual It seems a strong 35B model, especially in summarization of long texts, middle east languages and more. The model code is copied from Llama2 with minor modifications. Would it be p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
