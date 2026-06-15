# vllm-project/vllm#7567: [Usage]: Extremely slow inference with Llama 3.1 70b Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#7567](https://github.com/vllm-project/vllm/issues/7567) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Extremely slow inference with Llama 3.1 70b Instruct

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-1024-aws-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB GPU 4: NVIDIA A100-SXM4-40GB GPU 5: NVIDIA A100-SXM4-40GB GPU 6: NVIDIA A100-SXM4-40GB GPU 7: NVIDIA A100-SXM4-40GB Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Vendor ID: GenuineIntel Mod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Extremely slow inference with Llama 3.1 70b Instruct usage;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.0 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.4@4db5176d9758b720b05460c50ace3c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
