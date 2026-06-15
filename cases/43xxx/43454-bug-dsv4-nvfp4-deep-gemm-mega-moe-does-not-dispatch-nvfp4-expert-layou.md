# vllm-project/vllm#43454: [Bug][DSV4][NVFP4] `deep_gemm_mega_moe` does not dispatch NVFP4 expert layout — `KeyError: 'layers.0.ffn.experts.w13_input_scale'`

| 字段 | 值 |
| --- | --- |
| Issue | [#43454](https://github.com/vllm-project/vllm/issues/43454) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;kernel;moe;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][DSV4][NVFP4] `deep_gemm_mega_moe` does not dispatch NVFP4 expert layout — `KeyError: 'layers.0.ffn.experts.w13_input_scale'`

### Issue 正文摘录

### Your current environment ``` vLLM mainline @ 39910f2b25 (2026-05-22) + PR #42209 (NVFP4 MoE support for DSV4) — now merged + 4 local DSV4 patches (#43248, #43288, #43290, #43319) 8× NVIDIA B300 SXM6 AC (sm_103a, 288 GB HBM3e each) torch 2.11.0+cu130, CUDA 13.0 ``` ### How would you like to use vllm Serve an NVFP4-quantized DeepSeek-V4-Pro artifact on `--moe-backend deep_gemm_mega_moe`. The artifact uses standard NVIDIA ModelOpt NVFP4 layout (group=16, FP8 E4M3 block scales, FP32 per-tensor `weight_scale_2`, per-expert `input_scale`). ### Symptom Worker load fails with: ``` ERROR [multiproc_executor.py:870] Traceback (most recent call last): ERROR [multiproc_executor.py:870] KeyError: 'layers.0.ffn.experts.w13_input_scale' ``` Repro: serve any NVFP4 ModelOpt-layout DSV4 artifact with `--moe-backend deep_gemm_mega_moe` (e.g. the publicly available [`canada-quant/DeepSeek-V4-Pro-NVFP4-FP8-MTP`](https://huggingface.co/canada-quant/DeepSeek-V4-Pro-NVFP4-FP8-MTP)): ```bash vllm serve canada-quant/DeepSeek-V4-Pro-NVFP4-FP8-MTP \ --trust-remote-code --kv-cache-dtype fp8 --block-size 256 \ --tensor-parallel-size 8 --enable-expert-parallel \ --moe-backend deep_gemm_mega_moe \ --compilat...

## 现有链接修复摘要

#42209 Add NVFP4 MOE support for Deepseek V4. | #43248 [Bugfix][compressed-tensors] Wrap `is_static_input_scheme` with `bool()` for `input_quant=None` schemes | #43288 [Bugfix][DSV4] Default scale_fmt to "ue8m0" instead of hard-subscript | #43290 [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | #43319 [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config | #43467 [Bugfix][DSV4] Early-fail when MegaMoE is used with NVFP4 artifacts

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug][DSV4][NVFP4] `deep_gemm_mega_moe` does not dispatch NVFP4 expert layout — `KeyError: 'layers.0.ffn.experts.w13_input_scale'` ### Your current environment ``` vLLM mainline @ 39910f2b25 (2026-05-22) + PR #42209 (NV...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: on `--moe-backend deep_gemm_mega_moe`. The artifact uses standard NVIDIA ModelOpt NVFP4 layout (group=16, FP8 E4M3 block scales, FP32 per-tensor `weight_scale_2`, per-expert `input_scale`). ### Symptom Worker load fails...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][DSV4][NVFP4] `deep_gemm_mega_moe` does not dispatch NVFP4 expert layout — `KeyError: 'layers.0.ffn.experts.w13_input_scale'` ### Your current environment ``` vLLM mainline @ 39910f2b25 (2026-05-22) + PR #42209 (NV...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: cked Users who want to serve an NVFP4 V4-Pro artifact on the upstream-recipe-default `deep_gemm_mega_moe` mega-kernel backend (which the [`vllm-project/recipes/.../DeepSeek-V4-Pro.yaml`](https://github.com/vllm-project/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: al DSV4 patches (#43248, #43288, #43290, #43319) 8× NVIDIA B300 SXM6 AC (sm_103a, 288 GB HBM3e each) torch 2.11.0+cu130, CUDA 13.0 ``` ### How would you like to use vllm Serve an NVFP4-quantized DeepSeek-V4-Pro artifact...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42209](https://github.com/vllm-project/vllm/pull/42209) | mentioned | 0.45 | Add NVFP4 MOE support for Deepseek V4. | ng @sychen52 @xinli-sw @pavanimajety @zyongye since this is on the pr #42209 dispatch path. |
| [#43248](https://github.com/vllm-project/vllm/pull/43248) | mentioned | 0.45 | [Bugfix][compressed-tensors] Wrap `is_static_input_scheme` with `bool()` for `input_quant=None` schemes | 209 (nvfp4 moe support for dsv4) — now merged + 4 local dsv4 patches (#43248, #43288, #43290, #43319) 8× nvidia b300 sxm6 ac (sm_103a, 288 gb hbm3e each) torch 2.11.0+cu130, cuda… |
| [#43288](https://github.com/vllm-project/vllm/pull/43288) | mentioned | 0.45 | [Bugfix][DSV4] Default scale_fmt to "ue8m0" instead of hard-subscript | p4 moe support for dsv4) — now merged + 4 local dsv4 patches (#43248, #43288, #43290, #43319) 8× nvidia b300 sxm6 ac (sm_103a, 288 gb hbm3e each) torch 2.11.0+cu130, cuda 13.0 ```… |
| [#43290](https://github.com/vllm-project/vllm/pull/43290) | mentioned | 0.45 | [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | upport for dsv4) — now merged + 4 local dsv4 patches (#43248, #43288, #43290, #43319) 8× nvidia b300 sxm6 ac (sm_103a, 288 gb hbm3e each) torch 2.11.0+cu130, cuda 13.0 ``` ### how… |
| [#43319](https://github.com/vllm-project/vllm/pull/43319) | mentioned | 0.45 | [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config | or dsv4) — now merged + 4 local dsv4 patches (#43248, #43288, #43290, #43319) 8× nvidia b300 sxm6 ac (sm_103a, 288 gb hbm3e each) torch 2.11.0+cu130, cuda 13.0 ``` ### how would y… |
| [#43467](https://github.com/vllm-project/vllm/pull/43467) | closes_keyword | 0.95 | [Bugfix][DSV4] Early-fail when MegaMoE is used with NVFP4 artifacts | Closes #43454. ## Context Issue #43454 documents the failure mode: any NVFP4-quantized DSV4 artifact (e.g. our [`canada-quant/DeepSeek-V4-Pro-NVFP4-FP8-MTP`](https://huggingface. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
