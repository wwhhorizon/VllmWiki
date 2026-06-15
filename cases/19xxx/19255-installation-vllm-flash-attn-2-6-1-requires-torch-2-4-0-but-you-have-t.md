# vllm-project/vllm#19255: [Installation]: vllm-flash-attn 2.6.1 requires torch==2.4.0, but you have torch 2.7.0 which is incompatible

| 字段 | 值 |
| --- | --- |
| Issue | [#19255](https://github.com/vllm-project/vllm/issues/19255) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vllm-flash-attn 2.6.1 requires torch==2.4.0, but you have torch 2.7.0 which is incompatible

### Issue 正文摘录

### Your current environment ```text INFO 06-06 14:46:24 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 18.04.6 LTS (x86_64) GCC version : (Ubuntu 7.5.0-6ubuntu2) 7.5.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.0 (main, Mar 1 2023, 18:26:19) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-4.15.0-156-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 GPU 2: NVIDIA GeForce RTX 4090 Nvidia driver version : 550.90.07 cuDNN version : Probably one of the followi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: vllm-flash-attn 2.6.1 requires torch==2.4.0, but you have torch 2.7.0 which is incompatible installation;stale ### Your current environment ```text INFO 06-06 14:46:24 [__init__.py:243] Automatically dete
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: xt INFO 06-06 14:46:24 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 18.04.6 LTS (x86...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 18.04.6 LTS (x86_64) GCC version : (Ubuntu 7.5....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.51.3 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.3.0 [pip3] vector-quantize-pytorch==1.18.5 [conda] jj-pytorchvideo 0.1.5 pypi_0 pypi [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cubl
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: transformers-stream-generator==0.0.5 [pip3] triton==3.3.0 [pip3] vector-quantize-pytorch==1.18.5 [conda] jj-pytorchvideo 0.1.5 pypi_0 pypi [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
