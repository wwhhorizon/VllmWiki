# vllm-project/vllm#20574: [Installation]: which version of vllm that support torch2.2.2+cuda11.8+python 3.10

| 字段 | 值 |
| --- | --- |
| Issue | [#20574](https://github.com/vllm-project/vllm/issues/20574) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: which version of vllm that support torch2.2.2+cuda11.8+python 3.10

### Issue 正文摘录

### Your current environment I don't want to reinstall torch and cuda ```text The output of `python collect_env.py`: python collect_env.py /repo/MLLM/vllm/vllm/__init__.py:7: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from .version import __version__, __version_tuple__ # isort:skip Traceback (most recent call last): File "/repo/MLLM/vllm/collect_env.py", line 19, in from vllm.envs import environment_variables File "/repo/MLLM/vllm/vllm/__init__.py", line 14, in import vllm.env_override # noqa: F401 File "/repo/MLLM/vllm/vllm/env_override.py", line 41, in torch._inductor.config.compile_threads = 1 AttributeError: module 'torch._inductor' has no attribute 'config' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: which version of vllm that support torch2.2.2+cuda11.8+python 3.10 installation;stale ### Your current environment I don't want to reinstall torch and cuda ```text The output of `python collect_env.py`:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: which version of vllm that support torch2.2.2+cuda11.8+python 3.10 installation;stale ### Your current environment I don't want to reinstall torch and cuda ```text The output of `python collect_env.py`:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /repo/MLLM/vllm/vllm/env_override.py", line 41, in torch._inductor.config.compile_threads = 1 AttributeError: module 'torch._inductor' has no attribute 'config' ``` ### Before submitting a new issue... - [x] Make sure y...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ersion of vllm that support torch2.2.2+cuda11.8+python 3.10 installation;stale ### Your current environment I don't want to reinstall torch and cuda ```text The output of `python collect_env.py`: python collect_env.py /...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development cuda crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
