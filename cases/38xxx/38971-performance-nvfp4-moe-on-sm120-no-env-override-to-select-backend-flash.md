# vllm-project/vllm#38971: [Performance]: NVFP4 MoE on SM120: no env override to select backend (FLASHINFER_CUTLASS vs MARLIN)

| 字段 | 值 |
| --- | --- |
| Issue | [#38971](https://github.com/vllm-project/vllm/issues/38971) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;moe;quantization |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: NVFP4 MoE on SM120: no env override to select backend (FLASHINFER_CUTLASS vs MARLIN)

### Issue 正文摘录

### Proposal to improve performance Add an env variable (e.g. VLLM_NVFP4_MOE_BACKEND) to allow users to override the NVFP4 MoE backend selection. Currently the backend is auto-selected with no override possible. ### Report of performance regression Since v0.19.0, NVFP4 MoE models on SM120 (RTX PRO 6000) use FLASHINFER_CUTLASS by default. In v0.17.1, Marlin was the automatic fallback since FLASHINFER_CUTLASS did not support SM120 at that time. Single-user throughput on SM120 with Nemotron 3 Super (NVFP4, 120B): - Marlin (v0.17.1 default): ~92 tok/s - FLASHINFER_CUTLASS (v0.19.0 default): ~74 tok/s - Regression: ~20-25% Currently there is no way to override the MoE backend: - `VLLM_NVFP4_MOE_BACKEND` does not exist - `VLLM_NVFP4_GEMM_BACKEND=MARLIN` crashes with MoE models Log output (v0.19.0): ``` Using 'FLASHINFER_CUTLASS' NvFp4 MoE backend out of potential backends: ['FLASHINFER_TRTLLM', 'FLASHINFER_CUTEDSL', 'FLASHINFER_CUTLASS', 'VLLM_CUTLASS', 'MARLIN'] ``` ## KV cache comparison: Marlin vs FLASHINFER_CUTLASS Tested both backends on the same hardware with identical parameters (`--gpu-memory-utilization 0.95`, `--max-num-seqs 512`): | | v0.17.1 (Marlin) | v0.19.0 (FLASHINFER_CU...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Performance]: NVFP4 MoE on SM120: no env override to select backend (FLASHINFER_CUTLASS vs MARLIN) performance ### Proposal to improve performance Add an env variable (e.g. VLLM_NVFP4_MOE_BACKEND) to allow users to ove...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: NVFP4 MoE on SM120: no env override to select backend (FLASHINFER_CUTLASS vs MARLIN) performance ### Proposal to improve performance Add an env variable (e.g. VLLM_NVFP4_MOE_BACKEND) to allow users to ove...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: NVFP4 MoE on SM120: no env override to select backend (FLASHINFER_CUTLASS vs MARLIN) performance ### Proposal to improve performance Add an env variable (e.g. VLLM_NVFP4_MOE_BACKEND) to allow users to ove...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: d is auto-selected with no override possible. ### Report of performance regression Since v0.19.0, NVFP4 MoE models on SM120 (RTX PRO 6000) use FLASHINFER_CUTLASS by default. In v0.17.1, Marlin was the automatic fallback...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Performance]: NVFP4 MoE on SM120: no env override to select backend (FLASHINFER_CUTLASS vs MARLIN) performance ### Proposal to improve performance Add an env variable (e.g. VLLM_NVFP4_MOE_BACKEND) to allow users to ove...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
