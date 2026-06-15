# vllm-project/vllm#6573: [Feature]: Support Lora Adapter generated from mistral-finetune

| 字段 | 值 |
| --- | --- |
| Issue | [#6573](https://github.com/vllm-project/vllm/issues/6573) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Lora Adapter generated from mistral-finetune

### Issue 正文摘录

Recent mistral models inlcuding mistral 7b v0.3 instruct have consolidated.safetensors which have different weights key names compared to what vllm expects. Also there are keys like layernorm and postattention_layernorm that vllm finds difficult to deal with. Are you able to implement an update where a user who has generated a lora safetensors file from mistral-finetune can simply load this directly as a lora adapter into vllm and it just works instead of having to first try to map the weights to another weights key name convention as well as figuring out how to deal with unfamiliar keys such as layernorm and postattention_layernorm.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support Lora Adapter generated from mistral-finetune feature request;stale Recent mistral models inlcuding mistral 7b v0.3 instruct have consolidated.safetensors which have different weights key names compare...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ter generated from mistral-finetune feature request;stale Recent mistral models inlcuding mistral 7b v0.3 instruct have consolidated.safetensors which have different weights key names compared to what vllm expects. Also...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
