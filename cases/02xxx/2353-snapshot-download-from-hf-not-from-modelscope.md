# vllm-project/vllm#2353: snapshot download from HF not from modelscope

| 字段 | 值 |
| --- | --- |
| Issue | [#2353](https://github.com/vllm-project/vllm/issues/2353) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> snapshot download from HF not from modelscope

### Issue 正文摘录

since VLLM uses snapshot download from modelscope will not allow us to download private models , if it is implemented with snapshot download from HF it would be highly appreciable

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: snapshot download from HF not from modelscope since VLLM uses snapshot download from modelscope will not allow us to download private models , if it is implemented with snapshot download from HF it would be highly appre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: it is implemented with snapshot download from HF it would be highly appreciable

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
