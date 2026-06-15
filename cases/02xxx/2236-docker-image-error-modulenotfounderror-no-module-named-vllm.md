# vllm-project/vllm#2236: docker image error ModuleNotFoundError: No module named 'vllm'

| 字段 | 值 |
| --- | --- |
| Issue | [#2236](https://github.com/vllm-project/vllm/issues/2236) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> docker image error ModuleNotFoundError: No module named 'vllm'

### Issue 正文摘录

using this procedure https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html I was deploying on runpod this image: vllm/vllm-openai:latest https://hub.docker.com/r/vllm/vllm-openai/tags then I get an error ``` 2023-12-21T15:25:16.536115444Z /usr/bin/python3: Error while finding module specification for 'vllm.entrypoints.openai.api_server' (ModuleNotFoundError: No module named 'vllm') ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: docker image error ModuleNotFoundError: No module named 'vllm' using this procedure https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html I was deploying on runpod this image: vllm/vllm-openai:latest https:/
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: r: No module named 'vllm' using this procedure https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html I was deploying on runpod this image: vllm/vllm-openai:latest https://hub.docker.com/r/vllm/vllm-openai/ta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
