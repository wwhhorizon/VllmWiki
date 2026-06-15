# vllm-project/vllm#38551: [Bug]: AssertionError: Encoder cache miss crashes engine with MTP + multimodal under high concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#38551](https://github.com/vllm-project/vllm/issues/38551) |
| 状态 | open |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | fp8;gemm |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError: Encoder cache miss crashes engine with MTP + multimodal under high concurrency

### Issue 正文摘录

### Your current environment - **vLLM version:** v0.18.0 - **Model:** Qwen/Qwen3.5-27B-FP8 - **GPU:** NVIDIA L40S (48GB) - **OS:** Linux (EKS, Ubuntu-based) ### Bug description When using **MTP speculative decoding** (not EAGLE3) with multimodal (vision) inputs under sustained high-concurrency production traffic, the engine crashes with: ``` AssertionError: Encoder cache miss for ``` The crash originates in `gpu_model_runner.py` during `propose_draft_token_ids` → `_gather_mm_embeddings`. Under heavy load, the encoder cache evicts entries that MTP still needs for draft token proposal, causing a fatal assertion that kills the entire engine and drops all in-flight requests. This is **distinct from #32469** (fixed by #34220), which addressed EAGLE3 + `disable_chunked_mm_input`. In that case, encoder inputs were never scheduled. In our case, the entries are produced and cached correctly, but get **evicted under memory pressure** before MTP's draft proposer reads them. ### How to reproduce **Flags:** ``` --speculative-config.method mtp --speculative-config.num_speculative_tokens 1 --enable-chunked-prefill --enable-prefix-caching --enforce-eager --gpu-memory-utilization 0.90 --max-model-...

## 现有链接修复摘要

#39544 [Bugfix][V1] Retain encoder cache entries for multimodal models under async scheduling

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: AssertionError: Encoder cache miss crashes engine with MTP + multimodal under high concurrency ### Your current environment - **vLLM version:** v0.18.0 - **Model:** Qwen/Qwen3.5-27B-FP8 - **GPU:** NVIDIA L40S (48...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: **OS:** Linux (EKS, Ubuntu-based) ### Bug description When using **MTP speculative decoding** (not EAGLE3) with multimodal (vision) inputs under sustained high-concurrency production traffic, the engine crashes with: ``...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: multimodal under high concurrency ### Your current environment - **vLLM version:** v0.18.0 - **Model:** Qwen/Qwen3.5-27B-FP8 - **GPU:** NVIDIA L40S (48GB) - **OS:** Linux (EKS, Ubuntu-based) ### Bug description When usi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: t environment - **vLLM version:** v0.18.0 - **Model:** Qwen/Qwen3.5-27B-FP8 - **GPU:** NVIDIA L40S (48GB) - **OS:** Linux (EKS, Ubuntu-based) ### Bug description When using **MTP speculative decoding** (not EAGLE3) with...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: AssertionError: Encoder cache miss crashes engine with MTP + multimodal under high concurrency ### Your current environment - **vLLM version:** v0.18.0 - **Model:** Qwen/Qwen3.5-27B-FP8 - **GPU:** NVIDIA L40S (48...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39544](https://github.com/vllm-project/vllm/pull/39544) | mentioned | 0.6 | [Bugfix][V1] Retain encoder cache entries for multimodal models under async scheduling | 7 (intra-step reorder), #38622 (graceful skip, based on workaround in #38551) ## Evidence Tested on Qwen3.5-VL-27B-FP8 + MTP on L40S, vLLM v0.19.1. **The bug exists without this |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
