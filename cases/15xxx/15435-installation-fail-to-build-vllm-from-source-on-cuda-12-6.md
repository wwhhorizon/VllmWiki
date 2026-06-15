# vllm-project/vllm#15435: [Installation]: Fail to build vLLM from source on CUDA 12.6

| 字段 | 值 |
| --- | --- |
| Issue | [#15435](https://github.com/vllm-project/vllm/issues/15435) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Fail to build vLLM from source on CUDA 12.6

### Issue 正文摘录

### Your current environment ```text INFO 03-24 20:48:52 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Stream 9 (x86_64) GCC version: (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version: Could not collect CMake version: version 3.31.4 Libc version: glibc-2.34 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.4.3-0_fbk14_hardened_2601_gcd42476b84e9-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: 12.6.85 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 GPU 1: NVIDIA H100 GPU 2: NVIDIA H100 GPU 3: NVIDIA H100 GPU 4: NVIDIA H100 GPU 5: NVIDIA H100 GPU 6: NVIDIA H100 GPU 7: NVIDIA H100 Nvidia driver version: 550.90.07 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.9.6.0 /usr/lib64/libcudnn_adv.so.9.6.0 /usr/lib64/libcudnn_cnn.so.9.6.0 /usr/lib64/libcudnn_engines_precompiled.so.9.6.0 /usr/lib64/libcudnn_engines_runtime_compiled.so.9.6.0 /usr/lib64/libc...

## 现有链接修复摘要

#19095 fix: cuda 12.6 installation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: Fail to build vLLM from source on CUDA 12.6 installation;stale ### Your current environment ```text INFO 03-24 20:48:52 [__init__.py:239] Automatically detected platform cuda. Collecting environment infor
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Installation]: Fail to build vLLM from source on CUDA 12.6 installation;stale ### Your current environment ```text INFO 03-24 20:48:52 [__init__.py:239] Automatically detected platform cuda. Collecting environment info...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 clzero xsaveerptr wbnoinvd arat npt lbrv nrip_save tsc_scale vmcb_clean pausefilter pfthreshold v_vmsave_vmload vgif vnmi avx512vbmi umip pku...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: dio==2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.48.3 [pip3] triton==3.2.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Stream...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#19095](https://github.com/vllm-project/vllm/pull/19095) | closes_keyword | 0.95 | fix: cuda 12.6 installation | Fix #15435 ## Test Plan CUDA 12.6 isn't used as default but might still be useful for some people. Not sure we want to add a CI check to this? I've tested locally, but if you wa |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
