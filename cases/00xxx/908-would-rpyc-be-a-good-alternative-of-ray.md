# vllm-project/vllm#908: Would RPyC be a good alternative of Ray?

| 字段 | 值 |
| --- | --- |
| Issue | [#908](https://github.com/vllm-project/vllm/issues/908) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Would RPyC be a good alternative of Ray?

### Issue 正文摘录

Hi vLLM developers @WoosukKwon @zhuohan123 . I noticed that there is a plan to find alternative frameworks for distributed inference in the [RoadMap](https://github.com/vllm-project/vllm/issues/244). I think [RPyC](https://github.com/tomerfiliba-org/rpyc) maybe a good option for single machine scenario. RPyC is a concise RPC framework with basically no extra dependencies and its APIs are quite handy. RPyC is adopted by [lightllm](https://github.com/ModelTC/lightllm), a project parallel with vLLM, as its distributed backend and [this](https://github.com/ModelTC/lightllm/blob/main/lightllm/server/router/model_infer/model_rpc.py) is how it uses RPyC. As mentioned in some issues, Ray will bring heavy overhead for single machine serving. RPyC maybe a lightweight alternative to it. If you are interested, I think I can help to add RPyC support, create a new PR and implement it.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .com/ModelTC/lightllm), a project parallel with vLLM, as its distributed backend and [this](https://github.com/ModelTC/lightllm/blob/main/lightllm/server/router/model_infer/model_rpc.py) is how it uses RPyC. As mentione...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -org/rpyc) maybe a good option for single machine scenario. RPyC is a concise RPC framework with basically no extra dependencies and its APIs are quite handy. RPyC is adopted by [lightllm](https://github.com/ModelTC/lig...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s APIs are quite handy. RPyC is adopted by [lightllm](https://github.com/ModelTC/lightllm), a project parallel with vLLM, as its distributed backend and [this](https://github.com/ModelTC/lightllm/blob/main/lightllm/serv...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: and [this](https://github.com/ModelTC/lightllm/blob/main/lightllm/server/router/model_infer/model_rpc.py) is how it uses RPyC. As mentioned in some issues, Ray will bring heavy overhead for single machine serving. RPyC...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
