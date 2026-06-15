# vllm-project/vllm#25802: [Usage]: vllm.third_party.pynvml.NVMLError_InvalidArgument: Invalid Argument

| 字段 | 值 |
| --- | --- |
| Issue | [#25802](https://github.com/vllm-project/vllm/issues/25802) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm.third_party.pynvml.NVMLError_InvalidArgument: Invalid Argument

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` (uv run collect_env.py) warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warning. INFO 09-27 10:47:25 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.13.7 (main, Sep 2 2025, 14:21:46) [Clang 20.1.4 ] (64-bit runtime) Python platform : Linux-6.11.0-1027-oem-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : C...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: of `python collect_env.py` (uv run collect_env.py) warning: The `extra-build-dependencies` option is experimental and may change without warning. Pass `--preview-features extra-build-dependencies` to disable this warnin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: g. INFO 09-27 10:47:25 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: _.py:239] Automatically detected platform cuda. Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (U...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 11:06:21 [__init__.py:239] Automatically detected platform cuda. `torch_dtype` is deprecated! Use `dtype` instead! INFO 09-27 11:06:29 [config.py:600] This model supports multiple tasks: {'generate', 'reward', 'score',...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Vulnerable:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
