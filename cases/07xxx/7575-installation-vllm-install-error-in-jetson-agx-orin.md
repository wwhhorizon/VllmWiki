# vllm-project/vllm#7575: [Installation]: vllm install error in jetson agx orin

| 字段 | 值 |
| --- | --- |
| Issue | [#7575](https://github.com/vllm-project/vllm/issues/7575) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: vllm install error in jetson agx orin

### Issue 正文摘录

### Your current environment OS: Ubuntu 22.04 jammy Kernel: aarch64 Linux 5.15.136-tegra Uptime: 1d 23h 22m Shell: bash 5.1.16 Disk: 137G / 1.8T (8%) CPU: ARM Cortex-A78AE @ 12x 2.2016GHz GPU: Orin (nvgpu) RAM: 3162MiB / 62841MiB Nova Config: nova-devkit Nova Version: 1.3.0 Jetpack: 6.0+b106 torch: 2.3.0(use pytorch aarch64 wheels) ### How you are installing vllm I want to install vllm in Jetson AGX Orin. I use the script "pip install vllm" and try to install from source "pip install -e .", but both these method return failture. ############################# error info ################################ Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple/ Collecting vllm Using cached https://pypi.tuna.tsinghua.edu.cn/packages/1c/e2/b437c1d5a39814acfc706e714eceee7fe80455a9666a13b7582205b30345/vllm-0.5.4.tar.gz (958 kB) Installing build dependencies ... done Getting requirements to build wheel ... error error: subprocess-exited-with-error × Getting requirements to build wheel did not run successfully. │ exit code: 1 ╰─> [21 lines of output] /tmp/pip-build-env-94kz6585/overlay/lib/python3.10/site-packages/torch/_subclasses/functional_tensor.py:258: UserWarning: Failed to initi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: vllm install error in jetson agx orin installation;stale ### Your current environment OS: Ubuntu 22.04 jammy Kernel: aarch64 Linux 5.15.136-tegra Uptime: 1d 23h 22m Shell: bash 5.1.16 Disk: 137G / 1.8T (
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ion;stale ### Your current environment OS: Ubuntu 22.04 jammy Kernel: aarch64 Linux 5.15.136-tegra Uptime: 1d 23h 22m Shell: bash 5.1.16 Disk: 137G / 1.8T (8%) CPU: ARM Cortex-A78AE @ 12x 2.2016GHz GPU: Orin (nvgpu) RAM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tex-A78AE @ 12x 2.2016GHz GPU: Orin (nvgpu) RAM: 3162MiB / 62841MiB Nova Config: nova-devkit Nova Version: 1.3.0 Jetpack: 6.0+b106 torch: 2.3.0(use pytorch aarch64 wheels) ### How you are installing vllm I want to insta...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: vllm install error in jetson agx orin installation;stale ### Your current environment OS: Ubuntu 22.04 jammy Kernel: aarch64 Linux 5.15.136-tegra Uptime: 1d 23h 22m Shell: bash 5.1.16 Disk: 137G / 1.8T (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
