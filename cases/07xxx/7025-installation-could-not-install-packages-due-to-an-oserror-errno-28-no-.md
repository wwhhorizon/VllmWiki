# vllm-project/vllm#7025: [Installation]: Could not install packages due to an OSError: [Errno 28] No space left on device but disk still have space

| 字段 | 值 |
| --- | --- |
| Issue | [#7025](https://github.com/vllm-project/vllm/issues/7025) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Could not install packages due to an OSError: [Errno 28] No space left on device but disk still have space

### Issue 正文摘录

### Your current environment ![image](https://github.com/user-attachments/assets/b25198d8-8530-49a1-b116-9882b5fb5977) i install vllm in /mnt , i found is still have space but it has a wrong like: Installing build dependencies ... error error: subprocess-exited-with-error × pip subprocess to install build dependencies did not run successfully. │ exit code: 1 ╰─> [47 lines of output] Looking in indexes: http://mirrors.cloud.aliyuncs.com/pypi/simple/ Collecting cmake>=3.21 Using cached http://mirrors.cloud.aliyuncs.com/pypi/packages/78/5e/c274ffd124b8d4d95734af94c1080f0421c89dabdea2475651a7bd1e02ca/cmake-3.30.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (26.9 MB) Collecting ninja Using cached http://mirrors.cloud.aliyuncs.com/pypi/packages/6d/92/8d7aebd4430ab5ff65df2bfee6d5745f95c004284db2d8ca76dcbfd9de47/ninja-1.11.1.1-py2.py3-none-manylinux1_x86_64.manylinux_2_5_x86_64.whl (307 kB) Collecting packaging Using cached http://mirrors.cloud.aliyuncs.com/pypi/packages/08/aa/cc0199a5f0ad350994d660967a8efb233fe0416e4639146c089643407ce6/packaging-24.1-py3-none-any.whl (53 kB) Collecting setuptools>=49.4.0 Using cached http://mirrors.cloud.aliyuncs.com/pypi/packages/e1/58/e0ef3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: Could not install packages due to an OSError: [Errno 28] No space left on device but disk still have space installation;stale ### Your current environment ![image](https://github.com/user-attachments/asse
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: irrors.cloud.aliyuncs.com/pypi/packages/5e/44/73bea497ac69bafde2ee4269292fa3b41f1198f4bb7bbaaabde30ad29d4a/fsspec-2024.6.1-py3-none-any.whl (177 kB) Collecting nvidia-cuda-nvrtc-cu12==12.1.105 (from torch==2.3.0) Using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d29d4a/fsspec-2024.6.1-py3-none-any.whl (177 kB) Collecting nvidia-cuda-nvrtc-cu12==12.1.105 (from torch==2.3.0) Using cached http://mirrors.cloud.aliyuncs.com/pypi/packages/b6/9f/c64c03f49d6fbc56196664d05dba14e3a561038...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Errno 28] No space left on device but disk still have space installation;stale ### Your current environment ![image](https://github.com/user-attachments/assets/b25198d8-8530-49a1-b116-9882b5fb5977) i install vllm in /mn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
