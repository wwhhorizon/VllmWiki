# vllm-project/vllm#1246: The performance is not satisfactory!

| 字段 | 值 |
| --- | --- |
| Issue | [#1246](https://github.com/vllm-project/vllm/issues/1246) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The performance is not satisfactory!

### Issue 正文摘录

Using Baichuan 13B and following the documentation to launch the openai_api script, the speed has improved . However, the actual performance is vastly different from the native Hugging Face model. I've tried debugging many aspects without success. Has the author conducted any relevant tests? Are there any usage instructions specifically for Baichuan 13B?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: author conducted any relevant tests? Are there any usage instructions specifically for Baichuan 13B?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: the actual performance is vastly different from the native Hugging Face model. I've tried debugging many aspects without success. Has the author conducted any relevant tests? Are there any usage instructions specificall...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ging many aspects without success. Has the author conducted any relevant tests? Are there any usage instructions specifically for Baichuan 13B?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
