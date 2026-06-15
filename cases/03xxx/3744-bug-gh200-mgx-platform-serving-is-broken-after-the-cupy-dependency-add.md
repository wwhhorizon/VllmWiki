# vllm-project/vllm#3744: [Bug]:  GH200 MGX platform serving is broken after the cupy dependency addition 

| 字段 | 值 |
| --- | --- |
| Issue | [#3744](https://github.com/vllm-project/vllm/issues/3744) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  GH200 MGX platform serving is broken after the cupy dependency addition 

### Issue 正文摘录

### Your current environment ```text ollecting environment information... PyTorch version: 2.2.0a0+81ea7a4 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.28.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.2.0-1012-nvidia-64k-aarch64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: GH200 480GB Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/aarch64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/aarch64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/aarch64-linux-gnu/libcudnn_cnn_infer.so.8.9.7 /usr/lib/aarch64-linux-gnu/libcudnn_cnn_train.so.8.9.7 /usr/lib/aarch64-linux-gnu/libcudnn_ops_infer.so.8.9.7 /usr/lib/aarch64-linux-gnu/libcudnn_ops_train.so.8.9.7 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Arch...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: GH200 MGX platform serving is broken after the cupy dependency addition bug;stale ### Your current environment ```text ollecting environment information... PyTorch version: 2.2.0a0+81ea7a4 Is debug build: False C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nt information... PyTorch version: 2.2.0a0+81ea7a4 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti L1d cache: 4.5 MiB (72 instances) L1i cache: 4.5 MiB (72 instances) L2 cache: 72 MiB (72 instances) L3 cache:
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bug;stale ### Your current environment ```text ollecting environment information... PyTorch version: 2.2.0a0+81ea7a4 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to build PyTorch: N/A OS: Ubuntu 22.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 0 MGX platform serving is broken after the cupy dependency addition bug;stale ### Your current environment ```text ollecting environment information... PyTorch version: 2.2.0a0+81ea7a4 Is debug build: False CUDA used to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
