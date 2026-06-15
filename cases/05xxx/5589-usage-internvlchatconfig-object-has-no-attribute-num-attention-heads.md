# vllm-project/vllm#5589: [Usage]: 'InternVLChatConfig' object has no attribute 'num_attention_heads'

| 字段 | 值 |
| --- | --- |
| Issue | [#5589](https://github.com/vllm-project/vllm/issues/5589) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: 'InternVLChatConfig' object has no attribute 'num_attention_heads'

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.17 Python version: 3.11.0 (main, Mar 1 2023, 18:26:19) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.92.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 GPU 4: NVIDIA L20 GPU 5: NVIDIA L20 GPU 6: NVIDIA L20 GPU 7: NVIDIA L20 Nvidia driver version: 535.154.05 cuDNN version: Probably one of the following: /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn.so.8.9.7 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.7 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.7 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.7 /usr/local/cuda-12.1/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: 'InternVLChatConfig' object has no attribute 'num_attention_heads' usage ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA us...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: n collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 4.8.5 201506...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: transformers==4.41.2 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==2.3.0 [conda] numpy 1.26.3 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch 2.3.0+cu121
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ython collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 4.8.5 20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
