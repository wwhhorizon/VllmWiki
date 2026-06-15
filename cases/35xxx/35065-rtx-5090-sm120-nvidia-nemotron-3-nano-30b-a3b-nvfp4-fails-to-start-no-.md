# vllm-project/vllm#35065: RTX 5090 (SM120): NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 fails to start, No NvFp4 MoE backend supports the deployment configuration

| 字段 | 值 |
| --- | --- |
| Issue | [#35065](https://github.com/vllm-project/vllm/issues/35065) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | hardware_porting;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;kernel;moe |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RTX 5090 (SM120): NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 fails to start, No NvFp4 MoE backend supports the deployment configuration

### Issue 正文摘录

### Your current environment ```bash === BLACKWELL (sm_120) VERIFICATION === Device Count : 1 GPU 0 : NVIDIA GeForce RTX 5090 Compute Cap : 12.0 SM Units : 170 VRAM Total : 32044 MiB L2 Cache : 98304 KB Clock Rate : 2407 MHz ----- SOFTWARE STACK ----- Python 👇 /home/user/.venvs/vllm-env/bin/python Model Name : NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 Python -v : 3.11.14 Torch : 2.10.0+cu128 CUDA Runtime : 12.8 FlashInfer : 0.6.2 cuDNN : 91501 Native sm_120: True ----- CUDA TENSOR TESTS ----- BF16 Matrix : OK FP8 Support : SUPPORTED FP4 Support : SUPPORTED ====================================== ``` ### 🐛 Describe the bug vLLM’s NVFP4 MoE backend selection can hard-fail when no backend matches the deployment configuration. [[arxiv.org]](https://arxiv.org/pdf/2512.20848) Similar SM120 NVFP4 MoE backend/device support failures have been reported (e.g. kernel does not support current device). [[huggingface.co]](https://huggingface.co/Firworks/NVIDIA-Nemotron-3-Nano-30B-A3B-nvfp4), [[docs.vllm.ai]](https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_w4a4_fp4/) If relevant: community notes indicate Nemotron-H MoE may follow a path that is not supported for NVFP4 in s...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: RTX 5090 (SM120): NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 fails to start, No NvFp4 MoE backend supports the deployment configuration bug;stale ### Your current environment ```bash === BLACKWELL (sm_120) VERIFICATION === De...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: RTX 5090 (SM120): NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 fails to start, No NvFp4 MoE backend supports the deployment configuration bug;stale ### Your current environment ```bash === BLACKWELL (sm_120) VERIFICATION === De
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: B-A3B-NVFP4 fails to start, No NvFp4 MoE backend supports the deployment configuration bug;stale ### Your current environment ```bash === BLACKWELL (sm_120) VERIFICATION === Device Count : 1 GPU 0 : NVIDIA GeForce RTX 5...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: M120): NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 fails to start, No NvFp4 MoE backend supports the deployment configuration bug;stale ### Your current environment ```bash === BLACKWELL (sm_120) VERIFICATION === Device Count...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: are_porting;model_support;moe;quantization cuda;fp8;kernel;moe dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
