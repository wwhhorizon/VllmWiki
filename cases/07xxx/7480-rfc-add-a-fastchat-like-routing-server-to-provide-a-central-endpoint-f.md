# vllm-project/vllm#7480: [RFC]: Add a FastChat like routing server to provide a central endpoint for multiple models

| 字段 | 值 |
| --- | --- |
| Issue | [#7480](https://github.com/vllm-project/vllm/issues/7480) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add a FastChat like routing server to provide a central endpoint for multiple models

### Issue 正文摘录

### Motivation. FastChat has a Controller -> multiple worker setup whereby individual worker nodes run a single model and report their model list to a master controller that handles routing. This allows some users to setup multiple models and connect them to a unified router server that receives incoming traffic and portions it out to the right worker. This would solve one of the [FAQ items](https://docs.vllm.ai/en/latest/serving/faq.html). ### Proposed Change. For the OpenAI compatible server: * Add a heartbeat registration step to the openai entrypoint that registers the server's model to a `routing` server. * Create a new `routing` server that acts as both controller and OpenAI shim. It receives the initial user requests and forwards the request to an actual vLLM server as a pass through. It also receives the registration calls from actual vLLM servers to populate the list of supported models. ### Feedback Period. one week ### CC List. _No response_ ### Any Other Things. _No response_

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [RFC]: Add a FastChat like routing server to provide a central endpoint for multiple models RFC ### Motivation. FastChat has a Controller -> multiple worker setup whereby individual worker nodes run a single model and r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [RFC]: Add a FastChat like routing server to provide a central endpoint for multiple models RFC ### Motivation. FastChat has a Controller -> multiple worker setup whereby individual worker nodes run a single model and r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: FastChat like routing server to provide a central endpoint for multiple models RFC ### Motivation. FastChat has a Controller -> multiple worker setup whereby individual worker nodes run a single model and report their m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t acts as both controller and OpenAI shim. It receives the initial user requests and forwards the request to an actual vLLM server as a pass through. It also receives the registration calls from actual vLLM servers to p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: er. This would solve one of the [FAQ items](https://docs.vllm.ai/en/latest/serving/faq.html). ### Proposed Change. For the OpenAI compatible server: * Add a heartbeat registration step to the openai entrypoint that regi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
