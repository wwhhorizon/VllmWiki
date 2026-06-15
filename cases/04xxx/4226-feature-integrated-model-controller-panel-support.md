# vllm-project/vllm#4226: [Feature]: integrated model controller panel support?

| 字段 | 值 |
| --- | --- |
| Issue | [#4226](https://github.com/vllm-project/vllm/issues/4226) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: integrated model controller panel support?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the production scenario, multiple model registration is a needed feature, which could be served as auto scale or model update case or centralized service dispatch accessed from fixed URL. Previously, we use fastchat w/ vllm, and it works well to serve our purpose. But nowadays vllm get rapidly expansion in it LLM support feature like images/video, etc, and also engine args grows to support various need, fastchat‘s provided openai interface seems cannot keep up the pace with the changes of vllm side. So shall we consider to host some kind of function just like fastchat's controller feature, and model worker could be loosely-coupled with controller, and dynamic leave and register into controller's server backend, while controler could choose the best route for certain prompt request? ### Alternatives I'm not sure whether there is some other openai API server could does this controller/work loosely-coupled working mode well, and also could keep sync with vllm's quickly changing API. ### Additional context _No response_

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ould be served as auto scale or model update case or centralized service dispatch accessed from fixed URL. Previously, we use fastchat w/ vllm, and it works well to serve our purpose. But nowadays vllm get rapidly expan...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: integrated model controller panel support? feature request;unstale ### 🚀 The feature, motivation and pitch In the production scenario, multiple model registration is a needed feature, which could be served as...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: le model registration is a needed feature, which could be served as auto scale or model update case or centralized service dispatch accessed from fixed URL. Previously, we use fastchat w/ vllm, and it works well to serv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: integrated model controller panel support? feature request;unstale ### 🚀 The feature, motivation and pitch In the production scenario, multiple model registration is a needed feature, which could be served as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
