# vllm-project/vllm#36780: [RFC][NixlConnector]: Add support for hybrid SSM-FA models

| 字段 | 值 |
| --- | --- |
| Issue | [#36780](https://github.com/vllm-project/vllm/issues/36780) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][NixlConnector]: Add support for hybrid SSM-FA models

### Issue 正文摘录

### Motivation. # Problem Statement Supporting hybrid models that combine FullAttention (FA) and Mamba-style SSM layers introduces several challenges for the KV connector: - FA and Mamba layers use different internal state layouts (K/V vs Conv/SSM). - Kernel constraints may require physical block sizes that differ from the logical block abstraction used by the block manager. As a result, FA and Mamba layers must be able to index the same underlying KV cache tensor while using different block descriptor layouts. ## Proposed Design We introduce **two logical descriptor views over the same registered memory regions**: - **Current descriptor view** (used by non-Mamba layers) - Descriptors correspond to K/V blocks - **Mamba descriptor view** (used by Mamba layers) - Descriptors correspond to Conv and SSM state blocks Both descriptor sets reference the same underlying tensor but use different offsets and sizes. The descriptor lists are stored continuously, allowing the existing `block_id → desc_id` mapping logic to be extended with a simple index shift. **All changes proposed here are not meant to modify the existing workflow for "regular" models, but rather extend it for this specific...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: r the KV connector: - FA and Mamba layers use different internal state layouts (K/V vs Conv/SSM). - Kernel constraints may require physical block sizes that differ from the logical block abstraction used by the block ma...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: existing workflow for "regular" models, but rather extend it for this specific case.** PR here https://github.com/vllm-project/vllm/pull/36687. ### Proposed Change. # Prerequisite This PR builds on the recently introduc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ect/vllm/blob/545d18d81bf11761e51c2b11a006573c2ae366c1/vllm/v1/attention/backends/flashinfer.py#L304) of backends, resulting physical tensor may actually be represented with a different number of blocks wrt what the log...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC][NixlConnector]: Add support for hybrid SSM-FA models RFC ### Motivation. # Problem Statement Supporting hybrid models that combine FullAttention (FA) and Mamba-style SSM layers introduces several challenges for th...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: a result, FA and Mamba layers must be able to index the same underlying KV cache tensor while using different block descriptor layouts. ## Proposed Design We introduce **two logical descriptor views over the same regist...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
