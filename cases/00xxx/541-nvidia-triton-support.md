# vllm-project/vllm#541: NVIDIA Triton support

| 字段 | 值 |
| --- | --- |
| Issue | [#541](https://github.com/vllm-project/vllm/issues/541) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | triton |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> NVIDIA Triton support

### Issue 正文摘录

Hi vLLM genius @zhuohan123 @WoosukKwon We noticed the plan to support Triton server in the [vLLM roadmap](https://github.com/vllm-project/vllm/issues/244). I collaborate with @defined1007. We have also made some attempts on our own. Here, we share our choices and practices in the hope of jointly pushing forward the construction. ### Background and Objectives Our intention is to utilize the Triton server internally to facilitate model management and its integration with our internal services. ### Current Situation On the RPC level, Triton server supports asynchronous operations, yet, at the instance execution level, operations are executed synchronously. It's static batching. Consequently, with only a single instance, our operations become a multi-producer single-consumer (MPSC). Our aspiration, however, is to enable a multi-producer multi-consumer (MPMC). ### Strategy #### Strategy One: Triton Server + Python Backend This approach employs multi-processing for handling multiple instances but lacks memory sharing. - We are unable to initiate a sufficient number of instances, resulting in a low throughput. - On enabling max_batch_size, although the throughput can match that of the AP...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: NVIDIA Triton support feature request Hi vLLM genius @zhuohan123 @WoosukKwon We noticed the plan to support Triton server in the [vLLM roadmap](https://github.com/vllm-project/vllm/issues/244). I collaborate with @defin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: bjectives Our intention is to utilize the Triton server internally to facilitate model management and its integration with our internal services. ### Current Situation On the RPC level, Triton server supports asynchrono...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: unable to initiate a sufficient number of instances, resulting in a low throughput. - On enabling max_batch_size, although the throughput can match that of the API server, the latency is high, failing to meet our requir...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Our intention is to utilize the Triton server internally to facilitate model management and its integration with our internal services. ### Current Situation On the RPC level, Triton server supports asynchronous operati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: NVIDIA Triton support feature request Hi vLLM genius @zhuohan123 @WoosukKwon We noticed the plan to support Triton server in the [vLLM roadmap](https://github.com/vllm-project/vllm/issues/244). I collaborate with @defin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
