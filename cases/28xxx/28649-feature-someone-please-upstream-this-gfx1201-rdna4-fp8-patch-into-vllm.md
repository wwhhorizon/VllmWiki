# vllm-project/vllm#28649: [Feature]: Someone please upstream this gfx1201/RDNA4 FP8 Patch into vllm-rocm

| 字段 | 值 |
| --- | --- |
| Issue | [#28649](https://github.com/vllm-project/vllm/issues/28649) |
| 状态 | open |
| 标签 | feature request;rocm;unstale |
| 评论 | 42; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Someone please upstream this gfx1201/RDNA4 FP8 Patch into vllm-rocm

### Issue 正文摘录

Mea cupla - I missed the fall through case where it automatically ended up in the Gemm-w8a8, by adding an explicit gfx1201 it actually restricts the code more and is not necessary. Thank you [hurricane-dorian](https://github.com/hurricane-dorian) for pointing out that there was an existing fall through case already that led to the same code path for arriving at the W8A8 code. I did some regression testing to confirm and, simply adding in the tuned moe-config and matrix configs for the model resulted in the same performance uplifts without any of the patches. The uplifts in performance others observed I cannot explain beyond, throughput improvement was likely from cuda graph improvements that arrived in the 2025-11-08 nightly, not the fp8 changes. This actually only needs your individual model configs added to see massive gains in speed: no patch, no wrapper, nothing else. **Alternative: Inline Patch** If you don't want a wrapper script, add this to your Docker ENTRYPOINT or startup command: ```bash python3 -c "import aiter.ops.triton.utils.arch_info as arch_info; arch_info._ARCH_TO_DEVICE['gfx1201'] = 'MI350X'" && \ export VLLM_ROCM_USE_AITER=0 && \ vllm serve "$@" ``` --- ### 3....

## 现有链接修复摘要

#36659 [ROCm] Enable FP8 inference on gfx1201 AMD RDNA4 (Radeon AI PRO R9700) with aiter kernels

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: case where it automatically ended up in the Gemm-w8a8, by adding an explicit gfx1201 it actually restricts the code more and is not necessary. Thank you [hurricane-dorian](https://github.com/hurricane-dorian) for pointi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: Someone please upstream this gfx1201/RDNA4 FP8 Patch into vllm-rocm feature request;rocm;unstale Mea cupla - I missed the fall through case where it automatically ended up in the Gemm-w8a8, by adding an expli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Feature]: Someone please upstream this gfx1201/RDNA4 FP8 Patch into vllm-rocm feature request;rocm;unstale Mea cupla - I missed the fall through case where it automatically ended up in the Gemm-w8a8, by adding an explic...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: figs added to see massive gains in speed: no patch, no wrapper, nothing else. **Alternative: Inline Patch** If you don't want a wrapper script, add this to your Docker ENTRYPOINT or startup command: ```bash python3 -c "...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: hat led to the same code path for arriving at the W8A8 code. I did some regression testing to confirm and, simply adding in the tuned moe-config and matrix configs for the model resulted in the same performance uplifts...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36659](https://github.com/vllm-project/vllm/pull/36659) | mentioned | 0.6 | [ROCm] Enable FP8 inference on gfx1201 AMD RDNA4 (Radeon AI PRO R9700) with aiter kernels | ned defaults, leaving significant performance on the table. Related: #28649. **Changes:** ### 1. FP8 MoE Path for gfx12x (`vllm/model_executor/layers/fused_moe/fused_moe.py`) `dev… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
