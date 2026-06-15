# vllm-project/vllm#41855: [Bug]: vLLM+UCCL-EP: DeepGemm CUDA Illegal Address at EP=64

| 字段 | 值 |
| --- | --- |
| Issue | [#41855](https://github.com/vllm-project/vllm/issues/41855) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM+UCCL-EP: DeepGemm CUDA Illegal Address at EP=64

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary When using `allgather_reducescatter` backend with DeepGemm enabled at EP=64 scale (8 nodes, 64 GPUs), CUDA graph capture fails with `CUDA_ERROR_ILLEGAL_ADDRESS`. The JIT-compiled FP8 GEMM kernels produce illegal memory accesses at this EP world size. ## Severity Critical — blocks EP=64 with agrs backend (the only backend that doesn't deadlock at this scale). ## Environment | Component | Version | |-----------|---------| | vLLM | 0.20.0 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | | NVIDIA Driver | 580.105.08 | | NCCL | 2.30.4-1 | | EFA Installer | 1.48.0 | ## Hardware - Instance: 8× AWS p5en.48xlarge - GPU: 64× NVIDIA H200 (141 GiB each) - Topology: TP=4/DP=16/EP=64 ## Steps to Reproduce 1. Deploy DeepSeek-V3-0324 across 8 nodes: ```bash vllm serve deepseek-ai/DeepSeek-V3-0324 \ --tensor-parallel-size 4 \ --data-parallel-size 16 \ --enable-expert-parallel \ --gpu-memory-utilization 0.85 \ --max-model-len 32768 \ --trust-remote-code \ --data-parallel-address \ --api-server-count 16 ``` (default backend = `allgather_reducescatter`) 2. Model loads successfully. 3. CUDA graph capture begins. 4. Crash with `CUDA_ERROR_ILL...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Us), CUDA graph capture fails with `CUDA_ERROR_ILLEGAL_ADDRESS`. The JIT-compiled FP8 GEMM kernels produce illegal memory accesses at this EP world size. ## Severity Critical — blocks EP=64 with agrs backend (the only b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n using `allgather_reducescatter` backend with DeepGemm enabled at EP=64 scale (8 nodes, 64 GPUs), CUDA graph capture fails with `CUDA_ERROR_ILLEGAL_ADDRESS`. The JIT-compiled FP8 GEMM kernels produce illegal memory acc...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: vLLM+UCCL-EP: DeepGemm CUDA Illegal Address at EP=64 bug ### Your current environment ### 🐛 Describe the bug ## Summary When using `allgather_reducescatter` backend with DeepGemm enabled at EP=64 scale (8 nodes,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ### 🐛 Describe the bug ## Summary When using `allgather_reducescatter` backend with DeepGemm enabled at EP=64 scale (8 nodes, 64 GPUs), CUDA graph capture fails with `CUDA_ERROR_ILLEGAL_ADDRESS`. The JIT-compiled FP8 GE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: vLLM+UCCL-EP: DeepGemm CUDA Illegal Address at EP=64 bug ### Your current environment ### 🐛 Describe the bug ## Summary When using `allgather_reducescatter` backend with DeepGemm enabled at EP=64 scale (8 nodes,...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
