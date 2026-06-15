# vllm-project/vllm#43716: [Bug][Spec Decode][Multimodal] EAGLE FULL prefill CUDA graph drops mm_inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#43716](https://github.com/vllm-project/vllm/issues/43716) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | activation;cuda;gemm;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][Spec Decode][Multimodal] EAGLE FULL prefill CUDA graph drops mm_inputs

### Issue 正文摘录

### What looks wrong On current `main` (`6e503868caa46f3afa87e8d3365495464fd75fb3`), the V1 EAGLE draft prefill FULL CUDA graph path appears to drop multimodal draft inputs. Static path: - `GPUModelRunner` gathers draft `mm_inputs` when `self.speculator.supports_mm_inputs` is true and passes them into `speculator.propose()`: - `vllm/v1/worker/gpu/model_runner.py:1293` - `vllm/v1/worker/gpu/model_runner.py:1342` - `EagleSpeculator.run_model()` uses `mm_inputs` to build `inputs_embeds`: - `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py:192` - `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py:207` - The eager prefill path passes `mm_inputs=mm_inputs`: - `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py:561` - The FULL graph draft-prefill path calls `self.prefill_cudagraph_manager.run_fullgraph(prefill_batch_desc)` without `mm_inputs`: - `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py:549` - `PrefillEagleCudaGraphManager.capture()` also captures `forward_fn(..., cg_mode)` without `mm_inputs`: - `vllm/v1/worker/gpu/spec_decode/eagle/cudagraph.py:64` This means a multimodal-capable EAGLE draft model can build image-specific draft embeddings in eager mode, but FULL graph capt...

## 现有链接修复摘要

#22872 [Multimodal][Speculative Decoding]Eagle Eagle3 mm support, enablement on qwen2.5vl | #29594 [Multimodal][Speculative Decoding]Eagle3 mm support, enablement on qwen3vl

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug][Spec Decode][Multimodal] EAGLE FULL prefill CUDA graph drops mm_inputs ### What looks wrong On current `main` (`6e503868caa46f3afa87e8d3365495464fd75fb3`), the V1 EAGLE draft prefill FULL CUDA graph path appears t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug][Spec Decode][Multimodal] EAGLE FULL prefill CUDA graph drops mm_inputs ### What looks wrong On current `main` (`6e503868caa46f3afa87e8d3365495464fd75fb3`), the V1 EAGLE draft prefill FULL CUDA graph path appears t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: odel_runner.py:1342` - `EagleSpeculator.run_model()` uses `mm_inputs` to build `inputs_embeds`: - `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py:192` - `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py:207` - The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][Spec Decode][Multimodal] EAGLE FULL prefill CUDA graph drops mm_inputs ### What looks wrong On current `main` (`6e503868caa46f3afa87e8d3365495464fd75fb3`), the V1 EAGLE draft prefill FULL CUDA graph path appears t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: mpling_logits;scheduler_memory;speculative_decoding activation;cuda;gemm;triton build_error dtype;env_dependency;race_condition;shape #22872 [Multimodal][Speculative Decoding]Eagle Eagle3 mm support, enablement on qwen2...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#22872](https://github.com/vllm-project/vllm/pull/22872) | mentioned | 0.45 | [Multimodal][Speculative Decoding]Eagle Eagle3 mm support, enablement on qwen2.5vl | modal eagle full cudagraph` related but not duplicate work i saw: - #22872, multimodal eagle/eagle3 enablement on qwen2.5-vl - #29594, multimodal eagle3 enablement on qwen3-vl i u… |
| [#29594](https://github.com/vllm-project/vllm/pull/29594) | mentioned | 0.45 | [Multimodal][Speculative Decoding]Eagle3 mm support, enablement on qwen3vl | i saw: - #22872, multimodal eagle/eagle3 enablement on qwen2.5-vl - #29594, multimodal eagle3 enablement on qwen3-vl i used a forced minimal repro rather than a public checkpoint.… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
