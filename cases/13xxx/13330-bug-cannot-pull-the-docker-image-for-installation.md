# vllm-project/vllm#13330: [Bug]: Cannot pull the docker image for installation

| 字段 | 值 |
| --- | --- |
| Issue | [#13330](https://github.com/vllm-project/vllm/issues/13330) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Cannot pull the docker image for installation

### Issue 正文摘录

Hi, I am a beginner in using vllm and I'm trying to use docker following the [instruction `docker build -f Dockerfile . --target vllm-openai --tag vllm/vllm-openai`](https://docs.vllm.ai/en/latest/deployment/docker.html#deployment-docker-build-image-from-source). However, I cannot pull the docker image here for installation. What should I do if I want to install it from source.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Cannot pull the docker image for installation bug;stale Hi, I am a beginner in using vllm and I'm trying to use docker following the [instruction `docker build -f Dockerfile . --target vllm-openai --tag vllm/vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Cannot pull the docker image for installation bug;stale Hi, I am a beginner in using vllm and I'm trying to use docker following the [instruction `docker build -f Dockerfile . --target vllm-openai --tag vllm/vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: --target vllm-openai --tag vllm/vllm-openai`](https://docs.vllm.ai/en/latest/deployment/docker.html#deployment-docker-build-image-from-source). However, I cannot pull the docker image here for installation. What should...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
