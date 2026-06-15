# vllm-project/vllm#32547: [Performance]: Performance degradation from 0.13.0 to 0.14.0rc2

| 字段 | 值 |
| --- | --- |
| Issue | [#32547](https://github.com/vllm-project/vllm/issues/32547) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Performance degradation from 0.13.0 to 0.14.0rc2

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression 4*rtx pro 6000 GLM-4.7-GPTQ-Int4-Int8Mix 0.13.0 about 96 tps with mtp 0.14.0rc2 about 87 tps with mtp ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text (vllm-latest) aabbccddwasd@gpu-server:~/AI-stuffs$ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 20:16:04) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-90-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ==============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: rove performance _No response_ ### Report of performance regression 4*rtx pro 6000 GLM-4.7-GPTQ-Int4-Int8Mix 0.13.0 about 96 tps with mtp 0.14.0rc2 about 87 tps with mtp ### Misc discussion on performance _No response_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: onse_ ### Report of performance regression 4*rtx pro 6000 GLM-4.7-GPTQ-Int4-Int8Mix 0.13.0 about 96 tps with mtp 0.14.0rc2 about 87 tps with mtp ### Misc discussion on performance _No response_ ### Your current environm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: @gpu-server:~/AI-stuffs$ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: pb_ret arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
