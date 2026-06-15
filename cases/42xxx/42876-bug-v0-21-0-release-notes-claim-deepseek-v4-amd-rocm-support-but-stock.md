# vllm-project/vllm#42876: [Bug]: v0.21.0 release notes claim 'DeepSeek V4: AMD/ROCm support' but stock vllm/vllm-openai-rocm:v0.21.0 fails to bring up DeepSeek-V4-Flash on MI350X (mhc_post_tilelang → PDL is not supported); the official recipes YAML marks every AMD SKU as unsupported

| 字段 | 值 |
| --- | --- |
| Issue | [#42876](https://github.com/vllm-project/vllm/issues/42876) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: v0.21.0 release notes claim 'DeepSeek V4: AMD/ROCm support' but stock vllm/vllm-openai-rocm:v0.21.0 fails to bring up DeepSeek-V4-Flash on MI350X (mhc_post_tilelang → PDL is not supported); the official recipes YAML marks every AMD SKU as unsupported

### Issue 正文摘录

## Your current environment The reproduction pod has been reclaimed by other workloads, so a fresh `python collect_env.py` is not available; relevant fields gathered in-pod during the run: ## 🐛 Describe the bug ### Summary The v0.21.0 release notes list **"DeepSeek V4: AMD/ROCm support (#40871)"** under Model Support, but on the official `vllm/vllm-openai-rocm:v0.21.0` image, attempting to serve `deepseek-ai/DeepSeek-V4-Flash` on MI350X (gfx950) fails during `profile_run` in the `mhc_post_tilelang` op with a hard TVM/TileLang `LogFatal`: ``` tvm.error.InternalError: Check failed: (!mutator.has_trigger_launch_ && !mutator.has_grid_sync_) is false: PDL is not supported ``` PDL = NVIDIA Hopper's Programmatic Dependent Launch — a CUDA-only feature. The TileLang pass `MarkCudaSyncCalls` refuses an IR that emits `trigger_launch` / `grid_sync` ops when targeting AMD. The path is reached from the DSv4 model's `forward` → `torch.ops.vllm.mhc_fused_post_pre` → `mhc.py:717 mhc_post_tilelang` → TileLang JIT compile. Additionally, the canonical recipe source backing [recipes.vllm.ai](https://recipes.vllm.ai) marks **every AMD SKU as `unsupported`** for both DSv4-Pro and DSv4-Flash (see [`DeepS...

## 现有链接修复摘要

#40871 [New Model][ROCm] Add AMD support for DeepSeek V4 | #40991 [DSv4][Nvidia] SM12x DeepSeek V4 support | #41136 [ROCm] DeepSeekV4-Flash-Base model enablement on ROCm with triton & torchfallback | #41946 [Bugfix] [ROCm] [DSV4] [Perf] Add aiter mhc support

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: v0.21.0 release notes claim 'DeepSeek V4: AMD/ROCm support' but stock vllm/vllm-openai-rocm:v0.21.0 fails to bring up DeepSeek-V4-Flash on MI350X (mhc_post_tilelang → PDL is not supported); the official recipes Y...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: k-V4-Flash on MI350X (mhc_post_tilelang → PDL is not supported); the official recipes YAML marks every AMD SKU as unsupported rocm ## Your current environment The reproduction pod has been reclaimed by other workloads,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: PR that adds AMD MHC support (#41946 "[Bugfix] [ROCm] [DSV4] [Perf] Add aiter mhc support", merged 2026-05-13), but it **did not make the v0.21.0 cut** at commit `ad7125a` (`git log v0.21.0 --grep="(#41946)"` returns no...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: .0 release notes list **"DeepSeek V4: AMD/ROCm support (#40871)"** under Model Support, but on the official `vllm/vllm-openai-rocm:v0.21.0` image, attempting to serve `deepseek-ai/DeepSeek-V4-Flash` on MI350X (gfx950) f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: AML provides no AMD command since AMD is `unsupported`). The `--kv-cache-dtype fp8` is required because `vllm/model_executor/models/deepseek_v4.py:1636` asserts on it: ```bash export VLLM_ROCM_USE_AITER=1 vllm serve /pa...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40871](https://github.com/vllm-project/vllm/pull/40871) | mentioned | 0.45 | [New Model][ROCm] Add AMD support for DeepSeek V4 | releases/tag/v0.21.0 - base amd enablement pr cited in release notes: #40871 (merged, in 0.21.0) - amd mhc support: #41946 (merged on main 2026-05-13, **not in v0.21.0**) - remain… |
| [#40991](https://github.com/vllm-project/vllm/pull/40991) | mentioned | 0.45 | [DSv4][Nvidia] SM12x DeepSeek V4 support | m12x equivalent of this mhc issue (closed via a different code path): #40991 - recipes yamls claiming amd unsupported: - https://github.com/vllm-project/recipes/blob/main/models/d… |
| [#41136](https://github.com/vllm-project/vllm/pull/41136) | mentioned | 0.45 | [ROCm] DeepSeekV4-Flash-Base model enablement on ROCm with triton & torchfallback | -05-13, **not in v0.21.0**) - remaining amd fallbacks for dsv4-flash: #41136 (open, dirty) - tracking issue for dsv4 rocm: #41820 - existing amd-specific dsv4 bugs (separate failu… |
| [#41946](https://github.com/vllm-project/vllm/pull/41946) | mentioned | 0.45 | [Bugfix] [ROCm] [DSV4] [Perf] Add aiter mhc support | cited in release notes: #40871 (merged, in 0.21.0) - amd mhc support: #41946 (merged on main 2026-05-13, **not in v0.21.0**) - remaining amd fallbacks for dsv4-flash: #41136 (open… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
