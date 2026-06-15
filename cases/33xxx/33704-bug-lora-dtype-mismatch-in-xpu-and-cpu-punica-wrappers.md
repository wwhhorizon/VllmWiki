# vllm-project/vllm#33704: [Bug]: LoRA dtype mismatch in XPU and CPU punica wrappers

| 字段 | 值 |
| --- | --- |
| Issue | [#33704](https://github.com/vllm-project/vllm/issues/33704) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LoRA dtype mismatch in XPU and CPU punica wrappers

### Issue 正文摘录

## Your current environment - vLLM version: main branch - Platform: GPU / XPU / CPU ## Description The punica wrappers and LoRA layer implementations hardcode `torch.float32` for intermediate buffers in `add_lora_linear` and `add_lora_logits`, regardless of the input tensor dtype. This causes dtype mismatches when using bfloat16 models with LoRA. ## Root Cause The original code had comments referencing Triton issue #[1387](https://github.com/triton-lang/triton/pull/1387) which required float32 buffers for the Triton kernels. However, this issue has been resolved in Triton (May 2025, see: Triton https://github.com/triton-lang/triton/pull/6519) and the float32 constraint is no longer necessary. ## Affected code **punica_gpu.py** (lines ~241 and ~299): ```python # Current (incorrect): buffer = torch.empty(..., dtype=torch.float32, device=x.device) # should change to: buffer = torch.empty(..., dtype=x.dtype, device=x.device) ``` **punica_xpu.py** (lines ~211 and ~270): Same issue. **punica_cpu.py** (lines ~305 and ~345): Same issue. **column_parallel_linear.py** (line ~44): ```python buffers = torch.zeros(..., dtype=torch.float32, device=x.device) # Should be x.dtype ``` **row_paralle...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: LoRA dtype mismatch in XPU and CPU punica wrappers ## Your current environment - vLLM version: main branch - Platform: GPU / XPU / CPU ## Description The punica wrappers and LoRA layer implementations hardcode `t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: LoRA dtype mismatch in XPU and CPU punica wrappers ## Your current environment - vLLM version: main branch - Platform: GPU / XPU / CPU ## Description The punica wrappers and LoRA layer implementations hardcode `t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: match in XPU and CPU punica wrappers ## Your current environment - vLLM version: main branch - Platform: GPU / XPU / CPU ## Description The punica wrappers and LoRA layer implementations hardcode `torch.float32` for int...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ls with LoRA. ## Root Cause The original code had comments referencing Triton issue #[1387](https://github.com/triton-lang/triton/pull/1387) which required float32 buffers for the Triton kernels. However, this issue has...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: LoRA dtype mismatch in XPU and CPU punica wrappers ## Your current environment - vLLM version: main branch - Platform: GPU / XPU / CPU ## Description The punica wrappers and LoRA layer implementations hardcode `t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
