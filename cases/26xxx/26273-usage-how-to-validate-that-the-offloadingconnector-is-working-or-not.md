# vllm-project/vllm#26273: [Usage]: How to validate that the OffloadingConnector  is working or not

| 字段 | 值 |
| --- | --- |
| Issue | [#26273](https://github.com/vllm-project/vllm/issues/26273) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to validate that the OffloadingConnector  is working or not

### Issue 正文摘录

We have the 10 H100 gpu with and deploying in the kubernetes cluster. and have 5 worker nodes. we are doing the --kv-transfer-config '{"kv_connector":"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_config":{"block_size": 64, "num_cpu_blocks": 1000}}' with the LLama4 maverick

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: etes cluster. and have 5 worker nodes. we are doing the --kv-transfer-config '{"kv_connector":"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_config":{"block_size": 64, "num_cpu_blocks": 1000}}' with the L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: at the OffloadingConnector is working or not usage;stale We have the 10 H100 gpu with and deploying in the kubernetes cluster. and have 5 worker nodes. we are doing the --kv-transfer-config '{"kv_connector":"OffloadingC...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: How to validate that the OffloadingConnector is working or not usage;stale We have the 10 H100 gpu with and deploying in the kubernetes cluster. and have 5 worker nodes. we are doing the --kv-transfer-config '{...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: :"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_config":{"block_size": 64, "num_cpu_blocks": 1000}}' with the LLama4 maverick
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: How to validate that the OffloadingConnector is working or not usage;stale We have the 10 H100 gpu with and deploying in the kubernetes cluster. and have 5 worker nodes. we are doing the --kv-transfer-config '{"kv_co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
