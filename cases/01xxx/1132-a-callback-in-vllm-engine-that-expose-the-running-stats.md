# vllm-project/vllm#1132: A callback in vLLM engine that expose the running stats

| 字段 | 值 |
| --- | --- |
| Issue | [#1132](https://github.com/vllm-project/vllm/issues/1132) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> A callback in vLLM engine that expose the running stats

### Issue 正文摘录

While working on adding vLLM support in [Triton Inference Server](https://github.com/triton-inference-server/tutorials/blob/main/Quick_Deploy/vLLM/README.md), we found that it would be beneficial for us to track certain stats like the following: - infligtht count - max infligtht capacity - kv cache blocks in use - total kv cache blocks It would be great if vllm engine can take an optional callback function as input which will expose these stats. These stats can then be exported to Prometheus metrics. In a production environment, this information would be useful in routing requests to different instances of vLLM engines running on different machines. Let me know if there is any alternative way of reliably obtaining this information from a vLLM engine.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e that expose the running stats While working on adding vLLM support in [Triton Inference Server](https://github.com/triton-inference-server/tutorials/blob/main/Quick_Deploy/vLLM/README.md), we found that it would be be...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: g: - infligtht count - max infligtht capacity - kv cache blocks in use - total kv cache blocks It would be great if vllm engine can take an optional callback function as input which will expose these stats. These stats...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /blob/main/Quick_Deploy/vLLM/README.md), we found that it would be beneficial for us to track certain stats like the following: - infligtht count - max infligtht capacity - kv cache blocks in use - total kv cache blocks...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: - infligtht count - max infligtht capacity - kv cache blocks in use - total kv cache blocks It would be great if vllm engine can take an optional callback function as input which will expose these stats. These stats can...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n be exported to Prometheus metrics. In a production environment, this information would be useful in routing requests to different instances of vLLM engines running on different machines. Let me know if there is any al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
