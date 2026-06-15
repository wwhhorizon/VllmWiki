# vllm-project/vllm#14446: [Usage]: After starting the QwQ-32B model normally, it was found that the model could not output the thought tag normally

| 字段 | 值 |
| --- | --- |
| Issue | [#14446](https://github.com/vllm-project/vllm/issues/14446) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: After starting the QwQ-32B model normally, it was found that the model could not output the thought tag normally

### Issue 正文摘录

### Your current environment INFO 03-08 00:00:39 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 11.2.0 Clang version: Could not collect CMake version: version 3.31.5 Libc version: glibc-2.17 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.92.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10 GPU 1: NVIDIA A10 GPU 2: NVIDIA A10 GPU 3: NVIDIA A10 GPU 4: NVIDIA A10 GPU 5: NVIDIA A10 GPU 6: NVIDIA A10 GPU 7: NVIDIA A10 Nvidia driver version: 550.127.08 cuDNN version: Probably one of the following: /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_adv.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_cnn.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Cor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nt INFO 03-08 00:00:39 __init__.py:190] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: After starting the QwQ-32B model normally, it was found that the model could not output the thought tag normally usage ### Your current environment INFO 03-08 00:00:39 __init__.py:190] Automatically detected pl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.49.0 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 11.2.0 C...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
