# vllm-project/vllm#3463: [Bug]: ValueError: Model architectures ['Qwen2ForCausalLM'] are not supported for now

| 字段 | 值 |
| --- | --- |
| Issue | [#3463](https://github.com/vllm-project/vllm/issues/3463) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Model architectures ['Qwen2ForCausalLM'] are not supported for now

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.28.3 Libc version: glibc-2.31 Python version: 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.4.0-99-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100S-PCIE-32GB Nvidia driver version: 525.105.17 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.6.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: not supported for now bug ### Your current environment ```text PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: ValueError: Model architectures ['Qwen2ForCausalLM'] are not supported for now bug ### Your current environment ```text PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM use...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ValueError: Model architectures ['Qwen2ForCausalLM'] are not supported for now bug ### Your current environment ```text PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM use...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rent environment ```text PyTorch version: 2.1.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: elevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.1+cu118 [pip3] triton==2.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.1.1+cu118 pypi_0 pypi [conda] triton 2.1.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
