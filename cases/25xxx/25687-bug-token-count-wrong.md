# vllm-project/vllm#25687: [Bug]: Token count wrong ?

| 字段 | 值 |
| --- | --- |
| Issue | [#25687](https://github.com/vllm-project/vllm/issues/25687) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Token count wrong ?

### Issue 正文摘录

### Your current environment (root) root@G5090-03:~# python collect_env.py Collecting environment information... uv is set ============================== System Info ============================== OS : Debian GNU/Linux 13 (trixie) (x86_64) GCC version : (Debian 14.2.0-19) 14.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.41 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.3 (main, Aug 26 2025, 14:31:38) [GCC 14.2.0] (64-bit runtime) Python platform : Linux-6.14.8-2-pve-x86_64-with-glibc2.41 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 Nvidia driver version : 570.172.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ==============...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: OS : Debian GNU/Linux 13 (trixie) (x86_64) GCC version : (Debian 14.2.0-19) 14.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.41 ==========================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.3 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: (root) root@G5090-03:~# python collect_env.py Collecting environment information... uv is set ============================== System Info ============================== OS : Debian GNU/Linux 13 (trixie) (x86_64) GCC vers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: d cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni av...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
