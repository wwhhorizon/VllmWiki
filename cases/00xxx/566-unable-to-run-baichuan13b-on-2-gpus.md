# vllm-project/vllm#566: Unable to run baichuan13b on 2 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#566](https://github.com/vllm-project/vllm/issues/566) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Unable to run baichuan13b on 2 GPUs

### Issue 正文摘录

Hi, I have 2 4090, each one of them can not fully load a 13b model, but vllm unable to automatically locate model into 2 GPUs, what else need I specific? (I have set a 0.8 GPU frac due to one GPU have a tiny process running consumes about 1GB mem)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lm unable to automatically locate model into 2 GPUs, what else need I specific? (I have set a 0.8 GPU frac due to one GPU have a tiny process running consumes about 1GB mem)
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: model, but vllm unable to automatically locate model into 2 GPUs, what else need I specific? (I have set a 0.8 GPU frac due to one GPU have a tiny process running consumes about 1GB mem)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: b on 2 GPUs Hi, I have 2 4090, each one of them can not fully load a 13b model, but vllm unable to automatically locate model into 2 GPUs, what else need I specific? (I have set a 0.8 GPU frac due to one GPU have a tiny...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
