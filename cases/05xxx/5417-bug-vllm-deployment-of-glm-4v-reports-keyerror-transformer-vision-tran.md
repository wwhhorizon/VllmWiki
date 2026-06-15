# vllm-project/vllm#5417: [Bug]: vllm deployment of GLM-4V reports KeyError: 'transformer.vision.transformer.layers.45.mlp.fc2.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#5417](https://github.com/vllm-project/vllm/issues/5417) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm deployment of GLM-4V reports KeyError: 'transformer.vision.transformer.layers.45.mlp.fc2.weight'

### Issue 正文摘录

### Your current environment ```shell Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.0-94-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.104.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 43 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: Au...

## 现有链接修复摘要

#5358 [Model] Add GLM-4v support | #7672 [Model][Bugfix] Add glm-4v Model and Fix bnb Quantization Issue | #9242 [Model] Add GLM-4v support and meet vllm==0.6.2

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rent environment ```shell Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ght' bug ### Your current environment ```shell Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: l clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca Virtualization:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.3.0 [pip3] torchvision==0.18.1 [pip3] transformers==4.40.0 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version:...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5358](https://github.com/vllm-project/vllm/pull/5358) | closes_keyword | 0.95 | [Model] Add GLM-4v support | FIX #5417 FIX #6097 ## Changes 1. Add `vision_config` for `ChatGLMConfig` 2. Add glm4 vision encoder in `vllm/model_executor/models/glm4_vision_encoder.py`. 3. Add optional `v |
| [#7672](https://github.com/vllm-project/vllm/pull/7672) | closes_keyword | 0.95 | [Model][Bugfix] Add glm-4v Model and Fix bnb Quantization Issue | FIX #5417 **Description**: This PR integrates the glm-4v model into the vLLM project and resolves an issue related to bnb quantization for this model. The previous quantization |
| [#9242](https://github.com/vllm-project/vllm/pull/9242) | closes_keyword | 0.95 | [Model] Add GLM-4v support and meet vllm==0.6.2  | FIX #5417 FIX #6097 Changes --- 1. Add `vision_config` for `ChatGLMConfig` 2. Add glm4 vision encoder in `vllm/model_executor/models/glm4_vision_encoder.py`. 3. Add option |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
