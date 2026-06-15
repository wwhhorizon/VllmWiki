# vllm-project/vllm#10459: [Installation]: VLLM on ARM machine with GH200

| 字段 | 值 |
| --- | --- |
| Issue | [#10459](https://github.com/vllm-project/vllm/issues/10459) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |
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

> [Installation]: VLLM on ARM machine with GH200

### Issue 正文摘录

### Your current environment (I can not run collect_env since it requires VLLM installed) ```text $ pip freeze certifi==2022.12.7 charset-normalizer==2.1.1 filelock==3.16.1 fsspec==2024.10.0 idna==3.4 Jinja2==3.1.4 MarkupSafe==3.0.2 mpmath==1.3.0 networkx==3.4.2 numpy==2.1.3 pillow==10.2.0 pynvml==11.5.3 requests==2.28.1 sympy==1.13.1 torch==2.5.1 typing_extensions==4.12.2 urllib3==1.26.13 $ lsb_release -a No LSB modules are available. Distributor ID: Ubuntu Description: Ubuntu 22.04.4 LTS Release: 22.04 Codename: jammy ``` I have an ARM CPU and a NVIDIA GH200 Driver Version: 550.90.07 CUDA Version: 12.4. ### How you are installing vllm ```sh pip install torch numpy pip install vllm ``` I get this error: ```sh pip install vllm Collecting vllm Using cached vllm-0.6.4.post1.tar.gz (3.1 MB) Installing build dependencies ... done Getting requirements to build wheel ... error error: subprocess-exited-with-error × Getting requirements to build wheel did not run successfully. │ exit code: 1 ╰─> [18 lines of output] /tmp/pip-build-env-8t3z_6ag/overlay/lib/python3.10/site-packages/torch/_subclasses/functional_tensor.py:295: UserWarning: Failed to initialize NumPy: No module named 'numpy' (...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: VLLM on ARM machine with GH200 installation;stale ### Your current environment (I can not run collect_env since it requires VLLM installed) ```text $ pip freeze certifi==2022.12.7 charset-normalizer==2.1
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ammy ``` I have an ARM CPU and a NVIDIA GH200 Driver Version: 550.90.07 CUDA Version: 12.4. ### How you are installing vllm ```sh pip install torch numpy pip install vllm ``` I get this error: ```sh pip install vllm Col...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: VLLM on ARM machine with GH200 installation;stale ### Your current environment (I can not run collect_env since it requires VLLM installed) ```text $ pip freeze certifi==2022.12.7 charset-normalizer==2.1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: da available, but the error looks like VLLM might be trying to use a CPU backend. I tried manually installing pynvml, but it did not change anything. ### Before submitting a new issue... - [X] Make sure you already sear...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ess.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "/tmp/pip-build-env-8t3z_6ag/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 334, in get_requires_for_build_wheel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
