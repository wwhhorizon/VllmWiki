# vllm-project/vllm#6370: [Bug]: vLLM 0.5.1 tensor parallel 2 hang

| 字段 | 值 |
| --- | --- |
| Issue | [#6370](https://github.com/vllm-project/vllm/issues/6370) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.5.1 tensor parallel 2 hang

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.9.0 (default, Nov 15 2020, 14:28:56) [GCC 7.3.0] (64-bit runtime) Python platform: Linux-5.4.0-176-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.2.91 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800 80GB PCIe GPU 1: NVIDIA A800 80GB PCIe GPU 2: NVIDIA A800 80GB PCIe GPU 3: NVIDIA A800 80GB PCIe GPU 4: NVIDIA A800 80GB PCIe GPU 5: NVIDIA A800 80GB PCIe GPU 6: NVIDIA A800 80GB PCIe GPU 7: NVIDIA A800 80GB PCIe Nvidia driver version: 535.154.05 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.8.0 /usr/lib/...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and sec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC vers...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: l clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rallel 2 hang bug ### Your current environment Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
