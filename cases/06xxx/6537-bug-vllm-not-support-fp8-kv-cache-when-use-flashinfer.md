# vllm-project/vllm#6537: [Bug]: vllm not support fp8 kv cache when use flashinfer

| 字段 | 值 |
| --- | --- |
| Issue | [#6537](https://github.com/vllm-project/vllm/issues/6537) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm not support fp8 kv cache when use flashinfer

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.119-19.0009.44-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 GPU 4: NVIDIA L20 GPU 5: NVIDIA L20 GPU 6: NVIDIA L20 GPU 7: NVIDIA L20 Nvidia driver version: 535.161.07 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudn...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC vers...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: vllm not support fp8 kv cache when use flashinfer bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: vllm not support fp8 kv cache when use flashinfer bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
