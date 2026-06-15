# vllm-project/vllm#8851: [Installation]: Cannot install with Poetry

| 字段 | 值 |
| --- | --- |
| Issue | [#8851](https://github.com/vllm-project/vllm/issues/8851) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Cannot install with Poetry

### Issue 正文摘录

### Your current environment 5.47 /tmp/tmp4enbmtnv/.venv/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:258: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:84.) 45.47 cpu = _conversion_method_template(device=torch.device("cpu")) 45.47 Traceback (most recent call last): 45.47 File "/usr/local/lib/python3.12/site-packages/pyproject_hooks/_in_process/_in_process.py", line 373, in 45.47 main() 45.47 File "/usr/local/lib/python3.12/site-packages/pyproject_hooks/_in_process/_in_process.py", line 357, in main 45.47 json_out["return_val"] = hook(**hook_input["kwargs"]) 45.47 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 45.47 File "/usr/local/lib/python3.12/site-packages/pyproject_hooks/_in_process/_in_process.py", line 134, in get_requires_for_build_wheel 45.47 return hook(config_settings) 45.47 ^^^^^^^^^^^^^^^^^^^^^ 45.47 File "/tmp/tmp4enbmtnv/.venv/lib/python3.12/site-packages/setuptools/build_meta.py", line 332, in get_requires_for_build_wheel 45.47 return self._get_build_requires(config_settings, requirements=[]) 45.47 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 45.47 File "/tmp/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: Cannot install with Poetry installation;stale ### Your current environment 5.47 /tmp/tmp4enbmtnv/.venv/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:258: UserWarning: Failed to ini
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: in get_requirements 45.47 ValueError: Unsupported platform, please use CUDA, ROCm, Neuron, OpenVINO, or CPU. 45.47 45.47 45.47 at /usr/local/lib/python3.12/site-packages/poetry/installation/chef.py:164 in _prepare 45.48...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: = None) -> Path: 45.48 45.48 Note: This error originates from the build backend, and is likely not a problem with poetry but with vllm (0.6.2) not supporting PEP 517 builds. You can verify this by running 'pip wheel --n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s.py", line 134, in get_requires_for_build_wheel 45.47 return hook(config_settings) 45.47 ^^^^^^^^^^^^^^^^^^^^^ 45.47 File "/tmp/tmp4enbmtnv/.venv/lib/python3.12/site-packages/setuptools/build_meta.py", line 332, in get...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Cannot install with Poetry installation;stale ### Your current environment 5.47 /tmp/tmp4enbmtnv/.venv/lib/python3.12/site-packages/torch/_subclasses/functional_tensor.py:258: UserWarning: Failed to init...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
