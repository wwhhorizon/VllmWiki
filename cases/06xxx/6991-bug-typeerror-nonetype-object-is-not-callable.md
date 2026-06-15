# vllm-project/vllm#6991: [Bug]: TypeError: 'NoneType' object is not callable

| 字段 | 值 |
| --- | --- |
| Issue | [#6991](https://github.com/vllm-project/vllm/issues/6991) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: 'NoneType' object is not callable

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-187-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-PCIE-40GB GPU 1: NVIDIA A100-PCIE-40GB Nvidia driver version: 535.183.01 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.7 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: True CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-PCIE-40GB GPU 1: NVIDIA A100-PCIE-40GB Nvidia driver version: 535.183.01 cuDNN version: Probably one...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: object is not callable bug ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Not affected Vulnerability Spec store bypass...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ogle--gemma-2-9b-it/snapshots/1937c70277fcc5f7fb0fc772fc5bc69378996e71 --dtype bfloat16 --host 0.0.0.0 --port 8888 --api-key test-000 --max-model-len 4096 --gpu-memory-utilization 0.5 ``` logs ``` INFO 07-31 13:54:35 ap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
