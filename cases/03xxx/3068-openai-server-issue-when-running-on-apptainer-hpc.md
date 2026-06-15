# vllm-project/vllm#3068: OpenAI Server issue when running on Apptainer (HPC)

| 字段 | 值 |
| --- | --- |
| Issue | [#3068](https://github.com/vllm-project/vllm/issues/3068) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> OpenAI Server issue when running on Apptainer (HPC)

### Issue 正文摘录

Hi I'm trying to run the openai compatible server on an HPC cluster (that has apptainer instead of docker). I converted the docker image to an apptainer `.sif` file. However when I try to run the `.sif` file, I'm faced with this issue ```sh /usr/bin/python3: Error while finding module specification for 'vllm.entrypoints.openai.api_server' (ModuleNotFoundError: No module named 'vllm') ``` I assume it's because vllm isn't installed in the container/image's python environment (which it should be if it's equivalent to the an image built with DockerFile). New to the apptainer environment and would appreciate any help in getting this up in HPC clusters!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: penai compatible server on an HPC cluster (that has apptainer instead of docker). I converted the docker image to an apptainer `.sif` file. However when I try to run the `.sif` file, I'm faced with this issue ```sh /usr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: OpenAI Server issue when running on Apptainer (HPC) stale Hi I'm trying to run the openai compatible server on an HPC cluster (that has apptainer instead of docker). I converted the docker image to an apptainer `.sif` f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
