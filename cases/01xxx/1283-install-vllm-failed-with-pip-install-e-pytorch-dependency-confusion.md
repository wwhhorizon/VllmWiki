# vllm-project/vllm#1283: Install vLLM failed with `pip install -e .`, PyTorch dependency confusion?

| 字段 | 值 |
| --- | --- |
| Issue | [#1283](https://github.com/vllm-project/vllm/issues/1283) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash;import_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Install vLLM failed with `pip install -e .`, PyTorch dependency confusion?

### Issue 正文摘录

Hi guys, I install vllm failed with `pip install -e .` The error messages shows below: ``` (vllm) dell@dell:~/workSpace/vllm$ pip install -e . Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple Obtaining file:///home/dell/workSpace/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [28 lines of output] /tmp/pip-build-env-6fb626c8/overlay/lib/python3.10/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), /tmp/pip-build-env-6fb626c8/overlay/lib/python3.10/site-packages/torch/cuda/__init__.py:138: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11080). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively...

## 现有链接修复摘要

#1290 lock torch version to 2.0.1 when build for #1283

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: Install vLLM failed with `pip install -e .`, PyTorch dependency confusion? Hi guys, I install vllm failed with `pip install -e .` The error messages shows below: ``` (vllm) dell@dell:~/workSpace/vllm$ pip install -e . L
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /tmp/pip-build-env-6fb626c8/overlay/lib/python3.10/site-packages/torch/cuda/__init__.py:138: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11080). Please update your GPU dr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: and/editable_wheel.py", line 345, in _create_wheel_file files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp) File "/tmp/pip-build-env-id48fazi/overlay/lib/python3.10/site-packages/setuptools/command/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n _check_cuda_version raise RuntimeError(CUDA_MISMATCH_MESSAGE.format(cuda_str_version, torch.version.cuda)) RuntimeError: The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1)....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: kSpace/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1290](https://github.com/vllm-project/vllm/pull/1290) | mentioned | 0.6 | lock torch version to 2.0.1 when build for #1283 | 1.0 was compiled with CUDA 12.1, which not compatible with vllm。issue #1283 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
