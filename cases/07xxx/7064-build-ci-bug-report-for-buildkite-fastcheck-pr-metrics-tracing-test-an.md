# vllm-project/vllm#7064: [BUILD/CI Bug]: Report for buildkite/fastcheck/pr/metrics-tracing-test and suggesting a solution.

| 字段 | 值 |
| --- | --- |
| Issue | [#7064](https://github.com/vllm-project/vllm/issues/7064) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [BUILD/CI Bug]: Report for buildkite/fastcheck/pr/metrics-tracing-test and suggesting a solution.

### Issue 正文摘录

### Your current environment PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-45-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version: 535.183.06 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.1.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU:...

## 现有链接修复摘要

#6926 [SpecDecode] Support FlashInfer in DraftModelRunner | #7065 Fix tracing.py | #7266 [CI/Build] Pin OpenTelemetry versions and make availability errors clearer

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [BUILD/CI Bug]: Report for buildkite/fastcheck/pr/metrics-tracing-test and suggesting a solution. bug ### Your current environment PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: current environment PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: in brs arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm V...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.5.40 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version: 535.183.06 cuDNN version: Probably one of the following: /usr/lib/x...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: x async abort: Not affected Versions of relevant libraries: [pip3] flashinfer==0.1.2+cu121torch2.3 [pip3] mypy==1.9.0 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6926](https://github.com/vllm-project/vllm/pull/6926) | mentioned | 0.45 | [SpecDecode] Support FlashInfer in DraftModelRunner | ldkite/fastcheck/pr/metrics-tracing-test`. when proceeding with pr #6926 , unlike the previous pr, an valueerror occurred in the metrics-tracing-test. ``` [2024-08-02t04:09:43z] |
| [#7065](https://github.com/vllm-project/vllm/pull/7065) | closes_keyword | 0.95 | Fix tracing.py | FIX #7064 (*link existing issues this PR will resolve*) The issue with importing opentelemetry in `vllm/tracing.py` will be resolved. **BEFORE SUBMITTING, PLEASE READ THE CH |
| [#7266](https://github.com/vllm-project/vllm/pull/7266) | mentioned | 0.6 | [CI/Build] Pin OpenTelemetry versions and make availability errors clearer | lability error messages. These changes aim to mitigate issues like #7064, improving the stability and debuggability of the build process. **BEFORE SUBMITTING, PLEASE READ THE CHEC |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
