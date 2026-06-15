# vllm-project/vllm#1897: How to load local llm and refit the weights of LLM Engine?

| 字段 | 值 |
| --- | --- |
| Issue | [#1897](https://github.com/vllm-project/vllm/issues/1897) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to load local llm and refit the weights of LLM Engine?

### Issue 正文摘录

Hi, we are https://github.com/OpenLLMAI/OpenRLHF We want to integrate vLLM with OpenRLHF to support large models In RLHF we need to re-fit the weight of LLM models during the training We even need to free the vLLM GPU memory to leave more memory for training, but not destroy the vLLM object And then we can refit the LLM model weights from the training framework. thx for your reply!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the weights of LLM Engine? Hi, we are https://github.com/OpenLLMAI/OpenRLHF We want to integrate vLLM with OpenRLHF to support large models In RLHF we need to re-fit the weight of LLM models during the training We even...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e weight of LLM models during the training We even need to free the vLLM GPU memory to leave more memory for training, but not destroy the vLLM object And then we can refit the LLM model weights from the training framew...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
