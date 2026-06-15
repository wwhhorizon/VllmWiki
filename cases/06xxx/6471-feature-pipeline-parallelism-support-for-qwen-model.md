# vllm-project/vllm#6471: [Feature]: Pipeline parallelism support for qwen model

| 字段 | 值 |
| --- | --- |
| Issue | [#6471](https://github.com/vllm-project/vllm/issues/6471) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Pipeline parallelism support for qwen model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Pipeline parallelism is only supported for the following architectures: ['AquilaModel', 'AquilaForCausalLM', 'InternLMForCausalLM', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'Phi3ForCausalLM', 'GPT2LMHeadModel']. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Pipeline parallelism support for qwen model feature request ### 🚀 The feature, motivation and pitch Pipeline parallelism is only supported for the following architectures: ['AquilaModel', 'AquilaForCausalLM',...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Pipeline parallelism support for qwen model feature request ### 🚀 The feature, motivation and pitch Pipeline parallelism is only supported for the following architectures: ['AquilaModel', 'AquilaForCausalLM',...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Pipeline parallelism support for qwen model feature request ### 🚀 The feature, motivation and pitch Pipeline parallelism is only supported for the following architectures: ['AquilaModel', 'AquilaForCausalLM',...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
