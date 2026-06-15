# vllm-project/vllm#7135: [Installation]: ERROR: Failed to build installable wheels for some pyproject.toml based projects (vllm, xformers, vllm-nccl-cu12)

| 字段 | 值 |
| --- | --- |
| Issue | [#7135](https://github.com/vllm-project/vllm/issues/7135) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | activation;attention;cuda;fp8;operator;quantization |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: ERROR: Failed to build installable wheels for some pyproject.toml based projects (vllm, xformers, vllm-nccl-cu12)

### Issue 正文摘录

### Your current environment ```text Python version: 3.12.3 PyTorch version: 2.3.1+cu121 ``` ### How you are installing vllm ``` pip install vllm ``` Building wheels for collected packages: vllm, xformers, vllm-nccl-cu12 Building wheel for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building wheel for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [339 lines of output] /mnt/sd3/pip-build-env-vtc555m0/overlay/lib/python3.12/site-packages/setuptools/dist.py:447: SetuptoolsDeprecationWarning: Invalid dash-separated options !! ******************************************************************************** Usage of dash-separated 'index-url' will not be supported in future versions. Please use the underscore name 'index_url' instead. By 2024-Sep-26, you need to update your project and remove deprecated calls or your builds will no longer be supported. See https://setuptools.pypa.io/en/latest/userguide/declarative_config.html for details. ******************************************************************************** !! opt = self.warn_dash_deprecation(opt, section) running bdist_wheel running build running build_py creating build creating...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: ERROR: Failed to build installable wheels for some pyproject.toml based projects (vllm, xformers, vllm-nccl-cu12) installation;stale ### Your current environment ```text Python version: 3.12.3 PyTorch ver
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: See https://setuptools.pypa.io/en/latest/userguide/declarative_config.html for details. ******************************************************************************** !! opt = self.warn_dash_deprecation(opt, section)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: python-312/vllm/attention/backends copying vllm/attention/backends/rocm_flash_attn.py -> build/lib.linux-x86_64-cpython-312/vllm/attention/backends copying vllm/attention/backends/flashinfer.py -> build/lib.linux-x86_64...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: roject.toml based projects (vllm, xformers, vllm-nccl-cu12) installation;stale ### Your current environment ```text Python version: 3.12.3 PyTorch version: 2.3.1+cu121 ``` ### How you are installing vllm ``` pip install...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: x-x86_64-cpython-312/vllm/attention/ops copying vllm/attention/ops/triton_flash_attention.py -> build/lib.linux-x86_64-cpython-312/vllm/attention/ops copying vllm/attention/ops/paged_attn.py -> build/lib.linux-x86_64-cp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
