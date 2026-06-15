# vllm-project/vllm#35015: [Bug]: Qwen3.5 FP8 CUDA Illegal Access in CUTLASS GEMM

| 字段 | 值 |
| --- | --- |
| Issue | [#35015](https://github.com/vllm-project/vllm/issues/35015) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;moe;operator;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 FP8 CUDA Illegal Access in CUTLASS GEMM

### Issue 正文摘录

### Your current environment Docker Image Tag: `qwen3_5-cu130`, patched with PR #34866 ``` PyTorch version : 2.10.0+cu130 CUDA used to build PyTorch : 13.0 CUDA runtime version : 13.0.88 Python version : 3.12.12 vLLM Version : 0.16.0rc2.dev294+g6a7b85d94 (git sha: 6a7b85d94) flashinfer-python : 0.6.3 transformers : 4.57.6 triton : 3.6.0 nvidia-nccl-cu13 : 2.28.9 GPU : 8x NVIDIA H200 (DP=8, expert parallel) OS : Ubuntu 22.04.5 LTS Container : vllm/vllm-openai:qwen3_5-cu130 ``` ### 🐛 Describe the bug # How to Reproduce the Error **Server command** ``` export VLLM_ENGINE_READY_TIMEOUT_S=1200 export VLLM_USE_DEEP_GEMM=0 export VLLM_USE_FLASHINFER_MOE_FP8=1 export VLLM_FLASHINFER_MOE_BACKEND="throughput" vllm serve Qwen/Qwen3.5-397B-A17B-FP8 \ --data-parallel-size 8 \ --enable-expert-parallel \ --gpu-memory-utilization 0.8 \ --enable-prefix-caching \ --language-model-only \ --reasoning-parser qwen3 ``` **Workload that triggers the crash**: - Input sequence length: 1024 - Output sequence length: 128 - Concurrency: 64 - Request rate: inf **Error traceback** ``` (EngineCore_DP0) ERROR [core.py:1031] EngineCore encountered a fatal error. (EngineCore_DP0) ERROR [core.py:1031] Traceback (mos...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: P8 CUDA Illegal Access in CUTLASS GEMM bug ### Your current environment Docker Image Tag: `qwen3_5-cu130`, patched with PR #34866 ``` PyTorch version : 2.10.0+cu130 CUDA used to build PyTorch : 13.0 CUDA runtime version...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen3.5 FP8 CUDA Illegal Access in CUTLASS GEMM bug ### Your current environment Docker Image Tag: `qwen3_5-cu130`, patched with PR #34866 ``` PyTorch version : 2.10.0+cu130 CUDA used to build PyTorch : 13.0 CUDA
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Qwen3.5 FP8 CUDA Illegal Access in CUTLASS GEMM bug ### Your current environment Docker Image Tag: `qwen3_5-cu130`, patched with PR #34866 ``` PyTorch version : 2.10.0+cu130 CUDA used to build PyTorch : 13.0 CUDA...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Qwen3.5 FP8 CUDA Illegal Access in CUTLASS GEMM bug ### Your current environment Docker Image Tag: `qwen3_5-cu130`, patched with PR #34866 ``` PyTorch version : 2.10.0+cu130 CUDA used to build PyTorch : 13.0 CUDA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: sequence length: 1024 - Output sequence length: 128 - Concurrency: 64 - Request rate: inf **Error traceback** ``` (EngineCore_DP0) ERROR [core.py:1031] EngineCore encountered a fatal error. (EngineCore_DP0) ERROR [core....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
