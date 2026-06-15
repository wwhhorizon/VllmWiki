# vllm-project/vllm#6896: [Bug]: When using vllm in a Ray actor, the error "No CUDA GPUs are available" occurs.

| 字段 | 值 |
| --- | --- |
| Issue | [#6896](https://github.com/vllm-project/vllm/issues/6896) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using vllm in a Ray actor, the error "No CUDA GPUs are available" occurs.

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0a0+40ec155e58.nv24.03 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.28.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-4.19.91-014-kangaroo.2.10.13.5c249cdaf.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H800 GPU 1: NVIDIA H800 Nvidia driver version: 525.105.17 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.0.0 HIP runtime version: N/A...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: are available" occurs. bug ### Your current environment ```text PyTorch version: 2.3.0a0+40ec155e58.nv24.03 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: When using vllm in a Ray actor, the error "No CUDA GPUs are available" occurs. bug ### Your current environment ```text PyTorch version: 2.3.0a0+40ec155e58.nv24.03 Is debug build: False CUDA used to build PyTorch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H800 GPU 1: NVIDIA H800 Nvidia driver version: 525.105.17 cuDNN version: Probably one of the following: /us...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 wbnoinvd avx512vbmi umip pku waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid cldemote movdiri movdi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] optree==0.10.0 [pip3] pytorch-quantization==2.1.2 [pip3] pytorch-triton==2.2.0+e28a256d7 [pip3] torch==2.3.0a0+40ec155e58.nv24.3 [pip3] torch-tensorrt==2.3.0a0 [pip3] torchdata==0.7.1a0 [pip3] torchtext==0.17.0a0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
