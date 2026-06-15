# vllm-project/vllm#3276: install from source failed using the latest code

| 字段 | 值 |
| --- | --- |
| Issue | [#3276](https://github.com/vllm-project/vllm/issues/3276) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> install from source failed using the latest code

### Issue 正文摘录

``` Looking in indexes: https://pypi.org/simple, https://pypi.ngc.nvidia.com Obtaining file:///data/weilong.yu/github/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [23 lines of output] /tmp/pip-build-env-30uui0su/overlay/local/lib/python3.10/dist-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered i nternally at ../torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), :220: UserWarning: Unsupported CUDA architectures ({'5.2', '7.2', '8.7', '6.0', '6.1'}) are excluded from the `TORCH_CUDA_ARCH_LIST` env variable (5.2 6.0 6.1 7.0 7.2 7.5 8.0 8 .6 8.7 9.0+PTX). Supported CUDA architectures are: {'8.6', '9.0', '8.0+PTX', '8.9+PTX', '8.0', '8.9', '8.6+PTX', '7.5+PTX', '7.0+PTX', '7.5', '9.0+PTX', '7.0'}. /usr/bin/python: No module named pip Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-package...

## 现有链接修复摘要

#43147 [ROCm] Fuse Q pre-quant onto AITER static per-tensor FP8 path

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: install from source failed using the latest code ``` Looking in indexes: https://pypi.org/simple, https://pypi.ngc.nvidia.com
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: device()), # torch.device('cpu'), :220: UserWarning: Unsupported CUDA architectures ({'5.2', '7.2', '8.7', '6.0', '6.1'}) are excluded from the `TORCH_CUDA_ARCH_LIST` env variable (5.2 6.0 6.1 7.0 7.2 7.5 8.0 8 .6 8.7 9...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: github/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ;ci_build cuda build_error;crash env_dependency #43147 [ROCm] Fuse Q pre-quant onto AITER static per-tensor FP8 path ```
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 132, in get_requires_for_build_editable return hook(config_settings) File "/tmp/pip-build-env-30uui0su/overlay/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 448, in get_requires_for_build...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43147](https://github.com/vllm-project/vllm/pull/43147) | mentioned | 0.6 | [ROCm] Fuse Q pre-quant onto AITER static per-tensor FP8 path | onto AITER static per-tensor FP8 path > **Dependency:** ⚠️ Requires [ROCm/aiter#3276](https://github.com/ROCm/aiter/pull/3276) to be merged first — it adds the `static_per_tensor_… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
