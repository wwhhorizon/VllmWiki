# vllm-project/vllm#41969: [Bug]: AsyncLLM silent-hangs on multimodal pooling requests when default max_num_batched_tokens too small (L4); sync LLM works on same hardware

| 字段 | 值 |
| --- | --- |
| Issue | [#41969](https://github.com/vllm-project/vllm/issues/41969) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | gemm |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: AsyncLLM silent-hangs on multimodal pooling requests when default max_num_batched_tokens too small (L4); sync LLM works on same hardware

### Issue 正文摘录

### Summary On vLLM 0.19.1 + NVIDIA L4 24 GB + a multimodal pooling model with a video request: - `LLM.embed(...)` (sync) → returns in ~11 s ✓ - `AsyncLLM.encode(...)` → **silent hang** (no log lines, no error, never returns) ✗ Same hardware, same model, same request payload, same vLLM version — only the engine context differs. ### Root cause (per investigation) `EngineArgs.get_batch_defaults` (`vllm/engine/arg_utils.py:2050-2105`) picks different `max_num_batched_tokens` defaults based on device-memory-tier × engine-context: | device | engine context | default `max_num_batched_tokens` | |---|---|---| | L4 24 GB | `LLM_CLASS` (sync) | 8192 | | L4 24 GB | `ENGINE_CONTEXT` (AsyncLLM) | **2048** | | A100 80 GB | both | 8192 / 16384 | Pooling models force `enable_chunked_prefill=False`, and the encoder cache is sized from `max_num_batched_tokens` (→ 4096 on L4 async). A 32-frame `sample_demo_1.mp4` (native 360×640) video request produces more encoder tokens than this cache. The early-reject added in #33110 doesn't fire on this path — the request enters the scheduler and `_try_schedule_encoder_inputs` loops with `num_new_tokens=0` forever. ### Repro ```python import asyncio, decord, nu...

## 现有链接修复摘要

#33110 [Bugfix] Early-reject requests with MM data longer than encode cache capacity

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: AsyncLLM silent-hangs on multimodal pooling requests when default max_num_batched_tokens too small (L4); sync LLM works on same hardware ### Summary On vLLM 0.19.1 + NVIDIA L4 24 GB + a multimodal pooling model w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r returns) ✗ Same hardware, same model, same request payload, same vLLM version — only the engine context differs. ### Root cause (per investigation) `EngineArgs.get_batch_defaults` (`vllm/engine/arg_utils.py:2050-2105`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n, fps = len(vr), vr.get_avg_fps() idxs = np.linspace(0, n - 1, num=32, dtype=int) frames = vr.get_batch(idxs).asnumpy() meta = {"fps": fps, "duration": n / fps, "total_frames": n, "do_sample_frames": False} req = {"pro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: AsyncLLM silent-hangs on multimodal pooling requests when default max_num_batched_tokens too small (L4); sync LLM works on same hardware ### Summary On vLLM 0.19.1 + NVIDIA L4 24 GB + a multimodal pooling model w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s on multimodal pooling requests when default max_num_batched_tokens too small (L4); sync LLM works on same hardware ### Summary On vLLM 0.19.1 + NVIDIA L4 24 GB + a multimodal pooling model with a video request: - `LLM...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33110](https://github.com/vllm-project/vllm/pull/33110) | mentioned | 0.45 | [Bugfix] Early-reject requests with MM data longer than encode cache capacity | nt hang when video frames exceed profiled encoder budget) — closed by #33110 - #25890 (infinite empty scheduling on large mm input) — historic ### environment - `g2-standard-8` (1… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
