# vllm-project/vllm#978: Not able to use fine tunned model uploaded on higgingface

| 字段 | 值 |
| --- | --- |
| Issue | [#978](https://github.com/vllm-project/vllm/issues/978) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Not able to use fine tunned model uploaded on higgingface

### Issue 正文摘录

I have fine tuned llama 7b and falcon 7b models on Auto train of hugging face and both models are uploaded on hogging face on public repository but while loading the model in VLLM I am getting following error oserror : swapnilborude/falcon_7b_autotrain does not appear to have a file named config.json. I have then tried uploading config.json file from tiiuae/falcon-7b but still I am getting the same issue Any help on this will be really appreciable Thank you so much

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Not able to use fine tunned model uploaded on higgingface I have fine tuned llama 7b and falcon 7b models on Auto train of hugging face and both models are uploaded on hogging face on public repository but while loading...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t still I am getting the same issue Any help on this will be really appreciable Thank you so much

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
