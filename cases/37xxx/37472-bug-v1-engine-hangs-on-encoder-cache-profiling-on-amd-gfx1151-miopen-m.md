# vllm-project/vllm#37472: [Bug] V1 engine hangs on encoder cache profiling on AMD gfx1151 (MIOpen missing solver DB)

| 字段 | 值 |
| --- | --- |
| Issue | [#37472](https://github.com/vllm-project/vllm/issues/37472) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;hardware_porting;model_support;moe;multimodal_vlm |
| 子分类 | cold_start |
| Operator 关键词 | gemm;kernel;moe |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] V1 engine hangs on encoder cache profiling on AMD gfx1151 (MIOpen missing solver DB)

### Issue 正文摘录

## Description vLLM V1 engine hangs indefinitely during initialization when serving any model with a vision encoder on AMD gfx1151 (Strix Halo / Radeon 8060S). The hang occurs at encoder cache profiling where `embed_multimodal()` triggers MIOpen convolution operations that never complete. ## Environment - **GPU:** AMD Radeon 8060S (gfx1151, RDNA 3.5 iGPU, 128GB unified LPDDR5X) - **vLLM:** 0.17.1rc1.dev169 and 0.17.2rc1.dev71 - **PyTorch:** 2.10-2.12 (TheRock nightlies for gfx1151) - **ROCm:** TheRock 7.11-7.13 nightlies - **OS:** Fedora 43 ## Reproduction ```bash vllm serve Qwen/Qwen3.5-35B-A3B --enforce-eager --dtype float16 --trust-remote-code ``` Server logs show: ``` INFO: Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size. MIOpen(HIP): Error [...] Could not open metadata file: .../gfx1151_ConvHipImplicitGemm3DGroupFwdXdlops_metadata.tn.model ``` Then hangs forever. Health endpoint never returns 200. ## Root Cause `_maybe_initialize_encoder_cache()` in `gpu_model_runner.py` calls `self.model.embed_multimodal()` with dummy inputs, triggering MIOpen convolution operations. MIOpen has no pre-compiled solve...

## 现有链接修复摘要

#41587 [ROCm] Add VLLM_SKIP_MM_PROFILING env var as alternative to --skip-mm-profiling

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vLLM V1 engine hangs indefinitely during initialization when serving any model with a vision encoder on AMD gfx1151 (Strix Halo / Radeon 8060S). The hang occurs at encoder cache profiling where `embed_multimodal()` trig...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ngs on encoder cache profiling on AMD gfx1151 (MIOpen missing solver DB) rocm ## Description vLLM V1 engine hangs indefinitely during initialization when serving any model with a vision encoder on AMD gfx1151 (Strix Hal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: (HIP): Error [...] Could not open metadata file: .../gfx1151_ConvHipImplicitGemm3DGroupFwdXdlops_metadata.tn.model ``` Then hangs forever. Health endpoint never returns 200. ## Root Cause `_maybe_initialize_encoder_cach...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Reproduction ```bash vllm serve Qwen/Qwen3.5-35B-A3B --enforce-eager --dtype float16 --trust-remote-code ``` Server logs show: ``` INFO: Encoder cache will be initialized with a budget of 16384 tokens, and profiled with...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ems of the maximum feature size. MIOpen(HIP): Error [...] Could not open metadata file: .../gfx1151_ConvHipImplicitGemm3DGroupFwdXdlops_metadata.tn.model ``` Then hangs forever. Health endpoint never returns 200. ## Roo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41587](https://github.com/vllm-project/vllm/pull/41587) | closes_keyword | 0.95 | [ROCm] Add VLLM_SKIP_MM_PROFILING env var as alternative to --skip-mm-profiling | Fixes: #37472 ## Changes \| File \| Change \| \|---\|---\| \| `vllm/envs.py` \| Add `VLLM_SKIP_MM_PROFILING` (TYPE_CHECKING decl + runtime lambda) \| \| `vllm/engine/arg_utils.py` \| Change |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
