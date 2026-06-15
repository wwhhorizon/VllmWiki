# vllm-project/vllm#42118: [Bug]:  FLASHINFER_CUTLASS_MXFP4_MXFP8 produces wrong output under expert parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#42118](https://github.com/vllm-project/vllm/issues/42118) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  FLASHINFER_CUTLASS_MXFP4_MXFP8 produces wrong output under expert parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The post-all-to-all swizzle in the EP/DP-EP prepare-finalize wrappers is gated on `quant_dtype == "nvfp4"`, which means `mxfp8` activation scales arrive at the CUTLASS kernel unswizzled. The CUTLASS MoE kernel requires swizzled scales, so outputs are garbage. This is a pre-existing limitation surfaced by review of #42089, not a regression from that PR. **Affected lines** (gate currently `quant_dtype == "nvfp4"` only): - `vllm/model_executor/layers/fused_moe/prepare_finalize/naive_dp_ep.py:62` - `vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_one_sided.py:132-135` - `vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_two_sided.py:197` **Repro** (GPQA Eval times out at 1800 s; ~6/1584 items in 11 minutes): ```bash VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8_CUTLASS=1 \ vllm serve openai/gpt-oss-20b \ --data-parallel-size 2 --enable-expert-parallel --gpu-memory-utilization 0.4 # then run gpt_oss.evals gpqa against it ``` PF in use: `MoEPrepareAndFinalizeNaiveDPEPModular`. Backend confirmed: `FLASHINFER_CUTLASS_MXFP4_MXFP8`. **Why the obvious fix isn't quite right** Just expanding the gate to inc...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: FLASHINFER_CUTLASS_MXFP4_MXFP8 produces wrong output under expert parallelism bug ### Your current environment ### 🐛 Describe the bug The post-all-to-all swizzle in the EP/DP-EP prepare-finalize wrappers is gated...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: FLASHINFER_CUTLASS_MXFP4_MXFP8 produces wrong output under expert parallelism bug ### Your current environment ### 🐛 Describe the bug The post-all-to-all swizzle in the EP/DP-EP prepare-finalize wrappers is gated...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: . This is a pre-existing limitation surfaced by review of #42089, not a regression from that PR. **Affected lines** (gate currently `quant_dtype == "nvfp4"` only): - `vllm/model_executor/layers/fused_moe/prepare_finaliz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 2` - `vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_one_sided.py:132-135` - `vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_two_sided.py:197` **Repro** (GPQA Eval times...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ASHINFER_CUTLASS_MXFP4_MXFP8 produces wrong output under expert parallelism bug ### Your current environment ### 🐛 Describe the bug The post-all-to-all swizzle in the EP/DP-EP prepare-finalize wrappers is gated on `quan...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
