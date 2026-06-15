# vllm-project/vllm#8730: [Feature]: Multi-Modality Support for Loading Local Files (Images & Videos)

| 字段 | 值 |
| --- | --- |
| Issue | [#8730](https://github.com/vllm-project/vllm/issues/8730) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Multi-Modality Support for Loading Local Files (Images & Videos)

### Issue 正文摘录

### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.17 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.105.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version: 545.23.08 cuDNN version: Probably one of the following: /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.9.1 /usr/local/cuda-12.0/targets/x86_64-linux/lib/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ) good first issue;feature request ### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.0.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version: 545.23.08 cuDNN version: Probably one of the following: /usr/local/c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.43.3 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 4.8.5 201...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
