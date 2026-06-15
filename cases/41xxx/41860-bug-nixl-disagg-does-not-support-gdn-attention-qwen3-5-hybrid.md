# vllm-project/vllm#41860: [Bug]: NIXL Disagg Does Not Support GDN Attention (Qwen3.5 Hybrid)

| 字段 | 值 |
| --- | --- |
| Issue | [#41860](https://github.com/vllm-project/vllm/issues/41860) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NIXL Disagg Does Not Support GDN Attention (Qwen3.5 Hybrid)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary The NIXL KV connector (`NixlConnector`) cannot transfer GDN (Gated Dilated Neighborhood) attention state used by Qwen3.5 models. The 3-read conv transfer path only supports Mamba2 models, blocking disaggregated serving for the entire Qwen3.5 family. ## Severity Medium — blocks disaggregated serving for a major new model family (Qwen3.5). ## Environment | Component | Version | |-----------|---------| | vLLM | 0.20.0 | | NIXL | 1.0.1 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | ## Hardware - 2× AWS p5en.48xlarge (8×H200 each) - 16× EFA per node ## `collect_env.py` Output ``` PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 CMake version : version 3.28.3 Python version : 3.12.3 (64-bit runtime) Python platform : Linux-6.12.64-87.122.amzn2023.x86_64-x86_64-with-glibc2.39 Is CUDA available : True CUDA runtime version : 13.0.88 GPU models and configuration : GPU 0-7: NVIDIA H200 (141 GiB each) Nvidia driver version : 580.126.09 vLLM Version : 0.20.0 vLLM Build Flags : CUDA Archs: 8.0 8.6 8.9 9.0 10....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: g for a major new model family (Qwen3.5). ## Environment | Component | Version | |-----------|---------| | vLLM | 0.20.0 | | NIXL | 1.0.1 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | ## Hardware - 2× AWS p5en.48xlarge...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: hmem-cu13==3.4.5 ``` ## Steps to Reproduce 1. Deploy Qwen3.5-397B-A17B-FP8 with NIXL KV transfer: ```bash export VLLM_USE_DEEP_GEMM=0 export VLLM_WORKER_MULTIPROC_METHOD=spawn export VLLM_NIXL_SIDE_CHANNEL_HOST=0.0.0.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: -------| | vLLM | 0.20.0 | | NIXL | 1.0.1 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | ## Hardware - 2× AWS p5en.48xlarge (8×H200 each) - 16× EFA per node ## `collect_env.py` Output ``` PyTorch version : 2.11.0+cu130...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: en3.5 models. The 3-read conv transfer path only supports Mamba2 models, blocking disaggregated serving for the entire Qwen3.5 family. ## Severity Medium — blocks disaggregated serving for a major new model family (Qwen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: : 2.28.3-1 TORCH_CUDA_ARCH_LIST : 8.0 8.6 8.9 9.0 10.0 [pip3] flashinfer-python==0.6.8.post1 [pip3] torch==2.11.0+cu130 [pip3] transformers==5.6.2 [pip3] triton==3.6.0 [pip3] nvidia-nccl-cu13==2.28.9 [pip3] nvidia-nvshm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
