# vllm-project/vllm#1585: Dolly V2 : instruction following pipeline support in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#1585](https://github.com/vllm-project/vllm/issues/1585) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Dolly V2 : instruction following pipeline support in vLLM

### Issue 正文摘录

Hello everyone, I'm deploying some models leveraging vLLM and triton, and have been successful with a lot of them. However today I have some issue deploying dolly-v2-12b https://huggingface.co/databricks/dolly-v2-12b. Everything deploys but I get very rubbish response from the LLM. It is because it is not using the custom instruction following pipeline here https://huggingface.co/databricks/dolly-v2-12b/blob/main/instruct_pipeline.py. I've tried setting trust-remote-code (https://github.com/vllm-project/vllm/blob/1a2bbc930135cd3b94fbff2aafbdf5c568acc8bd/vllm/engine/arg_utils.py#L76), but it hasn't changed anything. My guess would be that I'm stuck with transformers.pipeline() to use this custom instruction pipeline. Is there a way to use vLLM and use this instruct pipeline ?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: following pipeline support in vLLM Hello everyone, I'm deploying some models leveraging vLLM and triton, and have been successful with a lot of them. However today I have some issue deploying dolly-v2-12b https://huggin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: in vLLM Hello everyone, I'm deploying some models leveraging vLLM and triton, and have been successful with a lot of them. However today I have some issue deploying dolly-v2-12b https://huggingface.co/databricks/dolly-v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
