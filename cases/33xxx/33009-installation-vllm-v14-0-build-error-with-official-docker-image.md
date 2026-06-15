# vllm-project/vllm#33009: [Installation]: vLLM v14.0 Build Error with Official Docker Image

| 字段 | 值 |
| --- | --- |
| Issue | [#33009](https://github.com/vllm-project/vllm/issues/33009) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vLLM v14.0 Build Error with Official Docker Image

### Issue 正文摘录

Since I’m not very familiar with environment setup, I tried using the official Docker image directly: **Docker image**: vllm/vllm-openai:nightly-x86_64 **Codebase**: latest v14.0 I followed the official documentation: https://docs.vllm.ai/en/v0.6.1/getting_started/installation.html https://docs.vllm.ai/en/stable/getting_started/installation/gpu/#requirements ```text The output of `python collect_env.py` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 4.2.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 10 2025, 08:52:57) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.11.0-28-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ==============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: vLLM v14.0 Build Error with Official Docker Image installation Since I’m not very familiar with environment setup, I tried using the official Docker image directly: **Docker image**: vllm/vllm-openai:nigh
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: aves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.1 [pip3] mypy_extensions==1.1.0 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
