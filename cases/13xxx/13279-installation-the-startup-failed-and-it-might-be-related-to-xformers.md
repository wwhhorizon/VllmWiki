# vllm-project/vllm#13279: [Installation]:  The startup failed, and it might be related to xformers.

| 字段 | 值 |
| --- | --- |
| Issue | [#13279](https://github.com/vllm-project/vllm/issues/13279) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]:  The startup failed, and it might be related to xformers.

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 11.2.1 20220127 (Red Hat 11.2.1-9) Clang version: Could not collect CMake version: version 3.26.4 Libc version: glibc-2.17 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.92.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB Nvidia driver version: 535.183.06 cuDNN version: Probably one of the following: /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn.so.8.9.6 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.6 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.6 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.6 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.9.6 /usr/local/cuda-11.4/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.9.6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: The startup failed, and it might be related to xformers. installation;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM u
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 11.2.1 2022012...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB Nvidia driver version: 535.183.06 cuDNN version: Probably one of the following: /usr/local/cu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.48.3 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rent environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 11.2.1 20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
