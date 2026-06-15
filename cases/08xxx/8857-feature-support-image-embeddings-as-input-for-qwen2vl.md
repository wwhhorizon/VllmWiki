# vllm-project/vllm#8857: [Feature]: Support image embeddings as input for qwen2vl

| 字段 | 值 |
| --- | --- |
| Issue | [#8857](https://github.com/vllm-project/vllm/issues/8857) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support image embeddings as input for qwen2vl

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Most multimodal models support input image embeddings. see previous pr: https://github.com/vllm-project/vllm/pull/6613 IMO there's no reason not to support qwen2vl. When I was about to add this feature to qwen2vl. Unfortunately, I've run into some difficulties. For example, I can't just rely on image embedding to generate new prompt_token_ids without the original image. See [here](https://github.com/vllm-project/vllm/blob/4bb98f2190aaf408cb063df5184829fb54ee5f81/vllm/model_executor/models/qwen2_vl.py#L788.) height, width = get_image_size(image, channel_dim=input_data_format) And [here](https://github.com/vllm-project/vllm/blob/4bb98f2190aaf408cb063df5184829fb54ee5f81/vllm/model_executor/models/qwen2_vl.py#L564C5-L564C33), if we just return image embeds, it will occur an error. AssertionError: mrope embedding type requires multi-modal input mapper returns 'image_grid_thw' or 'video_grid_thw'. Might we need to passthrough more parameters for qwen2vl? please me give some tips. here is my draft code: https://github.com/vllm-project/vllm/pull/8856 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support image embeddings as input for qwen2vl feature request ### 🚀 The feature, motivation and pitch Most multimodal models support input image embeddings. see previous pr: https://github.com/vllm-project/vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support image embeddings as input for qwen2vl feature request ### 🚀 The feature, motivation and pitch Most multimodal models support input image embeddings. see previous pr: https://github.com/vllm-project/vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
