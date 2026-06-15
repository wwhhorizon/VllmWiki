# vllm-project/vllm#6407: when i set tensor_parallel_size>1(A100 * 4), it does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#6407](https://github.com/vllm-project/vllm/issues/6407) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> when i set tensor_parallel_size>1(A100 * 4), it does not work

### Issue 正文摘录

### Your current environment ```text WARNING 07-13 11:30:05 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For multi-node inference, please install Ray with `pip install ray`. PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 11.3.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.17 Python version: 3.9.19 (main, May 6 2024, 19:43:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.114.2.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.7.64 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3: NVIDIA A100 80GB PCIe Nvidia driver version: 515.43.04 cuDNN version: Probably one of the following: /usr/lib/libcudnn.so /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8.4.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.4.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.4.1 /usr/local/cuda-11.7/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: t environment ```text WARNING 07-13 11:30:05 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For multi-node inference, please install Ray with `pip install ray`. PyTorch version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: when i set tensor_parallel_size>1(A100 * 4), it does not work bug ### Your current environment ```text WARNING 07-13 11:30:05 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 11.7.64 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3: NVIDIA A100 80GB PCIe Nvidi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: dio==2.3.0 [pip3] torchvision==0.18.0 [pip3] transformers==4.42.4 [pip3] triton==2.3.0 [conda] blas 1.0 mkl [conda] ffmpeg 4.3 hf484d3e_0 pytorch [conda] libjpeg-turbo 2.0.0 h9bf14
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: all Ray with `pip install ray`. PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 11.3.0 Clang version: C...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
