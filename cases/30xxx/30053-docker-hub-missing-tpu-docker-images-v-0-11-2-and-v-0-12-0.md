# vllm-project/vllm#30053: [Docker Hub]: missing TPU docker images v.0.11.2 and v.0.12.0

| 字段 | 值 |
| --- | --- |
| Issue | [#30053](https://github.com/vllm-project/vllm/issues/30053) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Docker Hub]: missing TPU docker images v.0.11.2 and v.0.12.0

### Issue 正文摘录

### Your current environment Hello there, The TPU images on Docker Hub have no updated TAG release. The latest tag available is [v0.11.1](https://hub.docker.com/layers/vllm/vllm-tpu/v0.11.1), while there were no major bug-fixes for TPUs on [v0.11.2](https://hub.docker.com/layers/vllm/vllm-tpu/v0.11.2) that tag was never released on Docker Hub. The same goes for the recently released [v0.12.0](https://hub.docker.com/layers/vllm/vllm-tpu/v0.12.0) so I'm suspecting something in the image building and publishing process is not working anymore .. ### How you are installing vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Docker Hub]: missing TPU docker images v.0.11.2 and v.0.12.0 installation;stale ### Your current environment Hello there, The TPU images on Docker Hub have no updated TAG release. The latest tag available is [v0.11.1](
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ocker Hub]: missing TPU docker images v.0.11.2 and v.0.12.0 installation;stale ### Your current environment Hello there, The TPU images on Docker Hub have no updated TAG release. The latest tag available is [v0.11.1](ht...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: there, The TPU images on Docker Hub have no updated TAG release. The latest tag available is [v0.11.1](https://hub.docker.com/layers/vllm/vllm-tpu/v0.11.1), while there were no major bug-fixes for TPUs on [v0.11.2](http...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
