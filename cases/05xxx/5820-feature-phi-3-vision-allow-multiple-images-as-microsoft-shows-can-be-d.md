# vllm-project/vllm#5820: [Feature]: Phi-3 vision -- allow multiple images as Microsoft shows can be done

| 字段 | 值 |
| --- | --- |
| Issue | [#5820](https://github.com/vllm-project/vllm/issues/5820) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Phi-3 vision -- allow multiple images as Microsoft shows can be done

### Issue 正文摘录

### 🚀 The feature, motivation and pitch i.e. instead of this: https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/serving_chat.py#L138-L140 allow multiple images. Idea is that many models trained for 1 image actually work well with multiple, and blocking usage inhibits exploration of what models are capable of. E.g. would be good for microsoft/Phi-3-vision-128k-instruct In HF transformers, Phi-3 handles multiple images just fine. I've used it just fine as well. It's also an officially supported task from Microsoft: https://github.com/microsoft/Phi-3CookBook/blob/main/md/03.Inference/Vision_Inference.md#3-comparison-of-multiple-images ### Alternatives None ### Additional context ``` openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': "Multiple 'image_url' input is currently not supported.", 'type': 'BadRequestError', 'param': None, 'code': 400} ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nai/serving_chat.py#L138-L140 allow multiple images. Idea is that many models trained for 1 image actually work well with multiple, and blocking usage inhibits exploration of what models are capable of. E.g. would be go...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ple images just fine. I've used it just fine as well. It's also an officially supported task from Microsoft: https://github.com/microsoft/Phi-3CookBook/blob/main/md/03.Inference/Vision_Inference.md#3-comparison-of-multi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: at many models trained for 1 image actually work well with multiple, and blocking usage inhibits exploration of what models are capable of. E.g. would be good for microsoft/Phi-3-vision-128k-instruct In HF transformers,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 3 vision -- allow multiple images as Microsoft shows can be done feature request ### 🚀 The feature, motivation and pitch i.e. instead of this: https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/servi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
