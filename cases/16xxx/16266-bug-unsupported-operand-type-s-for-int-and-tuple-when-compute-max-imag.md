# vllm-project/vllm#16266: [Bug]: unsupported operand type(s) for -: 'int' and 'tuple' when compute max_images in qwen2.5vl

| 字段 | 值 |
| --- | --- |
| Issue | [#16266](https://github.com/vllm-project/vllm/issues/16266) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: unsupported operand type(s) for -: 'int' and 'tuple' when compute max_images in qwen2.5vl

### Issue 正文摘录

### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.18.4 Libc version: glibc-2.31 Python version: 3.11.11 (main, Feb 14 2025, 14:40:43) [GCC 10.2.1 20210110] (64-bit runtime) Python platform: Linux-5.4.143.bsk.8-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 Nvidia driver version: 535.161.08 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.7 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ompute max_images in qwen2.5vl bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rted operand type(s) for -: 'int' and 'tuple' when compute max_images in qwen2.5vl bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.51.1 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.2.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.8.3 vLLM Build Flags: CUDA Archs: N...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 wbnoinvd arat avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid cldemote mo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
