# vllm-project/vllm#3546: [New Model]: CohereForCausalLM Support request 

| 字段 | 值 |
| --- | --- |
| Issue | [#3546](https://github.com/vllm-project/vllm/issues/3546) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: CohereForCausalLM Support request 

### Issue 正文摘录

### The model to consider. ValueError: Model architectures ['CohereForCausalLM'] are not supported for now ![1711001492046](https://github.com/vllm-project/vllm/assets/7098003/c9f431ec-bb69-4903-9bdd-0073fef03ade) ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Support request new-model ### The model to consider. ValueError: Model architectures ['CohereForCausalLM'] are not supported for now ![1711001492046](https://github.com/vllm-project/vllm/assets/7098003/c9f431ec-bb69-490...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: CohereForCausalLM Support request new-model ### The model to consider. ValueError: Model architectures ['CohereForCausalLM'] are not supported for now ![1711001492046](https://github.com/vllm-project/vllm/a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: CohereForCausalLM Support request new-model ### The model to consider. ValueError: Model architectures ['CohereForCausalLM'] are not supported for now ![1711001492046](https://github.com/vllm-project/vllm/a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
