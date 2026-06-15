# vllm-project/vllm#24876: [Bug]:  uv pip install vllm==0.10.2 --extra-index-url https://wheels.vllm.ai/0.10.2/ --torch-backend=auto  not work

| 字段 | 值 |
| --- | --- |
| Issue | [#24876](https://github.com/vllm-project/vllm/issues/24876) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  uv pip install vllm==0.10.2 --extra-index-url https://wheels.vllm.ai/0.10.2/ --torch-backend=auto  not work

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using an arm server with multi Nvidia GPUs as I follow the 0.10.2's release instructions to install vllm, I found that https://wheels.vllm.ai/0.10.2/vllm-0.10.2-cp38-abi3-manylinux2014_aarch64.whl not exist (vllm) root@aic30:/workspace/vllm# uv pip install vllm==0.10.2 --extra-index-url https://wheels.vllm.ai/0.10.2/ --torch-backend=auto ⠇ vllm==0.10.2 error: Failed to fetch: `https://wheels.vllm.ai/0.10.2/vllm-0.10.2-cp38-abi3-manylinux2014_aarch64.whl` Caused by: HTTP status client error (404 Not Found) for url (https://wheels.vllm.ai/0.10.2/vllm-0.10.2-cp38-abi3-manylinux2014_aarch64.whl) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: uv pip install vllm==0.10.2 --extra-index-url https://wheels.vllm.ai/0.10.2/ --torch-backend=auto not work bug;stale ### Your current environment ### 🐛 Describe the bug I am using an arm server with multi Nvidia...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ll vllm==0.10.2 --extra-index-url https://wheels.vllm.ai/0.10.2/ --torch-backend=auto not work bug;stale ### Your current environment ### 🐛 Describe the bug I am using an arm server with multi Nvidia GPUs as I follow th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: that https://wheels.vllm.ai/0.10.2/vllm-0.10.2-cp38-abi3-manylinux2014_aarch64.whl not exist (vllm) root@aic30:/workspace/vllm# uv pip install vllm==0.10.2 --extra-index-url https://wheels.vllm.ai/0.10.2/ --torch-backen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ex-url https://wheels.vllm.ai/0.10.2/ --torch-backend=auto not work bug;stale ### Your current environment ### 🐛 Describe the bug I am using an arm server with multi Nvidia GPUs as I follow the 0.10.2's release instruct...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
