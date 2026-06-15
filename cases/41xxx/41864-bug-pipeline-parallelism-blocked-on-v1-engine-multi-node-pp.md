# vllm-project/vllm#41864: [Bug]: Pipeline Parallelism Blocked on V1 Engine (Multi-Node PP)

| 字段 | 值 |
| --- | --- |
| Issue | [#41864](https://github.com/vllm-project/vllm/issues/41864) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;moe;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pipeline Parallelism Blocked on V1 Engine (Multi-Node PP)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary Multi-node pipeline parallelism (PP=2/TP=8 across 2 nodes) fails with `AssertionError: collective_rpc should not be called on follower node`. The V1 engine's `MultiprocessExecutor` only supports shared-memory IPC (single-node). Multi-node PP requires Ray or a new distributed executor. ## Severity Medium — blocks an important scaling strategy. SGLang/LMSYS show PP4+TP8 beats TP=32 by 30% for cross-node MoE serving. ## Environment | Component | Version | |-----------|---------| | vLLM | 0.20.0 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | | NVIDIA Driver | 580.105.08 | | NCCL | 2.30.4-1 | ## Hardware - Instance: 2× AWS p5en.48xlarge - GPU: 16× NVIDIA H200 - Network: 16× EFA per node ## `collect_env.py` Output ``` PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 CMake version : version 3.28.3 Python version : 3.12.3 (64-bit runtime) Python platform : Linux-6.12.64-87.122.amzn2023.x86_64-x86_64-with-glibc2.39 Is CUDA available : True CUDA runtime version : 13.0.88 GPU models and configuration : GPU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ires Ray or a new distributed executor. ## Severity Medium — blocks an important scaling strategy. SGLang/LMSYS show PP4+TP8 beats TP=32 by 30% for cross-node MoE serving. ## Environment | Component | Version | |-------...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Pipeline Parallelism Blocked on V1 Engine (Multi-Node PP) bug ### Your current environment ### 🐛 Describe the bug ## Summary Multi-node pipeline parallelism (PP=2/TP=8 across 2 nodes) fails with `AssertionError:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: : 2.28.3-1 TORCH_CUDA_ARCH_LIST : 8.0 8.6 8.9 9.0 10.0 [pip3] flashinfer-python==0.6.8.post1 [pip3] torch==2.11.0+cu130 [pip3] transformers==5.6.2 [pip3] triton==3.6.0 [pip3] nvidia-nccl-cu13==2.28.9 [pip3] nvidia-nvshm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: Pipeline Parallelism Blocked on V1 Engine (Multi-Node PP) bug ### Your current environment ### 🐛 Describe the bug ## Summary Multi-node pipeline parallelism (PP=2/TP=8 across 2 nodes) fails with `AssertionError:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: A available : True CUDA runtime version : 13.0.88 GPU models and configuration : GPU 0-7: NVIDIA H200 (141 GiB each) Nvidia driver version : 580.126.09 vLLM Version : 0.20.0 vLLM Build Flags : CUDA Archs: 8.0 8.6 8.9 9....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
