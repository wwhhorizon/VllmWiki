# vllm-project/vllm#19534: [Usage]: Error when building the XPU image using Dockerfile

| 字段 | 值 |
| --- | --- |
| Issue | [#19534](https://github.com/vllm-project/vllm/issues/19534) |
| 状态 | closed |
| 标签 | usage;intel-gpu;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Error when building the XPU image using Dockerfile

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ``` docker build -f Dockerfile.xpu -t vllm-xpu-env --shm-size=4g . docker run -it \ --rm \ --network=host \ --device /dev/xpu0 \ -v /dev:/dev \ vllm-xpu-env ``` but error when using xpu-smi ``` /usr/local/lib/python3.10/dist-packages/torch/xpu/__init__.py:60: UserWarning: XPU device count is zero! (Triggered internally at /pytorch/c10/xpu/XPUFunctions.cpp:60.) return torch._C._xpu_getDeviceCount() ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: Error when building the XPU image using Dockerfile usage;intel-gpu;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ``` docker build -f Doc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -v /dev:/dev \ vllm-xpu-env ``` but error when using xpu-smi ``` /usr/local/lib/python3.10/dist-packages/torch/xpu/__init__.py:60: UserWarning: XPU device count is zero! (Triggered internally at /pytorch/c10/xpu/XPUFunc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: age]: Error when building the XPU image using Dockerfile usage;intel-gpu;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ``` docker build -f Docker...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
