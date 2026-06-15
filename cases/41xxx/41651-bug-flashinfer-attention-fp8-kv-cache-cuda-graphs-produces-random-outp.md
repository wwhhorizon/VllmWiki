# vllm-project/vllm#41651: [Bug]: FlashInfer attention + FP8 KV cache + CUDA graphs produces random output on RTX 6000 Pro Blackwell (sm_120); TRITON_ATTN backend works

| 字段 | 值 |
| --- | --- |
| Issue | [#41651](https://github.com/vllm-project/vllm/issues/41651) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer attention + FP8 KV cache + CUDA graphs produces random output on RTX 6000 Pro Blackwell (sm_120); TRITON_ATTN backend works

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary On **RTX 6000 Pro Blackwell** (sm_120), vLLM with **FlashInfer** attention, `--kv-cache-dtype fp8`, and the [`poolside/Laguna-XS.2-FP8`](https://huggingface.co/poolside/Laguna-XS.2-FP8) checkpoint (compressed-tensors `fp8_w8a8` weights with FP8 KV cache via `kv_cache_scheme`) produces **completely random output** on long prompts when `torch.compile` and CUDA graphs are enabled. Switching attention backend to `TRITON_ATTN` while holding everything else constant produces a **perfect coherent answer** to the same prompt. The bug is therefore localized to **FlashInfer's interaction with FP8 KV cache + CUDA graphs on sm_120**. The bug requires all of: 1. FP8 KV cache enabled (`--kv-cache-dtype fp8`) 2. `torch.compile` and CUDA graphs both enabled (i.e., not `--enforce-eager`) 3. **FlashInfer** attention backend (default on sm_120 in this build) 4. RTX 6000 Pro Blackwell (sm_120). H100 and B200 are clean under the same config. Short prompts (~30 tokens) are coherent on Blackwell across every config tested — the bug only manifests at longer context. ## Hardware matrix | Hardware | Backend | FP8 KV + compile + cudagraphs | Res...

## 现有链接修复摘要

#42580 [Bugfix] Fix fp8 kv cache scaling for the triton attention backend | #42650 [Bugfix] Source num_qo_heads from Attention layers in Flashinfer/Triton metadata builders | #43044 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | #43047 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Bug]: FlashInfer attention + FP8 KV cache + CUDA graphs produces random output on RTX 6000 Pro Blackwell (sm_120); TRITON_ATTN backend works bug ### Your current environment ### 🐛 Describe the bug ## Summary On **RTX 6...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: heme`) produces **completely random output** on long prompts when `torch.compile` and CUDA graphs are enabled. Switching attention backend to `TRITON_ATTN` while holding everything else constant produces a **perfect coh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: FlashInfer attention + FP8 KV cache + CUDA graphs produces random output on RTX 6000 Pro Blackwell (sm_120); TRITON_ATTN backend works bug ### Your current environment ### 🐛 Describe the bug ## Summary On **RTX 6...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: FlashInfer attention + FP8 KV cache + CUDA graphs produces random output on RTX 6000 Pro Blackwell (sm_120); TRITON_ATTN backend works bug ### Your current environment ### 🐛 Describe the bug ## Summary On **RTX 6...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: on, `--kv-cache-dtype fp8`, and the [`poolside/Laguna-XS.2-FP8`](https://huggingface.co/poolside/Laguna-XS.2-FP8) checkpoint (compressed-tensors `fp8_w8a8` weights with FP8 KV cache via `kv_cache_scheme`) produces **com...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42580](https://github.com/vllm-project/vllm/pull/42580) | closes_keyword | 0.95 | [Bugfix] Fix fp8 kv cache scaling for the triton attention backend | Fix fp8 kv cache scaling for the triton attention backend ## Purpose While reproducing #41651 (FlashInfer + FP8 KV cache + CUDA graphs) producing random output on `poolside/Lagu |
| [#42650](https://github.com/vllm-project/vllm/pull/42650) | closes_keyword | 0.95 | [Bugfix] Source num_qo_heads from Attention layers in Flashinfer/Triton metadata builders | Fixes #41651. And also fixes the illegal memory access error when serving that model with certain configs. The FlashInfer and Triton attention metadata builders source `num_qo_h |
| [#43044](https://github.com/vllm-project/vllm/pull/43044) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | _up` CuMemAllocator leaks. Runtime allocator bug, not JIT autotune. - #41651 — FlashInfer FP8 KV garbage output on SM_120. Numerical correctness in a different code path. - #41834… |
| [#43047](https://github.com/vllm-project/vllm/pull/43047) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | _up` CuMemAllocator leaks. Runtime allocator bug, not JIT autotune. - #41651 — FlashInfer FP8 KV garbage output on SM_120. Numerical correctness in a different code path. - #41834… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
