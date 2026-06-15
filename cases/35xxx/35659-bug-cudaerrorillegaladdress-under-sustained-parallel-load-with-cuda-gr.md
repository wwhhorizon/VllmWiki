# vllm-project/vllm#35659: [Bug]: cudaErrorIllegalAddress under sustained parallel load with CUDA Graphs on Blackwell SM120 (NVFP4 MoE)

| 字段 | 值 |
| --- | --- |
| Issue | [#35659](https://github.com/vllm-project/vllm/issues/35659) |
| 状态 | open |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | attention;cuda;gemm;kernel;moe;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cudaErrorIllegalAddress under sustained parallel load with CUDA Graphs on Blackwell SM120 (NVFP4 MoE)

### Issue 正文摘录

### Your current environment ``` PyTorch version : 2.8.0.dev20250627+cu131 CUDA used to build PyTorch : 13.1 CUDA runtime version : 13.1 Python version : 3.12.12 vLLM Version : 0.16.0 flashinfer-python : 0.6.4 GPU : 4x NVIDIA RTX PRO 6000 (SM120, 96GB each) Driver : 590.48.01 OS : Ubuntu 24.04 ``` ### Model `nvidia/Qwen3.5-397B-A17B-NVFP4` (NVFP4 quantization, TP=4) ### Backend - GEMM: `NvFp4LinearBackend.FLASHINFER_CUTLASS` - MoE: `FLASHINFER_CUTLASS` (autotuner skips tactics 14/15 on SM120, remaining tactics work) - Attention: `FLASHINFER` ### 🐛 Describe the bug `cudaErrorIllegalAddress` crash occurs **only** under sustained concurrent load when CUDA Graphs are enabled. The crash does not occur with `--enforce-eager`. ### Reproduction matrix All tests use `max_tokens=16384` with real LLM test prompts (120 problems across 6 categories). | CUDA Graph Mode | Workload | Result | |---|---|---| | `FULL_AND_PIECEWISE` (default) | 10 concurrent, sustained | ❌ Crash after 12–20 min | | `PIECEWISE` only | 6 concurrent streams, sustained | ❌ Crash after ~8 min | | `PIECEWISE` only | 2–20 concurrent, 3 rounds with 3s gaps | ✅ Stable | | `PIECEWISE` only | 120 problems sequential | ✅ Stable...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: dress under sustained parallel load with CUDA Graphs on Blackwell SM120 (NVFP4 MoE) stale ### Your current environment ``` PyTorch version : 2.8.0.dev20250627+cu131 CUDA used to build PyTorch : 13.1 CUDA runtime version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: cudaErrorIllegalAddress under sustained parallel load with CUDA Graphs on Blackwell SM120 (NVFP4 MoE) stale ### Your current environment ``` PyTorch version : 2.8.0.dev20250627+cu131 CUDA used to build PyTo
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ckwell SM120 (NVFP4 MoE) stale ### Your current environment ``` PyTorch version : 2.8.0.dev20250627+cu131 CUDA used to build PyTorch : 13.1 CUDA runtime version : 13.1 Python version : 3.12.12 vLLM Version : 0.16.0 flas...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: on version : 3.12.12 vLLM Version : 0.16.0 flashinfer-python : 0.6.4 GPU : 4x NVIDIA RTX PRO 6000 (SM120, 96GB each) Driver : 590.48.01 OS : Ubuntu 24.04 ``` ### Model `nvidia/Qw
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: : 590.48.01 OS : Ubuntu 24.04 ``` ### Model `nvidia/Qwen3.5-397B-A17B-NVFP4` (NVFP4 quantization, TP=4) ### Backend - GEMM: `NvFp4LinearBackend.FLASHINFER_CUTLASS` - MoE: `FLASHINFER_CUTLASS` (autotuner skips tactics 14...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
