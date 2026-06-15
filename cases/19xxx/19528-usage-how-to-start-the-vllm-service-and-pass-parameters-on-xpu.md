# vllm-project/vllm#19528: [Usage]: How to start the vllm service and pass parameters on XPU

| 字段 | 值 |
| --- | --- |
| Issue | [#19528](https://github.com/vllm-project/vllm/issues/19528) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;kernel;operator;triton |
| 症状 | build_error;import_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to start the vllm service and pass parameters on XPU

### Issue 正文摘录

### Your current environment ``` python3 collect_env.py [W612 03:45:31.112336867 OperatorEntry.cpp:154] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a previously registered kernel for the same operator and the same dispatch key operator: aten::_validate_compressed_sparse_indices(bool is_crow, Tensor compressed_idx, Tensor plain_idx, int cdim, int dim, int nnz) -> () registered at /pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: XPU previous kernel: registered at /pytorch/build/aten/src/ATen/RegisterCPU.cpp:30477 new kernel: registered at /build/intel-pytorch-extension/build/Release/csrc/gpu/csrc/aten/generated/ATen/RegisterXPU.cpp:468 (function operator()) /usr/local/lib/python3.10/dist-packages/intel_extension_for_pytorch/nn/utils/_weight_prepack.py:6: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools () registered at /pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: XPU previous kernel: registered at /pytorch/build...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: plain_idx, int cdim, int dim, int nnz) -> () registered at /pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: XPU previous kernel: registered at /pytorch/build/aten/src/ATen/RegisterCPU.cpp:30477 new kernel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: import pkg_resources PyTorch version: 2.6.0+xpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: oduleNotFoundError("No module named 'vllm._C'") Collecting environment information... /usr/local/lib/python3.10/dist-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: bv1 xsaves clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip overflow_recov succor smca sme sev sev_es Virtua...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: riding a previously registered kernel for the same operator and the same dispatch key operator: aten::_validate_compressed_sparse_indices(bool is_crow, Tensor compressed_idx, Tensor plain_idx, int cdim, int dim, int nnz...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
