# vllm-project/vllm#1229: Support for grammar

| 字段 | 值 |
| --- | --- |
| Issue | [#1229](https://github.com/vllm-project/vllm/issues/1229) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for grammar

### Issue 正文摘录

It would be highly beneficial if the library could incorporate support for Grammar and GBNF files. https://github.com/ggerganov/llama.cpp/blob/master/grammars/README.md

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Support for grammar It would be highly beneficial if the library could incorporate support for Grammar and GBNF files. https://github.com/ggerganov/llama.cpp/blob/master/grammars/README.md
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rporate support for Grammar and GBNF files. https://github.com/ggerganov/llama.cpp/blob/master/grammars/README.md

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
