# vllm-project/vllm#15395: [Feature]: Add Warning for Chat Template Mismatches similar to SGLang

| 字段 | 值 |
| --- | --- |
| Issue | [#15395](https://github.com/vllm-project/vllm/issues/15395) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Warning for Chat Template Mismatches similar to SGLang

### Issue 正文摘录

I'm requesting a feature to add warnings when users supply a chat template that differs from the official template for a particular model. Currently, vLLM simply acknowledges the supplied template without alerting users to potential performance issues. **Current Behavior:** When using a wrong chat template with vLLM, it only logs: ``` Using supplied chat template: {% for message in messages %}{% if message.role == 'user' %}{{ message.content }}{% endif %}{% endfor %} ``` **Requested Behavior:** While SGLang provides this helpful warning: ``` Using a chat_template: 'None', which is different from official chat template: 'llama-3-instruct', This discrepancy may lead to performance degradation. ``` I think that would improve the user experience by making potential issues more visible before they cause problems in production. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Add Warning for Chat Template Mismatches similar to SGLang good first issue;feature request I'm requesting a feature to add warnings when users supply a chat template that differs from the official template f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a chat template that differs from the official template for a particular model. Currently, vLLM simply acknowledges the supplied template without alerting users to potential performance issues. **Current Behavior:** Whe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Feature]: Add Warning for Chat Template Mismatches similar to SGLang good first issue;feature request I'm requesting a feature to add warnings when users supply a chat template that differs from the official template f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: add warnings when users supply a chat template that differs from the official template for a particular model. Currently, vLLM simply acknowledges the supplied template without alerting users to potential performance is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: for Chat Template Mismatches similar to SGLang good first issue;feature request I'm requesting a feature to add warnings when users supply a chat template that differs from the official template for a particular model....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
