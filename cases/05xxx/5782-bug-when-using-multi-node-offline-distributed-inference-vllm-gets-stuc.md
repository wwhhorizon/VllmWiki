# vllm-project/vllm#5782: [Bug]: When using multi-node offline distributed inference, VLLM gets stuck at the last few samples of inference

| 字段 | 值 |
| --- | --- |
| Issue | [#5782](https://github.com/vllm-project/vllm/issues/5782) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using multi-node offline distributed inference, VLLM gets stuck at the last few samples of inference

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.24.1 Libc version: glibc-2.31 Python version: 3.8.10 (default, Mar 13 2023, 10:26:41) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.4.119-19-0009.11-x86_64-with-glibc2.29 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB GPU 4: NVIDIA A100-SXM4-40GB GPU 5: NVIDIA A100-SXM4-40GB GPU 6: NVIDIA A100-SXM4-40GB GPU 7: NVIDIA A100-SXM4-40GB Nvidia driver version: 525.85.12 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0 /usr/lib/x86...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: python collect_env.py` ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: down: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization Vuln...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: l clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca Versions of rel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
