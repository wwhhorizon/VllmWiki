# vllm-project/vllm#14095: [Bug]: [Bug]: Run vllm serve raise Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#14095](https://github.com/vllm-project/vllm/issues/14095) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Bug]: Run vllm serve raise Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks

### Issue 正文摘录

### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.8 (main, Feb 25 2025, 17:18:01) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.8.0-52-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.8.61 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A16 GPU 1: NVIDIA A16 GPU 2: NVIDIA A16 GPU 3: NVIDIA A16 GPU 4: NVIDIA A16 GPU 5: NVIDIA A16 GPU 6: NVIDIA A16 GPU 7: NVIDIA A16 GPU 8: NVIDIA A16 GPU 9: NVIDIA A16 GPU 10: NVIDIA A16 GPU 11: NVIDIA A16 GPU 12: NVIDIA A16 GPU 13: NVIDIA A16 GPU 14: NVIDIA A16 GPU 15: NVIDIA A16 GPU 16: NVIDIA A16 GPU 17: NVIDIA A16 GPU 18: NVIDIA A16 GPU 19: NVIDIA A16 GPU 20: NVIDIA A16 GPU 21: NVIDIA A16 GPU 22: NVIDIA A16 GPU 23: NVIDIA A16 Nvidia driver version: 570.86.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ine_num_available_blocks bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.8.61 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A16 GPU 1: NVIDIA A16 GPU 2: NVIDIA A16 GPU 3: NVIDIA A16 GPU 4: NVIDIA A16 GPU 5: NVIDIA A16 GPU 6: NVIDIA...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: worker VllmWorkerProcess while processing method determine_num_available_blocks bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to bui...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.49.0 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.7.4.dev85+g37b6cb49 vLLM Build Fla...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
