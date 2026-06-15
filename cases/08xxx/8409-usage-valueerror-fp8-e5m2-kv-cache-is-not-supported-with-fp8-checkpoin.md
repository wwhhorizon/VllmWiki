# vllm-project/vllm#8409: [Usage]: ValueError: fp8_e5m2 kv-cache is not supported with fp8 checkpoints.

| 字段 | 值 |
| --- | --- |
| Issue | [#8409](https://github.com/vllm-project/vllm/issues/8409) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: ValueError: fp8_e5m2 kv-cache is not supported with fp8 checkpoints.

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.4.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.31 Python version: 3.11.2 (main, Jul 23 2024, 17:09:09) [GCC 10.2.1 20210110] (64-bit runtime) Python platform: Linux-5.4.143.bsk.8-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40 GPU 1: NVIDIA L40 GPU 2: NVIDIA L40 GPU 3: NVIDIA L40 GPU 4: NVIDIA L40 GPU 5: NVIDIA L40 GPU 6: NVIDIA L40 GPU 7: NVIDIA L40 Nvidia driver version: Could not collect cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_heu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ith fp8 checkpoints. usage ### Your current environment ```text PyTorch version: 2.4.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.4.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: ValueError: fp8_e5m2 kv-cache is not supported with fp8 checkpoints. usage ### Your current environment ```text PyTorch version: 2.4.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40 GPU 1: NVIDIA L40 GPU 2: NVIDIA L40 GPU 3: NVIDIA L40 GPU 4: NVIDIA L40 GPU 5: NVIDIA L40 GPU 6: NVIDI...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Versions of relevant libraries: [pip3] byted-torch==2.4.0.post1 [pip3] flashinfer==0.1.6+cu124torch2.4 [pip3] numpy==1.26.3 [pip3] nvidia-cublas-cu12==12.4.2.65 [pip3] nvidia-cuda-cupti-cu12==12.4.99 [pip3] nvidia-cuda-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
