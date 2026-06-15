# vllm-project/vllm#4490: [Usage]: Do I need to specify chat-template for Qwen model?  

| 字段 | 值 |
| --- | --- |
| Issue | [#4490](https://github.com/vllm-project/vllm/issues/4490) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Do I need to specify chat-template for Qwen model?  

### Issue 正文摘录

### Your current environment Hi, I did a full SFT on Qwen 0.5 B model using LLama-Factory, during which I specified the template parameter. I'm a little confused on whether I should to use a template for the qwen model ? I searched on line but found it not mentioned a lot on under which circumstance should I use the "chat-template" parameter ? Can anyone give me some suggestion ? thank you.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Do I need to specify chat-template for Qwen model? usage;stale ### Your current environment Hi, I did a full SFT on Qwen 0.5 B model using LLama-Factory, during which I specified the template parameter. I'm a l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: Do I need to specify chat-template for Qwen model? usage;stale ### Your current environment Hi, I did a full SFT on Qwen 0.5 B model using LLama-Factory, during which I specified the template parameter. I'm a l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: confused on whether I should to use a template for the qwen model ? I searched on line but found it not mentioned a lot on under which circumstance should I use the "chat-template" parameter ? Can anyone give me some su...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Do I need to specify chat-template for Qwen model? usage;stale ### Your current environment Hi, I did a full SFT on Qwen 0.5 B model using LLama-Factory, during which I specified the template parameter. I'm a l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
