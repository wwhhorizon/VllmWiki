# vllm-project/vllm#37701: [Bug]: Segfault in FlashInfer autotuning for NVFP4 latency backend on Qwen3-30B-A3B-NVFP4

| 字段 | 值 |
| --- | --- |
| Issue | [#37701](https://github.com/vllm-project/vllm/issues/37701) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | moe |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Segfault in FlashInfer autotuning for NVFP4 latency backend on Qwen3-30B-A3B-NVFP4

### Issue 正文摘录

### Your current environment sm100 ### 🐛 Describe the bug ### Description On current `main`, serving `nvidia/Qwen3-30B-A3B-NVFP4` with FlashInfer NVFP4 MoE enabled and `VLLM_FLASHINFER_MOE_BACKEND=latency` crashes during startup. The crash happens right after: `flashinfer.jit: [Autotuner]: Autotuning process starts ...` and then segfaults in: `cuModuleGetFunction -> BatchedGemmInterface::run -> FP4BlockScaleLauncher::run -> trtllm_fp4_block_scale_moe` ### Environment - vLLM: `0.10.1.dev7157+gaa84e43cc.d20260320` - flashinfer: `0.6.6` (built from source) - torch: `2.10.0+cu130` ### Repro res： https://paste.ubuntu.com/p/CvkXmb7tVh/ ```bash export VLLM_USE_FLASHINFER_MOE_FP4=1 export VLLM_FLASHINFER_MOE_BACKEND=latency CUDA_VISIBLE_DEVICES=4 \ vllm serve nvidia/Qwen3-30B-A3B-NVFP4 \ --tensor-parallel-size 1 \ --port 8102 \ --no-enable-prefix-caching res： https://paste.ubuntu.com/p/CvkXmb7tVh/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Segfault in FlashInfer autotuning for NVFP4 latency backend on Qwen3-30B-A3B-NVFP4 bug ### Your current environment sm100 ### 🐛 Describe the bug ### Description On current `main`, serving `nvidia/Qwen3-30B-A3B-NV...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: atency backend on Qwen3-30B-A3B-NVFP4 bug ### Your current environment sm100 ### 🐛 Describe the bug ### Description On current `main`, serving `nvidia/Qwen3-30B-A3B-NVFP4` with FlashInfer NVFP4 MoE enabled and `VLLM_FLA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Segfault in FlashInfer autotuning for NVFP4 latency backend on Qwen3-30B-A3B-NVFP4 bug ### Your current environment sm100 ### 🐛 Describe the bug ### Description On current `main`, serving `nvidia/Qwen3-30B-A3B-NV...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: rrent `main`, serving `nvidia/Qwen3-30B-A3B-NVFP4` with FlashInfer NVFP4 MoE enabled and `VLLM_FLASHINFER_MOE_BACKEND=latency` crashes during startup. The crash happens right after: `flashinfer.jit: [Autotuner]: Autotun...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Segfault in FlashInfer autotuning for NVFP4 latency backend on Qwen3-30B-A3B-NVFP4 bug ### Your current environment sm100 ### 🐛 Describe the bug ### Description On current `main`, serving `nvidia/Qwen3-30B-A3B-NV...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
