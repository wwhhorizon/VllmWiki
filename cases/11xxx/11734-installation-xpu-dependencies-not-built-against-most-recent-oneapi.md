# vllm-project/vllm#11734: [Installation]: XPU dependencies not built against most recent oneAPI

| 字段 | 值 |
| --- | --- |
| Issue | [#11734](https://github.com/vllm-project/vllm/issues/11734) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: XPU dependencies not built against most recent oneAPI

### Issue 正文摘录

### Your current environment The current prebuilt xpu dependencies are linked against OneAPI 2024 . The most recent version is 2025, which among other incompatible changes uses libsycl.so.8. Intel only allows paying customers to download older versions on OneAPI so using the one that is available and suggested by vllm docs (2024.2 or later) runs intro build errors. ```text from torch._C import * # noqa: F403 ImportError: libsycl.so.7: cannot open shared object file: No such file or directory ``` I am aware of the vllm docker image for xpu, this is about building from source. ### How you are installing vllm Building from source https://docs.vllm.ai/en/stable/getting_started/xpu-installation.html#build-xpu-backend-from-source ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: XPU dependencies not built against most recent oneAPI installation;stale ### Your current environment The current prebuilt xpu dependencies are linked against OneAPI 2024 . The most recent version is 2025
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: //docs.vllm.ai/en/stable/getting_started/xpu-installation.html#build-xpu-backend-from-source ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rce ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ion]: XPU dependencies not built against most recent oneAPI installation;stale ### Your current environment The current prebuilt xpu dependencies are linked against OneAPI 2024 . The most recent version is 2025, which a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
