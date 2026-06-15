# vllm-project/vllm#11591: [Installation]: official docker image missing for version v0.6.6.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#11591](https://github.com/vllm-project/vllm/issues/11591) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: official docker image missing for version v0.6.6.post1

### Issue 正文摘录

### Your current environment Docker image is missing in official docker repo for version v0.6.6.post1. [https://hub.docker.com/r/vllm/vllm-openai/tags](https://hub.docker.com/r/vllm/vllm-openai/tags) ### How you are installing vllm ```sh docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:v0.6.6.post1 \ --model mistralai/Mistral-7B-v0.1 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: official docker image missing for version v0.6.6.post1 installation;stale ### Your current environment Docker image is missing in official docker repo for version v0.6.6.post1. [https://hub.docker.com/r/
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing vllm ```sh docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN= " \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:v0.6.6.post1 \ --model mistralai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: on]: official docker image missing for version v0.6.6.post1 installation;stale ### Your current environment Docker image is missing in official docker repo for version v0.6.6.post1. [https://hub.docker.com/r/vllm/vllm-o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
