# vllm-project/vllm#5550: [Bug]: OOM when setting prompt_logprobs=1

| 字段 | 值 |
| --- | --- |
| Issue | [#5550](https://github.com/vllm-project/vllm/issues/5550) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM when setting prompt_logprobs=1

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.31 Python version: 3.10.0 (default, Mar 3 2022, 09:58:08) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.4.0-162-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.54.03 cuDNN version: Probably one of the following: /usr/local/cuda-11.0/targets/x86_64-linux/lib/libcudnn.so.8.4.1 /usr/local/cuda-11.0/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.4.1 /usr/local/cuda-11.0/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.4.1 /usr/local/cuda-11.0/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.4.1 /usr/local/cuda-11.0/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.4.1 /usr/local/cuda-11.0/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.4.1 /usr/local/cuda-11.0/...

## 现有链接修复摘要

#5355 [Bugfix] Take the VRAM usage of prompt_logprobs into account

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: l clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload vgif umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: OOM when setting prompt_logprobs=1 bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM use...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5355](https://github.com/vllm-project/vllm/pull/5355) | closes_keyword | 0.95 | [Bugfix] Take the VRAM usage of prompt_logprobs into account | FIX #5550 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist (Click to Expand) </b>< |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
