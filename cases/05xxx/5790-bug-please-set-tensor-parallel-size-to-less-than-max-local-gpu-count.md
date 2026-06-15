# vllm-project/vllm#5790: [Bug]: please set tensor_parallel_size to less than max local gpu count

| 字段 | 值 |
| --- | --- |
| Issue | [#5790](https://github.com/vllm-project/vllm/issues/5790) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: please set tensor_parallel_size to less than max local gpu count

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-41-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 Nvidia driver version: 535.183.01 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: count bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev sev_es Virtualization: AMD-V...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: xsaveerptr rdpru wbnoinvd amd_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
