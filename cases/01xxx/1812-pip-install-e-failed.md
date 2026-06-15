# vllm-project/vllm#1812: pip install -e . failed

| 字段 | 值 |
| --- | --- |
| Issue | [#1812](https://github.com/vllm-project/vllm/issues/1812) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> pip install -e . failed

### Issue 正文摘录

Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [28 lines of output] /tmp/pip-build-env-dhfydmaz/overlay/lib/python3.10/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), /tmp/pip-build-env-dhfydmaz/overlay/lib/python3.10/site-packages/torch/cuda/__init__.py:138: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11080). Please update your GPU driver by downloading and installing a new version from the URL: http://www.nvidia.com/Download/index.aspx Alternatively, go to: https://pytorch.org to install a PyTorch version that has been compiled with your version of the CUDA driver. (Triggered internally at ../c10/cuda/CUDAFunctions.cpp:108.) return torch._C._cuda_getDeviceCount() > 0 No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' Traceback (most recent call last): File "/miniconda3/envs/vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: pip install -e . failed Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [28 lines of output]
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /tmp/pip-build-env-dhfydmaz/overlay/lib/python3.10/site-packages/torch/cuda/__init__.py:138: UserWarning: CUDA initialization: The NVIDIA driver on your system is too old (found version 11080). Please update your GPU dr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: y. │ exit code: 1 ╰─> [28 lines of output] /tmp/pip-build-env-dhfydmaz/overlay/lib/python3.10/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
