# vllm-project/vllm#297: Installing with some issues

| 字段 | 值 |
| --- | --- |
| Issue | [#297](https://github.com/vllm-project/vllm/issues/297) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Installing with some issues

### Issue 正文摘录

Hello someone know how this error caused? ``` Obtaining file:///home/lclcq/infer_workspace/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [18 lines of output] Traceback (most recent call last): File "/home/lclcq/miniconda3/envs/new_env2/lib/python3.8/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in main() File "/home/lclcq/miniconda3/envs/new_env2/lib/python3.8/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main json_out['return_val'] = hook(**hook_input['kwargs']) File "/home/lclcq/miniconda3/envs/new_env2/lib/python3.8/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 132, in get_requires_for_build_editable return hook(config_settings) File "/tmp/pip-build-env-g_a1aa9s/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 450, in get_requires_for_build_editable return self.get_requires_for_build_wheel(config_settings) File "/tmp/pip-build-env-g_a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Installing with some issues installation Hello someone know how this error caused? ``` Obtaining file:///home/lclcq/infer_workspace/vllm Installing build dependencies ... done Checking if build backend supports buil
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: kspace/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ) File " ", line 59, in File " ", line 34, in get_nvcc_cuda_version TypeError: unsupported operand type(s) for +: 'NoneType' and 'str' [end of output] note: This error originates from a subprocess, and is likely not a p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 132, in get_requires_for_build_editable return hook(config_settings) File "/tmp/pip-build-env-g_a1aa9s/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 450, in get_requires_for_build_editab...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
