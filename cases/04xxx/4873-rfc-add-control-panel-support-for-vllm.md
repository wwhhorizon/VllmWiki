# vllm-project/vllm#4873: [RFC]: Add control panel support for vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#4873](https://github.com/vllm-project/vllm/issues/4873) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add control panel support for vLLM

### Issue 正文摘录

### Motivation. The Fastchat-vLLM operational model offers significant advantages in deploying large language models (LLMs) for product services. [1](https://blog.vllm.ai/2023/06/20/vllm.html) The controller architecture in Fastchat is particularly beneficial for LLM deployment, owing to its loosely coupled design with the vLLM backend. This allows for: * Autoscaling: The vLLM backend can join and exit the cluster freely, enabling dynamic scaling capabilities. * Rolling Updates: The introduction of new models with distinct names allows the cluster to gradually update models, a process known as rolling updates. * Centralized Access: Users are relieved from the burden of tagging different URLs or IPs for various models; they simply send their requests to the controller, which then manages the rest, including dispatching requests to the appropriate backend based on the model name and ensuring effective load balancing. However, the challenge for Fastchat lies in managing multiple backends, including vLLM. This complexity appears to hinder its ability to keep pace with the rapid evolution of vLLM. It is disheartening to observe that Fastchat currently does not support the latest vLLM f...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: al for LLM deployment, owing to its loosely coupled design with the vLLM backend. This allows for: * Autoscaling: The vLLM backend can join and exit the cluster freely, enabling dynamic scaling capabilities. * Rolling U...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tagging different URLs or IPs for various models; they simply send their requests to the controller, which then manages the rest, including dispatching requests to the appropriate backend based on the model name and ens...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: llm.html) The controller architecture in Fastchat is particularly beneficial for LLM deployment, owing to its loosely coupled design with the vLLM backend. This allows for: * Autoscaling: The vLLM backend can join and e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: services. [1](https://blog.vllm.ai/2023/06/20/vllm.html) The controller architecture in Fastchat is particularly beneficial for LLM deployment, owing to its loosely coupled design with the vLLM backend. This allows for:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rt for vLLM RFC;keep-open ### Motivation. The Fastchat-vLLM operational model offers significant advantages in deploying large language models (LLMs) for product services. [1](https://blog.vllm.ai/2023/06/20/vllm.html)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
