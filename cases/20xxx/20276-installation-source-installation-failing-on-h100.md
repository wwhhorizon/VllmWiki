# vllm-project/vllm#20276: [Installation]: Source installation failing on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#20276](https://github.com/vllm-project/vllm/issues/20276) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;moe;quantization;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Source installation failing on H100

### Issue 正文摘录

### Your current environment ```text P5.48x i.e. using H100 ``` Also tried ``` export MAX_JOBS=1 ``` Error: ```sh Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB) Building wheels for collected packages: vllm Building editable for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building editable for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─ creating /tmp/pip-wheel-0kkaw4t3/.tmp-i6ch0xse/vllm.egg-info writing /tmp/pip-wheel-0kkaw4t3/.tmp-i6ch0xse/vllm.egg-info/PKG-INFO writing dependency_links to /tmp/pip-wheel-0kkaw4t3/.tmp-i6ch0xse/vllm.egg-info/dependency_links.txt writing entry points to /tmp/pip-wheel-0kkaw4t3/.tmp-i6ch0xse/vllm.egg-info/entry_points.txt writing requirements to /tmp/pip-wheel-0kkaw4t3/.tmp-i6ch0xse/vllm.egg-info/requires.txt writing top-level names to /tmp/pip-wheel-0kkaw4t3/.tmp-i6ch0xse/vllm.egg-info/top_level.txt writing manifest file '/tmp/pip-wheel-0kkaw4t3/.tmp-i6ch0xse/vllm.egg-info/SOURCES.txt' package init file 'vllm/vllm_flash_attn/__init__.py' not found (or not a regular file) package init file 'vllm/attention/utils/__init__.py' not found (or not a regular file) package init file 'vllm/model_ex...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: Source installation failing on H100 installation;stale ### Your current environment ```text P5.48x i.e. using H100 ``` Also tried ``` export MAX_JOBS=1 ``` Error: ```sh Downloading shellingham-1.5.4-
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: not a regular file) package init file 'vllm/model_executor/layers/quantization/utils/configs/__init__.py' not found (or not a regular file) ERROR setuptools_scm._file_finders.git listing git files failed - pretending th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: Source installation failing on H100 installation;stale ### Your current environment ```text P5.48x i.e. using H100 ``` Also tried ``` export MAX_JOBS=1 ``` Error: ```sh Downloading shellingham-1.5.4-py2....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: bling cumem allocator extension. -- CMake Version: 3.27.6 -- CUTLASS 3.9.2 -- Found CUDAToolkit: /usr/local/cuda/include (found version "12.2.140") -- CUDART: /usr/local/cuda/lib64/libcudart.so -- CUDA Driver: /usr/loca...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: fer_schema.h:42:7: note: ‘std::integral_constant ::value’ evaluates to false In file included from /usr/local/lib/python3.10/dist-packages/torch/include/ATen/core/boxing/KernelFunction_impl.h:2, from /usr/local/lib/pyth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
