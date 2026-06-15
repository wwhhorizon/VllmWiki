# vllm-project/vllm#39170: [Intel-GPU]: Using docker image at intel/vllm:0.17.0-xpu -> RuntimeError: PyTorch was compiled without CUDA support

| 字段 | 值 |
| --- | --- |
| Issue | [#39170](https://github.com/vllm-project/vllm/issues/39170) |
| 状态 | open |
| 标签 | installation;intel-gpu |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Intel-GPU]: Using docker image at intel/vllm:0.17.0-xpu -> RuntimeError: PyTorch was compiled without CUDA support

### Issue 正文摘录

### Your current environment I want to try vllm via docker on my intel Arc B60 system. I followed the documentation for the docker method provided by intel, but always get the error `RuntimeError:` PyTorch was compiled without CUDA support I also tried the llm-scaler docker from intel. That works, but it seems it is not really maintained by intel. Any idea what to do? Thank you! ```text The output of `python collect_env.py` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 4.2.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+xpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jan 22 2026, 20:57:42) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.17.0-19-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Intel-GPU]: Using docker image at intel/vllm:0.17.0-xpu -> RuntimeError: PyTorch was compiled without CUDA support installation;intel-gpu ### Your current environment I want to try vllm via docker on my intel Arc B60 s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: e at intel/vllm:0.17.0-xpu -> RuntimeError: PyTorch was compiled without CUDA support installation;intel-gpu ### Your current environment I want to try vllm via docker on my intel Arc B60 system. I followed the document...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: eError:` PyTorch was compiled without CUDA support I also tried the llm-scaler docker from intel. That works, but it seems it is not really maintained by intel. Any idea what to do? Thank you! ```text The output of `pyt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
