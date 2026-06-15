# vllm-project/vllm#16909: [Bug]: oom occurs when 128+128 256 concurrency, while 4K+4K 256 concurrency is ok. DeepSeek-R1-awq benchmark test.

| 字段 | 值 |
| --- | --- |
| Issue | [#16909](https://github.com/vllm-project/vllm/issues/16909) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: oom occurs when 128+128 256 concurrency, while 4K+4K 256 concurrency is ok. DeepSeek-R1-awq benchmark test.

### Issue 正文摘录

### Your current environment /usr/local/lib/python3.10/site-packages/vllm/transformers_utils/tokenizers/cpm_9g.py:7: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html import pkg_resources INFO 04-21 15:53:01 __init__.py:208] Automatically detected platform cuda. Collecting environment information... /usr/local/corex-4.3.0.20250309/lib64/python3/dist-packages/_distutils_hack/__init__.py:26: UserWarning: Setuptools is replacing distutils. warnings.warn("Setuptools is replacing distutils.") PyTorch version: 2.4.1 Is debug build: False CUDA used to build PyTorch: 10.2 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-6ubuntu2) 7.5.0 Clang version: 16.0.6 (ssh://git@bitbucket.iluvatar.ai:7999/csys/ixcc.git a8c75f43607e5a500838757b8a1ab91078d722da) CMake version: version 3.25.2-corex.4.3.0.20250309 Libc version: glibc-2.31 Python version: 3.10.12 (main, Mar 9 2025, 16:33:20) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-5.10.134-14.zncgsl6.x86_64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 10.2.89 CUDA_MODULE_LOADING set to: LAZY GPU models and conf...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html import pkg_resources INFO 04-21 15:53:01 __init__.py:208] Automatically detected platform cuda. Collecting environment information... /usr/local/cor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ces INFO 04-21 15:53:01 __init__.py:208] Automatically detected platform cuda. Collecting environment information... /usr/local/corex-4.3.0.20250309/lib64/python3/dist-packages/_distutils_hack/__init__.py:26: UserWarnin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:208] Automatically detected platform cuda. Collecting environment information... /usr/local/corex-4.3.0.20250309/lib64/python3/dist-packages/_distutils_hack/__init__.py:26: UserWarning: Setuptools is replacing dist...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: oom occurs when 128+128 256 concurrency, while 4K+4K 256 concurrency is ok. DeepSeek-R1-awq benchmark test. bug;stale ### Your current environment /usr/local/lib/python3.10/site-packages/vllm/transformers_utils/t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
