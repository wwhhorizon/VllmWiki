# vllm-project/vllm#7194: [Bug]: Incomplete tool calling response for pipeline-parallel vllm with ray

| 字段 | 值 |
| --- | --- |
| Issue | [#7194](https://github.com/vllm-project/vllm/issues/7194) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incomplete tool calling response for pipeline-parallel vllm with ray

### Issue 正文摘录

### Your current environment vllm v0.5.4 Setup A) single docker container with vllm, no pipeline-parallelism ``` docker run ... vllm/vllm-openai:v0.5.4 --model "meta-llama/Meta-Llama-3.1-70B-Instruct" --tensor-parallel-size 2 --max-model-len=4096 ``` Setup B) two docker containers with ray + vllm (pipeline parallelism) ``` docker run -it ... --network host --entrypoint /bin/bash vllm/vllm-openai:v0.5.4 # start ray head node in one of the docker containers ray start --head --disable-usage-stats # start ray worker node in the other docker container ray start --address=' :6379' # start vllm in head node container vllm serve "meta-llama/Meta-Llama-3.1-70B-Instruct" --tensor-parallel-size 1 --pipeline-parallel-size 2 --distributed-executor-backend ray --max-model-len=4096 ``` The issue does not depend on the model; e.g. it also appears with `meta-llama/Meta-Llama-3-70B-Instruct` instead of Llama-3.1 ### 🐛 Describe the bug Without pipeline-parallelism, a request with tool calling is responded correctly with a valid tool call. With pipeline-parallelism, the same request is responded with incomplete tool call (just a few tokens long, but still status 200). Example request: ``` { "model":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lm, no pipeline-parallelism ``` docker run ... vllm/vllm-openai:v0.5.4 --model "meta-llama/Meta-Llama-3.1-70B-Instruct" --tensor-parallel-size 2 --max-model-len=4096 ``` Setup B) two docker containers with ray + vllm (p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ay bug;stale ### Your current environment vllm v0.5.4 Setup A) single docker container with vllm, no pipeline-parallelism ``` docker run ... vllm/vllm-openai:v0.5.4 --model "meta-llama/Meta-Llama-3.1-70B-Instruct" --ten...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Incomplete tool calling response for pipeline-parallel vllm with ray bug;stale ### Your current environment vllm v0.5.4 Setup A) single docker container with vllm, no pipeline-parallelism ``` docker run ... vllm/vllm-op...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tensor-parallel-size 1 --pipeline-parallel-size 2 --distributed-executor-backend ray --max-model-len=4096 ``` The issue does not depend on the model; e.g. it also appears with `meta-llama/Meta-Llama-3-70B-Instruct` inst...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0.5.4 Setup A) single docker container with vllm, no pipeline-parallelism ``` docker run ... vllm/vllm-openai:v0.5.4 --model "meta-llama/Meta-Llama-3.1-70B-Instruct" --tensor-parallel-size 2 --max-model-len=4096 ``` Set...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
