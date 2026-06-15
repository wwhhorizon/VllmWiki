# vllm-project/vllm#4157: [Bug]: 0.4.0.post1: ValueError: Model architectures ['MiniCPMForCausalLM'] are not supported for now

| 字段 | 值 |
| --- | --- |
| Issue | [#4157](https://github.com/vllm-project/vllm/issues/4157) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.4.0.post1: ValueError: Model architectures ['MiniCPMForCausalLM'] are not supported for now

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.8.10 (default, Jun 4 2021, 15:09:15) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.15.0-101-generic-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 11.6.124 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 D Nvidia driver version: 550.54.14 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.4.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.4.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: 0.4.0.post1: ValueError: Model architectures ['MiniCPMForCausalLM'] are not supported for now bug ### Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: Fa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: 0.4.0.post1: ValueError: Model architectures ['MiniCPMForCausalLM'] are not supported for now bug ### Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: Fa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation; safe RET Vulnerability Spec store bypass: Mitiga...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
