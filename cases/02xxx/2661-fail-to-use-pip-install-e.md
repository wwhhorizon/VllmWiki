# vllm-project/vllm#2661: Fail to use ``pip install -e .''

| 字段 | 值 |
| --- | --- |
| Issue | [#2661](https://github.com/vllm-project/vllm/issues/2661) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Fail to use ``pip install -e .''

### Issue 正文摘录

Here are the errors. I also installed numpy, but still failed. CUDA==12.2 ``` Collecting git+https://github.com/vllm-project/vllm Cloning https://github.com/vllm-project/vllm to /tmp/pip-req-build-yuxv0lpu Running command git clone --filter=blob:none --quiet https://github.com/vllm-project/vllm /tmp/pip-req-build-yuxv0lpu Resolved https://github.com/vllm-project/vllm to commit ab406446691f289ef51d1abd8d1ff66760eda36f Installing build dependencies ... done Getting requirements to build wheel ... error error: subprocess-exited-with-error × Getting requirements to build wheel did not run successfully. │ exit code: 1 ╰─> [21 lines of output] /tmp/pip-build-env-ehqfzo6d/overlay/lib/python3.10/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), Traceback (most recent call last): File "/home/ec2-user/SageMaker/conda/deekseek/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in main() File "/home/ec2-user/SageMaker/conda/deek...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Fail to use ``pip install -e .'' Here are the errors. I also installed numpy, but still failed. CUDA==12.2 ``` Collecting git+https://github.com/vllm-project/vllm
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ll -e .'' Here are the errors. I also installed numpy, but still failed. CUDA==12.2 ``` Collecting git+https://github.com/vllm-project/vllm Cloning https://github.com/vllm-project/vllm to /tm
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ess.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "/tmp/pip-build-env-ehqfzo6d/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 325, in get_requires_for_build_wheel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
