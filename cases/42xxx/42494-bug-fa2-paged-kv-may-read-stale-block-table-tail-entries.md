# vllm-project/vllm#42494: [Bug]: FA2 paged-KV may read stale block-table tail entries

| 字段 | 值 |
| --- | --- |
| Issue | [#42494](https://github.com/vllm-project/vllm/issues/42494) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FA2 paged-KV may read stale block-table tail entries

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary **Related to #42273.** I observed a possible robustness issue around FlashAttention-2 paged-KV reads and V1 worker block tables. In workloads with frequent request turnover in the persistent batch (requests finish and new requests reuse rows), inactive entries in a worker block-table row can retain old physical block ids. FA2's paged KV helper then appears able to dereference one of those entries on a partial-block boundary. Current outputs appear to remain correct because the corresponding logical positions are outside the request's valid sequence range and are masked/pruned before affecting softmax. I found related documentation in `vllm/v1/attention/backends/flex_attention.py::physical_to_logical_mapping` about garbage values in unused block-table positions and reused physical blocks for sliding window and hybrid attention. My question is whether there is a more general V1 contract between worker block tables and paged attention backends that makes this behavior intentional. ## Question for maintainers Is it an intended point that inactive block-table tail entries may contain stale physical block ids, as long as att...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: y **Related to #42273.** I observed a possible robustness issue around FlashAttention-2 paged-KV reads and V1 worker block tables. In workloads with frequent request turnover in the persistent batch (requests finish and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: andling. If not, it may be safer to make inactive block-table tails explicitly safe, e.g., zero/null them before they can be consumed by attention kernels. ## Actual behavior The worker `BlockTable` API updates active r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: FA2 paged-KV may read stale block-table tail entries bug ### Your current environment ### 🐛 Describe the bug ## Summary **Related to #42273.** I observed a possible robustness issue around FlashAttention-2 paged-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding attention;cache;cuda;kernel;operator;quantization;sampling;triton b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: FA2 paged-KV may read stale block-table tail entries bug ### Your current environment ### 🐛 Describe the bug ## Summary **Related to #42273.** I observed a possible robustness issue around FlashAttention-2 paged-...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
