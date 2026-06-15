# vllm-project/vllm#961: [Feature] Support the new version of baichuan2

| 字段 | 值 |
| --- | --- |
| Issue | [#961](https://github.com/vllm-project/vllm/issues/961) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Support the new version of baichuan2

### Issue 正文摘录

`baichuan-inc` released a new version of `Baichuan2-13B-Chat` today. There should be a problem with the calculation of prompt tokens when the existing code is tested reference: https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature] Support the new version of baichuan2 `baichuan-inc` released a new version of `Baichuan2-13B-Chat` today. There should be a problem with the calculation of prompt tokens when the existing code is tested refere...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ion of prompt tokens when the existing code is tested reference: https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: problem with the calculation of prompt tokens when the existing code is tested reference: https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
