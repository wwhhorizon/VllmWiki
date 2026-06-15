# vllm-project/vllm#12350: [Bug]: Cannot serve Qwen2.5 in OpenVINO

| 字段 | 值 |
| --- | --- |
| Issue | [#12350](https://github.com/vllm-project/vllm/issues/12350) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator;quantization |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot serve Qwen2.5 in OpenVINO

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.31.4 Libc version: glibc-2.31 Python version: 3.11.4 (main, Jul 5 2023, 13:45:01) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.14.0-284.25.1.el9_2.x86_64-x86_64-with-glibc2.31 Is CUDA available: False CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 D Nvidia driver version: 550.90.07 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.7.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True C...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: Your current environment Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl Vuln...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: veerptr rdpru wbnoinvd amd_ppin brs arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ironment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Cannot serve Qwen2.5 in OpenVINO bug ### Your current environment Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
