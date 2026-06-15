# vllm-project/vllm#556: intall vllm failed

| 字段 | 值 |
| --- | --- |
| Issue | [#556](https://github.com/vllm-project/vllm/issues/556) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
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

> intall vllm failed

### Issue 正文摘录

using conda install vllm pip install vllm Collecting vllm Using cached vllm-0.1.2.tar.gz (93 kB) Installing build dependencies ... done Getting requirements to build wheel ... error error: subprocess-exited-with-error × Getting requirements to build wheel did not run successfully. │ exit code: 1 ╰─> [15 lines of output] Traceback (most recent call last): File "/home/fzq/anaconda3/envs/zhixi/lib/python3.9/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in main() File "/home/fzq/anaconda3/envs/zhixi/lib/python3.9/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main json_out['return_val'] = hook(**hook_input['kwargs']) File "/home/fzq/anaconda3/envs/zhixi/lib/python3.9/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "/tmp/pip-build-env-0mlfx90i/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 341, in get_requires_for_build_wheel return self._get_build_requires(config_settings, requirements=['wheel']) File "/tmp/pip-build-env-0mlfx90i/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: intall vllm failed using conda install vllm pip install vllm Collecting vllm Using cached vllm-0.1.2.tar.gz (93 kB) Installing build dependencies ... done Getting requirements to build wheel ... error error: subprocess-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: exec(code, locals()) File " ", line 60, in RuntimeError: CUDA 11.0 or higher is required to build the package. [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. error:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ess.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "/tmp/pip-build-env-0mlfx90i/overlay/lib/python3.9/site-packages/setuptools/build_meta.py", line 341, in get_requires_for_build_wheel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
