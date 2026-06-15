# vllm-project/vllm#39766: [RFC]: Support Mooncake Based ECConnector for EPD

| 字段 | 值 |
| --- | --- |
| Issue | [#39766](https://github.com/vllm-project/vllm/issues/39766) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Support Mooncake Based ECConnector for EPD

### Issue 正文摘录

### Motivation. vLLM's **EPD (Encoder-Prefill-Decode)** disaggregation feature allows running vision encoders on separate instances from the language model prefill/decode stages. This enables independent scaling, lower TTFT for text-only requests, and cross-process reuse of encoder outputs. The current EPD implementation uses `ECExampleConnector`, a file-based connector suitable for debugging and experimentation. For production deployments, we need a high-performance connector that supports multiple network transports (TCP, RDMA, SHM/NVLink). `MooncakeECConnector` addresses this by leveraging the Mooncake TransferEngine, which provides a unified API across multiple transport backends. **Key Challenge:** Unlike KV Cache transfer (where block memory is pre-allocated at fixed addresses), encoder cache tensors are dynamically allocated with variable sizes. Each multimodal input produces an encoder output of different dimensions depending on image resolution, model architecture, etc. Mooncake's TransferEngine requires pre-registered memory for efficient transfers, so we introduce an `EmbedBlockManager` with a pre-registered GPU buffer. **Related Discussions:** - https://github.com/vllm...

## 现有链接修复摘要

#40695 [EC Connector] Mooncake EC Connector for Distributed Encoder-Cache Transfer

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e allows running vision encoders on separate instances from the language model prefill/decode stages. This enables independent scaling, lower TTFT for text-only requests, and cross-process reuse of encoder outputs. The...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ake Based ECConnector for EPD RFC ### Motivation. vLLM's **EPD (Encoder-Prefill-Decode)** disaggregation feature allows running vision encoders on separate instances from the language model prefill/decode stages. This e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ce connector that supports multiple network transports (TCP, RDMA, SHM/NVLink). `MooncakeECConnector` addresses this by leveraging the Mooncake TransferEngine, which provides a unified API across multiple transport back...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: transport backends. **Key Challenge:** Unlike KV Cache transfer (where block memory is pre-allocated at fixed addresses), encoder cache tensors are dynamically allocated with variable sizes. Each multimodal input produc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: oder output of different dimensions depending on image resolution, model architecture, etc. Mooncake's TransferEngine requires pre-registered memory for efficient transfers, so we introduce an `EmbedBlockManager` with a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40695](https://github.com/vllm-project/vllm/pull/40695) | mentioned | 0.6 | [EC Connector] Mooncake EC Connector for Distributed Encoder-Cache Transfer | der-cache data in EPD-style disaggregation. Compared to the issue [#39766](https://github.com/vllm-project/vllm/issues/39766), this implementation takes a minimal-surface-area app… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
