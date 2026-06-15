# vllm-project/vllm#15214: [Misc][Help]: Adding support for a Custom model with External MoE Routing

| 字段 | 值 |
| --- | --- |
| Issue | [#15214](https://github.com/vllm-project/vllm/issues/15214) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc][Help]: Adding support for a Custom model with External MoE Routing

### Issue 正文摘录

### Anything you want to discuss about vllm. I have a custom model that uses something really similar to MoE but instead of that routing being determined by the model itself, I set routing dependent on what part of the sequence the tokens are from. I would now like to inference my model using VLLM, and because I have a non-standard model I assume I will need to modify some parts of VLLM to get it to work. It would be really nice if someone more familiar with the project can give me some feedback on my implementation thoughts and maybe can point me to the right places in the code base. - I really would like to have batching support where each batch item can have a different routing map. - I will most likely need a custom sampler, which is capable of determining the routing pattern / setting the next expert, based on the sequence. - I assume that I would need to CUDA graph cache each routing pattern / combination, which sounds like a lot. How is this handled with other MoE models? Most likely I want to at first deactivate this. Thank you for all your help in advance and with best regards XMaster96 ### Before submitting a new issue... - [x] Make sure you already searched for relevant...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Misc][Help]: Adding support for a Custom model with External MoE Routing stale ### Anything you want to discuss about vllm. I have a custom model that uses something really similar to MoE but instead of that routing be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the next expert, based on the sequence. - I assume that I would need to CUDA graph cache each routing pattern / combination, which sounds like a lot. How is this handled with other MoE models? Most likely I want to at f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Misc][Help]: Adding support for a Custom model with External MoE Routing stale ### Anything you want to discuss about vllm. I have a custom model that uses something really similar to MoE but instead of that routing be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Misc][Help]: Adding support for a Custom model with External MoE Routing stale ### Anything you want to discuss about vllm. I have a custom model that uses something really similar to MoE but instead of that routing be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Misc][Help]: Adding support for a Custom model with External MoE Routing stale ### Anything you want to discuss about vllm. I have a custom model that uses something really similar to MoE but instead of that routing bei...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
