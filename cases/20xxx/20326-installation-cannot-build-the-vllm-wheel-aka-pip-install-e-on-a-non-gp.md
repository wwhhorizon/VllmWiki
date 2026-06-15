# vllm-project/vllm#20326: [Installation]: Cannot build the vLLM wheel (aka pip install -e .) on a non-GPU x86 Linux machine

| 字段 | 值 |
| --- | --- |
| Issue | [#20326](https://github.com/vllm-project/vllm/issues/20326) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Cannot build the vLLM wheel (aka pip install -e .) on a non-GPU x86 Linux machine

### Issue 正文摘录

### Your current environment I was able to `pip install -r requirement/cpu.txt` on an x86 Linux VM (launched using Canonical's "Multipass" on an i9 Mac 2019). According to the guideline, I then tun ``` $ VLLM_TARGET_DEVICE=cpu pip install -e . -v ``` Eventualy the following cmake command tries to run: ``` [ 'cmake', '/home/ubuntu/projects/remotes/chris-relational/vllm', '-G', 'Ninja', '-DCMAKE_BUILD_TYPE=RelWithDebInfo', '-DVLLM_TARGET_DEVICE=cpu', '-DVLLM_PYTHON_EXECUTABLE=/home/ubuntu/projects/remotes/chris-relational/vllm/.venv/bin/python3.12', '-DVLLM_PYTHON_PATH=/tmp/pip-build-env-khmpa04v/site:/usr/lib/python312.zip:/usr/lib/python3.12:/usr/lib/python3.12/lib-dynload:/tmp/pip-build-env-khmpa04v/overlay/lib/python3.12/ site-packages:/tmp/pip-build-env-khmpa04v/normal/lib/python3.12/site-packages:/tmp/pip-build-env-khmpa04v/overlay/lib/python3.12/site-packages/setuptools/_vendor', '-DFETCHCONTENT_BASE_DIR=/home/ubuntu/projects/remotes/chris-relational/vllm/.deps', '-DCMAKE_JOB_POOL_COMPILE:STRING=compile', '-DCMAKE_JOB_POOLS:STRING=compile=4' ] ``` I get however the following error: ``` CMake Error at /tmp/pip-build-env-jstth2gb/overlay/lib/python3.12/site-packages/torch/share...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Cannot build the vLLM wheel (aka pip install -e .) on a non-GPU x86 Linux machine installation;stale ### Your current environment I was able to `pip install -r requirement/cpu.txt` on an x86 Linux VM (lau
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: affe2Config.cmake:90 (message): Your installed Caffe2 version uses CUDA but I cannot find the CUDA libraries. Please set the proper CUDA prefixes and / or install CUDA. Call Stack (most recent call first): /tmp/pip-buil...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h2gb/overlay/lib/python3.12/site-packages/torch/share/cmake/Caffe2/Caffe2Config.cmake:90 (message): Your installed Caffe2 version uses CUDA but I cannot find the CUDA libraries. Please set the proper CUDA prefixes and /...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: wheel (aka pip install -e .) on a non-GPU x86 Linux machine installation;stale ### Your current environment I was able to `pip install -r requirement/cpu.txt` on an x86 Linux VM (launched using Canonical's "Multipass" o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
