# vllm-project/vllm#16343: [Bug]: orch.OutOfMemoryError: CUDA out of memory. Tried to allocate 350.00 MiB. GPU 0 has a total capacity of 23.68 GiB of which 212.81

| 字段 | 值 |
| --- | --- |
| Issue | [#16343](https://github.com/vllm-project/vllm/issues/16343) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: orch.OutOfMemoryError: CUDA out of memory. Tried to allocate 350.00 MiB. GPU 0 has a total capacity of 23.68 GiB of which 212.81

### Issue 正文摘录

### Your current environment I am using docker image but installed it to be sure: ``` INFO 04-09 14:53:41 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-57-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 Nvidia driver version: 550.120 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn.so.9.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.6.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.6.0 /usr/lib/x86_64-linu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: CUDA out of memory. Tried to allocate 350.00 MiB. GPU 0 has a total capacity of 23.68 GiB of which 212.81 bug;stale ### Your current environment I am using docker image but installed it to be sure: ``` INFO 04-09 14:53:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd cppc amd_ibpb_ret arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pau...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: orch.OutOfMemoryError: CUDA out of memory. Tried to allocate 350.00 MiB. GPU 0 has a total capacity of 23.68 GiB of which 212.81 bug;stale ### Your current environment I am using docker image but installed it to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 350.00 MiB. GPU 0 has a total capacity of 23.68 GiB of which 212.81 bug;stale ### Your current environment I am using docker image but installed it to be sure: ``` INFO 04-09 14:53:41 [__init__.py:239] Automatically det...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
