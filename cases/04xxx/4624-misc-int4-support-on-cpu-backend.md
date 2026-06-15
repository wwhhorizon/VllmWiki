# vllm-project/vllm#4624: [Misc]: int4 support on CPU backend

| 字段 | 值 |
| --- | --- |
| Issue | [#4624](https://github.com/vllm-project/vllm/issues/4624) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: int4 support on CPU backend

### Issue 正文摘录

### Anything you want to discuss about vllm. I'm trying play with the new CPU backend, but met below issues: ``` WARNING 05-06 21:24:15 cpu_executor.py:113] float16 is not supported on CPU, casting to bfloat16. 2024-05-06 21:24:16 | ERROR | stderr | [rank0]: ValueError: torch.bfloat16 is not supported for quantization method gptq. Supported dtypes: [torch.float16] ``` It seems to me that current CPU backend only support float16 type model, and no int4 is supported? When could we have int4 model supported, do we have any roadmap?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Misc]: int4 support on CPU backend feature request;stale ### Anything you want to discuss about vllm. I'm trying play with the new CPU backend, but met below issues: ``` WARNING 05-06 21:24:15 cpu_executor.py:113] floa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: int4 support on CPU backend feature request;stale ### Anything you want to discuss about vllm. I'm trying play with the new CPU backend, but met below issues: ``` WARNING 05-06 21:24:15 cpu_executor.py:113] floa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Misc]: int4 support on CPU backend feature request;stale ### Anything you want to discuss about vllm. I'm trying play with the new CPU backend, but met below issues: ``` WARNING 05-06 21:24:15 cpu_executor.py:113] floa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ] ``` It seems to me that current CPU backend only support float16 type model, and no int4 is supported? When could we have int4 model supported, do we have any roadmap?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
