# vllm-project/vllm#41410: [Bug]: DSV4 TileLang JIT fails with 'Permission denied: /tmp/tvm-debug-mode-tempdirs/...' on shared multi-user hosts

| 字段 | 值 |
| --- | --- |
| Issue | [#41410](https://github.com/vllm-project/vllm/issues/41410) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;kernel;moe;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSV4 TileLang JIT fails with 'Permission denied: /tmp/tvm-debug-mode-tempdirs/...' on shared multi-user hosts

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On a shared multi-user machine, starting vLLM with a model that JIT-compiles a TileLang kernel (e.g. DeepSeek-V4 with the `mhc_pre_big_fuse_tilelang` indexer kernel) crashes during `profile_run` with: ``` RuntimeError: [Errno 13] Permission denied: '/tmp/tvm-debug-mode-tempdirs/2026-04-30T19-45-18___mxg1ylol' ``` #### Reproduction ```bash vllm serve deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 4 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v4 ``` …on a host where another user has previously run TileLang and `/tmp/tvm-debug-mode-tempdirs/` already exists, owned by them with mode `0755`: ``` $ ls -ld /tmp/tvm-debug-mode-tempdirs/ drwxr-xr-x. 14 otheruser otheruser 280 Apr 30 17:31 /tmp/tvm-debug-mode-tempdirs/ ``` #### Root cause `tilelang/contrib/nvcc.py:70` calls: ```python temp = utils.tempdir(keep_for_debug=not env.should_cleanup_temp_files()) ``` `should_cleanup_temp_files()` is False by default (env var `TILELANG_CLEANUP_TEMP_FILES` unset), so `keep_f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bug On a shared multi-user machine, starting vLLM with a model that JIT-compiles a TileLang kernel (e.g. DeepSeek-V4 with the `mhc_pre_big_fuse_tilelang` indexer kernel) crashes during `profile_run` with: ``` RuntimeErr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rve deepseek-ai/DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 4 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: leLang JIT path doesn't rely on a world-shared `/tmp` subdir whose ownership is determined by whichever user happened to compile first. (Upstream fix in TileLang/TVM would be even better — using a per-user prefix.) ####...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: DeepSeek-V4-Flash \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 4 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-too...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: t-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --tensor-parallel-size 4 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --reasoning-par...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
