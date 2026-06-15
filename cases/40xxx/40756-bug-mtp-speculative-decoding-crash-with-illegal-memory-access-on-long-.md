# vllm-project/vllm#40756: [Bug]: MTP speculative decoding crash with illegal memory access on long sequences (Qwen3.6-27B-FP8, v0.19.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#40756](https://github.com/vllm-project/vllm/issues/40756) |
| 状态 | open |
| 标签 | bug |
| 评论 | 31; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MTP speculative decoding crash with illegal memory access on long sequences (Qwen3.6-27B-FP8, v0.19.1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description When using MTP speculative decoding (num_spec_tokens=5) with the FP8‑quantized Qwen3.6‑27B model as both target and draft model, the engine crashes on long requests. Environment vLLM version: 0.19.1 Model: Qwen3.6-27B-FP8 TP size: 4, fp8 quantization, prefix caching + chunked prefill enabled Speculative config: method=mtp, model=same as target, num_spec_tokens=5 Symptoms The crash occurs after the request has accumulated ~26 k total tokens and has generated >1200 output tokens. Just before the crash, spec metrics become abnormal: accepted tokens equal drafted tokens, acceptance rate jumps to 100%, and the scheduled draft tokens are all -1. All worker processes then fail with torch.AcceleratorError: CUDA error: an illegal memory access was encountered in gpu_model_runner.py line 1706 (prev_common_req_indices_tensor = torch.tensor(...)). Excerpt from logs SpecDecoding metrics: Mean acceptance length: 6.00, ..., Avg Draft acceptance rate: 100.0% scheduled_spec_decode_tokens={...: [-1, -1, -1, -1, -1]} ... torch.AcceleratorError: CUDA error: an illegal memory access was encountered File "gpu_model_runner.py", line 1706, i...

## 现有链接修复摘要

#42603 [Bugfix] Fix race condition in MTP speculative decoding draft loop | #43682 [Bugfix] Skip CUDA-graph padded positions in eagle draft step kernel

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: MTP speculative decoding crash with illegal memory access on long sequences (Qwen3.6-27B-FP8, v0.19.1) bug ### Your current environment ### 🐛 Describe the bug Description When using MTP speculative decoding (num_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: and draft model, the engine crashes on long requests. Environment vLLM version: 0.19.1 Model: Qwen3.6-27B-FP8 TP size: 4, fp8 quantization, prefix caching + chunked prefill enabled Speculative config: method=mtp, model=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: decoding crash with illegal memory access on long sequences (Qwen3.6-27B-FP8, v0.19.1) bug ### Your current environment ### 🐛 Describe the bug Description When using MTP speculative decoding (num_spec_tokens=5) with the...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ithout invalid draft tokens or illegal memory access. Additional notes GPU memory usage was low (~5.4% KV cache), so it’s not an OOM issue. The problem is reproducible; disabling speculative decoding avoids the crash. #...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: speculative decoding crash with illegal memory access on long sequences (Qwen3.6-27B-FP8, v0.19.1) bug ### Your current environment ### 🐛 Describe the bug Description When using MTP speculative decoding (num_spec_tokens...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42603](https://github.com/vllm-project/vllm/pull/42603) | closes_keyword | 0.95 | [Bugfix] Fix race condition in MTP speculative decoding draft loop | Fix #40756 A race condition in `vllm/v1/spec_decode/llm_base_proposer.py` that can trigger `cudaErrorIllegalAddress` under high concurrency when using MTP speculative decoding. |
| [#43682](https://github.com/vllm-project/vllm/pull/43682) | mentioned | 0.6 | [Bugfix] Skip CUDA-graph padded positions in eagle draft step kernel | an illegal memory access was encountered ``` Related issues: #39295, #40756 ## Test plan - [ ] Verify existing spec decode tests pass (`pytest tests/v1/spec_decode/`) - [ ] Run co… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
