# vllm-project/vllm#463: PIP install error

| 字段 | 值 |
| --- | --- |
| Issue | [#463](https://github.com/vllm-project/vllm/issues/463) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> PIP install error

### Issue 正文摘录

I installed it on the docker image using the install method given in the documentation, but I get the following error. ``` docker run --gpus all -it --rm --shm-size=8g nvcr.io/nvidia/pytorch:22.12-py3 pip install vllm ``` At first I thought it was a PIP version issue, so I upgraded PIP and ran it again, but it was still there. Installing in the following way also fails. ``` git clone https://github.com/vllm-project/vllm.git cd vllm pip install -e ``` ``` root@:/workspace# pip install vllm Looking in indexes: https://pypi.org/simple, https://pypi.ngc.nvidia.com Collecting vllm Downloading vllm-0.1.2.tar.gz (93 kB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.8/93.8 kB 10.2 MB/s eta 0:00:00 Installing build dependencies ... done Getting requirements to build wheel ... error error: subprocess-exited-with-error × Getting requirements to build wheel did not run successfully. │ exit code: 1 ╰─> [15 lines of output] Traceback (most recent call last): File "/usr/local/lib/python3.8/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in main() File "/usr/local/lib/python3.8/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: PIP install error installation I installed it on the docker image using the install method given in the documentation, but I get the following error. ``` docker run --gpus all -it --rm --shm-size=8g nvcr.io/nvidia/pytor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: )) File " ", line 47, in RuntimeError: GPUs with compute capability less than 7.0 are not supported. [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. error: subprocess...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes fou
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ess.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "/tmp/pip-build-env-ha3un36c/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 341, in get_requires_for_build_wheel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
