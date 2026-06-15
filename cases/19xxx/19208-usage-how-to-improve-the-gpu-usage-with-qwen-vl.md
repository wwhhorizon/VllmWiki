# vllm-project/vllm#19208: [Usage]: How to improve the gpu usage with Qwen-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#19208](https://github.com/vllm-project/vllm/issues/19208) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to improve the gpu usage with Qwen-VL

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` INFO 06-05 19:47:16 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : TencentOS Server 4.2 (x86_64) GCC version : (Tencent Compiler 12.3.1.2) 12.3.1 20230912 (TencentOS 12.3.1.2-3) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.38 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.241-1-tlinux4-0017.7-x86_64-with-glibc2.38 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ======= OS : TencentOS Server 4.2 (x86_64) GCC version : (Tencent Compiler 12.3.1.2) 12.3.1 20230912 (TencentOS 12.3.1.2-3) Clang version : Could not collect CMake version : Could not collect Libc version
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Usage]: How to improve the gpu usage with Qwen-VL usage;stale ### Your current environment ```text The output of `python collect_env.py` INFO 06-05 19:47:16 [__init__.py:243] Automatically detected platform cuda. Colle...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: y` INFO 06-05 19:47:16 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : TencentOS Server 4.2 (x...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to improve the gpu usage with Qwen-VL usage;stale ### Your current environment ```text The output of `python collect_env.py` INFO 06-05 19:47:16 [__init__.py:243] Automatically detected platform cuda. Colle...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 clzero irperf xsaveerptr wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
