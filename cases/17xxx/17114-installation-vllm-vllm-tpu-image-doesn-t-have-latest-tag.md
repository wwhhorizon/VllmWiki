# vllm-project/vllm#17114: [Installation]: vllm/vllm-tpu image doesn't have :latest tag

| 字段 | 值 |
| --- | --- |
| Issue | [#17114](https://github.com/vllm-project/vllm/issues/17114) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: vllm/vllm-tpu image doesn't have :latest tag

### Issue 正文摘录

### Your current environment Environment is not relevant. ### How you are installing vllm When following the [documentation](https://docs.vllm.ai/en/latest/getting_started/installation/ai_accelerator.html) I want to use the `vllm/vllm-tpu` docker image. To do that, I think there should be the `:latest` tag defined for it... ```sh docker pull vllm/vllm-tpu:latest # Error response from daemon: manifest for vllm/vllm-tpu:latest not found: manifest unknown: manifest unknown ``` So I can't really follow the instruction from documentation that says: > See [Use vLLM’s Official Docker Image](https://docs.vllm.ai/en/latest/deployment/docker.html#deployment-docker-pre-built-image) for instructions on using the official Docker image, making sure to substitute the image name vllm/vllm-openai with vllm/vllm-tpu. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: vllm/vllm-tpu image doesn't have :latest tag installation;stale ### Your current environment Environment is not relevant. ### How you are installing vllm When following the [documentation](https://docs.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pu. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Installation]: vllm/vllm-tpu image doesn't have :latest tag installation;stale ### Your current environment Environment is not relevant. ### How you are installing vllm When following the [documentation](https://docs.vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Installation]: vllm/vllm-tpu image doesn't have :latest tag installation;stale ### Your current environment Environment is not relevant. ### How you are installing vllm When following the [documentation](https://docs.v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
