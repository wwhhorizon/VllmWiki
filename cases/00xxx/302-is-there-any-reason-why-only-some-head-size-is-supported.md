# vllm-project/vllm#302: Is there any reason why only some head_size is supported?

| 字段 | 值 |
| --- | --- |
| Issue | [#302](https://github.com/vllm-project/vllm/issues/302) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is there any reason why only some head_size is supported?

### Issue 正文摘录

Hi, Thanks for awesome library. I tried to load model which has `head_size` is 256, but it is not supported yet. Attention code [here](https://github.com/vllm-project/vllm/blob/998d9d15095e7a69629f9e131c8b59bfdd1c6314/vllm/model_executor/layers/attention.py) only 4 type of `head_size` is supported. Is there any reason why `head_size=256` is not supported yet? Thanks! [Update] I checked the attention ops code [here](https://github.com/vllm-project/vllm/blob/998d9d15095e7a69629f9e131c8b59bfdd1c6314/csrc/attention/attention_kernels.cu#L396) and the comment said that to reduce compile time it allow only few head size. Therefore I uncomment it and recompile for the 256 head_size model, and it works well. I'll close this issue.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: attention/attention_kernels.cu#L396) and the comment said that to reduce compile time it allow only few head size. Therefore I uncomment it and recompile for the 256 head_size model, and it works well. I'll close this i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: head_size is supported? Hi, Thanks for awesome library. I tried to load model which has `head_size` is 256, but it is not supported yet. Attention code [here](https://github.com/vllm-project/vllm/blob/998d9d15095e7a6962...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
