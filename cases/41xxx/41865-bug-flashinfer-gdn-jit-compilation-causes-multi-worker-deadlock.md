# vllm-project/vllm#41865: [Bug]: FlashInfer GDN JIT Compilation Causes Multi-Worker Deadlock

| 字段 | 值 |
| --- | --- |
| Issue | [#41865](https://github.com/vllm-project/vllm/issues/41865) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer GDN JIT Compilation Causes Multi-Worker Deadlock

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary The FlashInfer GDN (Gated Dilated Neighborhood) prefill kernel uses JIT compilation that causes a deadlock when multiple TP workers attempt to compile simultaneously. Worker 0 completes compilation (172s) but workers 1-7 hang indefinitely. The workaround is `--gdn-prefill-backend triton`. ## Severity Medium — has a working workaround (`--gdn-prefill-backend triton`), but the default behavior is broken. ## Environment | Component | Version | |-----------|---------| | vLLM | 0.20.0 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | | NVIDIA Driver | 580.105.08 | ## Hardware - 1× AWS p5en.48xlarge (8×H200) ## `collect_env.py` Output ``` PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 CMake version : version 3.28.3 Python version : 3.12.3 (64-bit runtime) Python platform : Linux-6.12.64-87.122.amzn2023.x86_64-x86_64-with-glibc2.39 Is CUDA available : True CUDA runtime version : 13.0.88 GPU models and configuration : GPU 0-7: NVIDIA H200 (141 GiB each) Nvidia driver version : 580.126.09 vLLM Version : 0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: T compilation that causes a deadlock when multiple TP workers attempt to compile simultaneously. Worker 0 completes compilation (172s) but workers 1-7 hang indefinitely. The workaround is `--gdn-prefill-backend triton`....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: rch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 CMake version : version 3.28.3 Pyth
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: FlashInfer GDN JIT Compilation Causes Multi-Worker Deadlock bug ### Your current environment ### 🐛 Describe the bug ## Summary The FlashInfer GDN (Gated Dilated Neighborhood) prefill kernel uses JIT compilation t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0 VLLM_WORKER_MULTIPROC_METHOD=spawn \ vllm serve Qwen/Qwen3.5-397B-A17B-FP8 \ --trust-remote-code \ --tensor-parallel-size 8 \ --language-model-only \ --gpu-memory-utilization 0.90 \ --max-model-len 32768 ``` (Note: no...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: | |-----------|---------| | vLLM | 0.20.0 | | PyTorch | 2.11.0+cu130 | | CUDA | 13.0.3 | | NVIDIA Driver | 580.105.08 | ## Hardware - 1× AWS p5en.48xlarge (8×H200) ## `collect_env.py` Output ``` PyTorch version : 2.11.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
