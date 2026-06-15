# vllm-project/vllm#41858: [Bug]: agrs Workspace Buffer Sizing Overflow at Large EP

| 字段 | 值 |
| --- | --- |
| Issue | [#41858](https://github.com/vllm-project/vllm/issues/41858) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: agrs Workspace Buffer Sizing Overflow at Large EP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary The `allgather_reducescatter` MoE workspace buffer is sized during the warmup/profile run (which uses a small batch), then locked. During CUDA graph capture (which uses max batch size), the workspace is too small, causing a runtime error. ## Severity High — blocks agrs at EP≥32 with CUDA graphs. ## Environment | Component | Version | |-----------|---------| | vLLM | 0.20.0 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | | NVIDIA Driver | 580.105.08 | | NCCL | 2.30.4-1 | ## Hardware - Instance: 8× AWS p5en.48xlarge - GPU: 64× NVIDIA H200 ## `collect_env.py` Output ``` PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 CMake version : version 3.28.3 Python version : 3.12.3 (64-bit runtime) Python platform : Linux-6.12.64-87.122.amzn2023.x86_64-x86_64-with-glibc2.39 Is CUDA available : True CUDA runtime version : 13.0.88 GPU models and configuration : GPU 0-7: NVIDIA H200 (141 GiB each) Nvidia driver version : 580.126.09 vLLM Version : 0.20.0 vLLM Build Flags : CUDA Archs: 8.0 8.6 8.9 9.0 10.0; ROCm:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: — blocks agrs at EP≥32 with CUDA graphs. ## Environment | Component | Version | |-----------|---------| | vLLM | 0.20.0 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | | NVIDIA Driver | 580.105.08 | | NCCL | 2.30.4-1 | #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: oE workspace buffer is sized during the warmup/profile run (which uses a small batch), then locked. During CUDA graph capture (which uses max batch size), the workspace is too small, causing a runtime error. ## Severity...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: nt ### 🐛 Describe the bug ## Summary The `allgather_reducescatter` MoE workspace buffer is sized during the warmup/profile run (which uses a small batch), then locked. During CUDA graph capture (which uses max batch siz...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: : 2.28.3-1 TORCH_CUDA_ARCH_LIST : 8.0 8.6 8.9 9.0 10.0 [pip3] flashinfer-python==0.6.8.post1 [pip3] torch==2.11.0+cu130 [pip3] transformers==5.6.2 [pip3] triton==3.6.0 [pip3] nvidia-nccl-cu13==2.28.9 [pip3] nvidia-nvshm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: he workspace is too small, causing a runtime error. ## Severity High — blocks agrs at EP≥32 with CUDA graphs. ## Environment | Component | Version | |-----------|---------| | vLLM | 0.20.0 | | PyTorch | 2.11.0+cu130 | |...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
