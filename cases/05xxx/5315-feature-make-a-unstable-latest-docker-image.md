# vllm-project/vllm#5315: [Feature]: Make a unstable latest docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#5315](https://github.com/vllm-project/vllm/issues/5315) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make a unstable latest docker image

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm trying to test Lora with quantization using BnB and I'm using Docker to run vLLM. However, I can't find a docker image, on docker hub, with a tag that matches the 'latest' version. The latest tag of the docker images correspond til the stable version - not latest. So have you considered makes a tag for the 'latest' (unstable) version for Docker? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Make a unstable latest docker image feature request;stale ### 🚀 The feature, motivation and pitch I'm trying to test Lora with quantization using BnB and I'm using Docker to run vLLM. However, I can't find a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Make a unstable latest docker image feature request;stale ### 🚀 The feature, motivation and pitch I'm trying to test Lora with quantization using BnB and I'm using Docker to run vLLM. However, I can't find a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: le ### 🚀 The feature, motivation and pitch I'm trying to test Lora with quantization using BnB and I'm using Docker to run vLLM. However, I can't find a docker image, on docker hub, with a tag that matches the 'latest'...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: Make a unstable latest docker image feature request;stale ### 🚀 The feature, motivation and pitch I'm trying to test Lora with quantization using BnB and I'm using Docker to run vLLM. However, I can't find a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
