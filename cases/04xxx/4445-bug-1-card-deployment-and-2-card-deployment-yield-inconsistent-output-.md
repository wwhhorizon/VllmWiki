# vllm-project/vllm#4445: [Bug]: 1-card deployment and 2-card deployment yield inconsistent output logits.

| 字段 | 值 |
| --- | --- |
| Issue | [#4445](https://github.com/vllm-project/vllm/issues/4445) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 1-card deployment and 2-card deployment yield inconsistent output logits.

### Issue 正文摘录

### Your current environment version: v0.4.1 device: A800*2 model: qwen-14b-chat ### 🐛 Describe the bug I added a print statement in the following code. ```python # vllm.model_executor.layers.sampler.py # line 53-58 assert logits is not None _, vocab_size = logits.shape print(torch.mean(logits).cpu()) # I added my code here # Apply min_tokens penalty which sets stop tokens to -inf if min_tokens # have not been generated yet logits = _apply_min_tokens_penalty(logits, sampling_metadata) ``` Even when using the same decoding parameters, the output logits still changes when I increase the tensor-parallel-size from 1 to 2.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: . bug;stale ### Your current environment version: v0.4.1 device: A800*2 model: qwen-14b-chat ### 🐛 Describe the bug I added a print statement in the following code. ```python # vllm.model_executor.layers.sampler.py # li...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ield inconsistent output logits. bug;stale ### Your current environment version: v0.4.1 device: A800*2 model: qwen-14b-chat ### 🐛 Describe the bug I added a print statement in the following code. ```python # vllm.model_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: t been generated yet logits = _apply_min_tokens_penalty(logits, sampling_metadata) ``` Even when using the same decoding parameters, the output logits still changes when I increase the tensor-parallel-size from 1 to 2.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d deployment and 2-card deployment yield inconsistent output logits. bug;stale ### Your current environment version: v0.4.1 device: A800*2 model: qwen-14b-chat ### 🐛 Describe the bug I added a print statement in the fol...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
