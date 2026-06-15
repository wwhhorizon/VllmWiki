# vllm-project/vllm#41862: [Bug]: EP Deadlock with Hybrid GDN/Mamba Architecture (Qwen3.5)

| 字段 | 值 |
| --- | --- |
| Issue | [#41862](https://github.com/vllm-project/vllm/issues/41862) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;fp8;moe;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EP Deadlock with Hybrid GDN/Mamba Architecture (Qwen3.5)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary All Expert Parallelism configurations deadlock on Qwen3.5-397B-A17B-FP8 during CUDA graph capture or profile forward. Worker rank 0 completes torch.compile but other ranks hang indefinitely after the Mamba page size initialization step. ## Severity High — blocks all EP configurations for the Qwen3.5 model family. ## Environment | Component | Version | |-----------|---------| | vLLM | 0.20.0 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | | NVIDIA Driver | 580.105.08 | | NCCL | 2.30.4-1 | ## Hardware - Instance: 1× AWS p5en.48xlarge - GPU: 8× NVIDIA H200 (141 GiB each) ## `collect_env.py` Output ``` PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 CMake version : version 3.28.3 Python version : 3.12.3 (64-bit runtime) Python platform : Linux-6.12.64-87.122.amzn2023.x86_64-x86_64-with-glibc2.39 Is CUDA available : True CUDA runtime version : 13.0.88 GPU models and configuration : GPU 0-7: NVIDIA H200 (141 GiB each) Nvidia driver version : 580.126.09 vLLM Version : 0.20.0 vLLM Build Flags : CUDA Arc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ing CUDA graph capture or profile forward. Worker rank 0 completes torch.compile but other ranks hang indefinitely after the Mamba page size initialization step. ## Severity High — blocks all EP configurations for the Q...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: : 2.28.3-1 TORCH_CUDA_ARCH_LIST : 8.0 8.6 8.9 9.0 10.0 [pip3] flashinfer-python==0.6.8.post1 [pip3] torch==2.11.0+cu130 [pip3] transformers==5.6.2 [pip3] triton==3.6.0 [pip3] nvidia-nccl-cu13==2.28.9 [pip3] nvidia-nvshm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: EP Deadlock with Hybrid GDN/Mamba Architecture (Qwen3.5) bug ### Your current environment ### 🐛 Describe the bug ## Summary All Expert Parallelism configurations deadlock on Qwen3.5-397B-A17B-FP8 during CUDA grap...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ompletes torch.compile but other ranks hang indefinitely after the Mamba page size initialization step. ## Severity High — blocks all EP configurations for the Qwen3.5 model family. ## Environment | Component | Version...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ### Your current environment ### 🐛 Describe the bug ## Summary All Expert Parallelism configurations deadlock on Qwen3.5-397B-A17B-FP8 during CUDA graph capture or profile forward. Worker rank 0 completes torch.compile...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
