# vllm-project/vllm#3002: some error happend when installing vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#3002](https://github.com/vllm-project/vllm/issues/3002) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> some error happend when installing vllm

### Issue 正文摘录

Nvidia jetson is aarch64 , in ubuntu20.04 server(cuda 12.2), when run "pip install vllm " , some error happened : × Getting requirements to build wheel did not run successfully. │ exit code: 1 ╰─> [19 lines of output] /tmp/pip-build-env-jkd2f4g4/overlay/lib/python3.10/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda' Traceback (most recent call last): File "/root/miniconda3/envs/python310/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in main() File "/root/miniconda3/envs/python310/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main json_out['return_val'] = hook(**hook_input['kwargs']) File "/root/miniconda3/envs/python310/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "/tmp/pip-build...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: some error happend when installing vllm stale Nvidia jetson is aarch64 , in ubuntu20.04 server(cuda 12.2), when run "pip install vllm " , some error happened : × Getting requirements to build wheel did not run successfu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: some error happend when installing vllm stale Nvidia jetson is aarch64 , in ubuntu20.04 server(cuda 12.2), when run "pip install vllm " , some error happened : × Getting requirements to build wheel did not run successfu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ess.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "/tmp/pip-build-env-jkd2f4g4/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 325, in get_requires_for_build_wheel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: some error happend when installing vllm stale Nvidia jetson is aarch64 , in ubuntu20.04 server(cuda 12.2), when run "pip install vllm " , some error happened : × Getting requirements to build wheel did not run successfu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
