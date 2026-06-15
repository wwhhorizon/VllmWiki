# vllm-project/vllm#24950: [Usage]: AttributeError: 'Parameter' object has no attribute 'load_column_parallel_weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#24950](https://github.com/vllm-project/vllm/issues/24950) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: AttributeError: 'Parameter' object has no attribute 'load_column_parallel_weight'

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` INFO 09-16 15:35:11 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /root/miniconda3/lib/python3.11/site-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils. warnings.warn("Setuptools is replacing distutils.") ============================== System Info ============================== OS : Ubuntu 20.04.4 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.15.0-89-generic-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LO...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils. warnings.warn("Setuptools is replacing distutils.") ============================== System Info ============================== OS :...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: y` INFO 09-16 15:35:11 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /root/miniconda3/lib/python3.11/site-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:239] Automatically detected platform cuda. Collecting environment information... /root/miniconda3/lib/python3.11/site-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils. warning...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.2.3 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
