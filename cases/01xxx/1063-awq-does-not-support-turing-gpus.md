# vllm-project/vllm#1063: AWQ does not support Turing GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#1063](https://github.com/vllm-project/vllm/issues/1063) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;quantization |
| 子分类 | build_fail |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AWQ does not support Turing GPUs

### Issue 正文摘录

@WoosukKwon Doesn't it support Turing arch? my GPU's compute capabitlity is 7.5. CUDA-12.1. build Error message: `ptxas /tmp/tmpxft_0006e7c4_00000000-6_gemm_kernels.ptx, line 928; error : Feature '.m16n8k16' requires .target sm_80 or higher` If not, hope can add backward compatibility for kernel build. _Originally posted by @esmeetu in https://github.com/vllm-project/vllm/issues/1032#issuecomment-1722179620_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: AWQ does not support Turing GPUs @WoosukKwon Doesn't it support Turing arch? my GPU's compute capabitlity is 7.5. CUDA-12.1. build Error message: `ptxas /tmp/tmpxft_0006e7c4_00000000-6_gemm_kernels.ptx, line 928; error...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: it support Turing arch? my GPU's compute capabitlity is 7.5. CUDA-12.1. build Error message: `ptxas /tmp/tmpxft_0006e7c4_00000000-6_gemm_kernels.ptx, line 928; error : Feature '.m16n8k16' requires .target sm_80 or highe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: m-project/vllm/issues/1032#issuecomment-1722179620_ development ci_build;quantization cuda;kernel;quantization build_error @WoosukKwon Doesn't it support Turing arch? my GPU's compute capabitlity is 7.5. CUDA-12.1.
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: DA-12.1. build Error message: `ptxas /tmp/tmpxft_0006e7c4_00000000-6_gemm_kernels.ptx, line 928; error : Feature '.m16n8k16' requires .target sm_80 or higher` If not, hope can add backward compatibility for kernel build...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
