# vllm-project/vllm#33092: [Accessory/Distributed] KV Transfer crashes with short prompts when chunked prefill is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#33092](https://github.com/vllm-project/vllm/issues/33092) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Accessory/Distributed] KV Transfer crashes with short prompts when chunked prefill is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Bug Description When running distributed inference with KV Transfer enabled (P2pNcclConnector) and Chunked Prefill enabled (--enable-chunked-prefill), the Producer (Rank 0) crashes with an AssertionError if it processes a short prompt that fits within a single scheduling step. The issue is located in (p2p_nccl_connector.py) within the (build_connector_meta) method. The code unconditionally asserts (assert req_id in self.chunked_prefill) when the role is producer. However, the scheduler logic determines that short requests do not need chunking and therefore does not register them in the (chunked_prefill) dictionary. This causes the assertion to fail when the connector attempts to build metadata for these requests. Steps to Reproduce 1. Start the Producer (Rank 0) Enable KV transfer and chunked prefill: python -m vllm.entrypoints.openai.api_server \ --model /path/to/your/model \ --port 8000 \ --enable-chunked-prefill \ --kv-transfer-config '{"kv_connector":"P2pNcclConnector","kv_role":"kv_producer","kv_rank":0,"kv_parallel_size":2}' 2. Start the Consumer (Rank 1) python -m vllm.entrypoints.openai.api_server \ --model /path/to/your/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: cessory/Distributed] KV Transfer crashes with short prompts when chunked prefill is enabled bug;stale ### Your current environment ### 🐛 Describe the bug Bug Description When running distributed inference with KV Transf...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: uling step. The issue is located in (p2p_nccl_connector.py) within the (build_connector_meta) method. The code unconditionally asserts (assert req_id in self.chunked_prefill) when the role is producer. However, the sche...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ... ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: . This causes the assertion to fail when the connector attempts to build metadata for these requests. Steps to Reproduce 1. Start the Producer (Rank 0) Enable KV transfer and chunked prefill: python -m vllm.entrypoints....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nd chunked prefill: python -m vllm.entrypoints.openai.api_server \ --model /path/to/your/model \ --port 8000 \ --enable-chunked-prefill \ --kv-transfer-config '{"kv_connector":"P2pNcclConnector","kv_role":"kv_producer",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
