# vllm-project/vllm#506: How to config the gpu utilization rate after build.

| 字段 | 值 |
| --- | --- |
| Issue | [#506](https://github.com/vllm-project/vllm/issues/506) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to config the gpu utilization rate after build.

### Issue 正文摘录

Hi team, thanks for making this product and I am glad to see huggingface text-generation-inference(tgi) has support on it. For my understanding, they only use vllm vllm_cache_ops and vllm_attention_ops. However, the vllm reserved a lot of gpu memory beforehand making the model out of memory. I wonder if there is any config I can made after the build, or not through the model LLM interface to specify the memory usage or gpu utilization rate? Thanks

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: How to config the gpu utilization rate after build. Hi team, thanks for making this product and I am glad to see huggingface text-generation-inference(tgi) has support on it. For my understanding, they only use vllm vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: How to config the gpu utilization rate after build. Hi team, thanks for making this product and I am glad to see huggingface text-generation-inference(tgi) has support on it. For my understanding, they only use vllm vll...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: m_cache_ops and vllm_attention_ops. However, the vllm reserved a lot of gpu memory beforehand making the model out of memory. I wonder if there is any config I can made after the build, or not through the model LLM inte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
