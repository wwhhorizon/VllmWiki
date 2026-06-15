# vllm-project/vllm#23049: [BUG]:torch.OutOfMemoryError: CUDA out of memory.

| 字段 | 值 |
| --- | --- |
| Issue | [#23049](https://github.com/vllm-project/vllm/issues/23049) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [BUG]:torch.OutOfMemoryError: CUDA out of memory.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 | packaged by Anaconda, Inc. | (main, Jun 5 2025, 13:09:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 Nvidia driver version : 580.97 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.12.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.12.0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [BUG]:torch.OutOfMemoryError: CUDA out of memory. usage ### Your current environment ```text The output of `python collect_env.py` ``` ============================== System Info ============================== OS : U
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: untime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 Nvidia driver version : 580.97 cuDNN version : Probably one of the following: /usr/lib/x86_64-linu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 16 clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload avx512vbmi umip avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx_vnni avx512_bf16 clzero xsaveerptr arat npt nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold v_vmsave_vmload avx512vbmi umip av...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
