# vllm-project/vllm#8878: [Installation]: Cannot compile flash attention when building from source

| 字段 | 值 |
| --- | --- |
| Issue | [#8878](https://github.com/vllm-project/vllm/issues/8878) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Cannot compile flash attention when building from source

### Issue 正文摘录

### Your current environment The doc did not specify what CUDA version is required, but the recommended Docker image `nvcr.io/nvidia/pytorch:23.10-py3` uses 12.2. The output of `python collect_env.py`, running from the NVIDIA PyTorch 23.10 Docker image. ``` Collecting environment information... PyTorch version: 2.1.0a0+32f93b1 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-122-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A30 Nvidia driver version: 535.183.01 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_tra...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: Cannot compile flash attention when building from source installation ### Your current environment The doc did not specify what CUDA version is required, but the recommended Docker image `nvcr.io/nvidia/p
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: installation ### Your current environment The doc did not specify what CUDA version is required, but the recommended Docker image `nvcr.io/nvidia/pytorch:23.10-py3` uses 12.2. The output of `python collect_env.py`, runn...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: from the NVIDIA PyTorch 23.10 Docker image. ``` Collecting environment information... PyTorch version: 2.1.0a0+32f93b1 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sme sev sev_es Virtualization: A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Installation]: Cannot compile flash attention when building from source installation ### Your current environment The doc did not specify what CUDA version is required, but the recommended Docker image `nvcr.io/nvidia/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
