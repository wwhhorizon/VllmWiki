# vllm-project/vllm#43269: [Feature]: Support multi-image and interleaved multimodal custom datasets in bench serve

| 字段 | 值 |
| --- | --- |
| Issue | [#43269](https://github.com/vllm-project/vllm/issues/43269) |
| 状态 | closed |
| 标签 | feature request;multi-modality |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support multi-image and interleaved multimodal custom datasets in bench serve

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are using `vllm bench serve` to test our online multimodal services. For image-based multimodal models, the current custom image dataset support has two limitations: 1. If a custom sample contains multiple images in `image_files`, only the first image is used and the remaining images are discarded. 2. The request format does not support arbitrary interleaving of text and images, such as `text -> image -> text -> image -> text`. This makes it difficult to reproduce realistic production traffic, where requests may include multiple images, image comparison, document/page sequences, or instructions placed between images. It would be useful if `vllm bench serve` could support a custom chat-style multimodal dataset format, where each JSONL row can provide OpenAI-compatible content parts directly, for example: ```json { "content": [ {"type": "text", "text": "Please inspect this image."}, {"type": "image_url", "image_url": {"url": "file:///path/to/a.jpg"}}, {"type": "text", "text": "Now compare it with this one."}, {"type": "image_url", "image_url": {"url": "file:///path/to/b.jpg"}} ], "output_tokens": 128 } ``` I would like to know whether the c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support multi-image and interleaved multimodal custom datasets in bench serve feature request;multi-modality ### 🚀 The feature, motivation and pitch We are using `vllm bench serve` to test our online multimod...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: as `text -> image -> text -> image -> text`. This makes it difficult to reproduce realistic production traffic, where requests may include multiple images, image comparison, document/page sequences, or instructions plac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -image and interleaved multimodal custom datasets in bench serve feature request;multi-modality ### 🚀 The feature, motivation and pitch We are using `vllm bench serve` to test our online multimodal services. For image-b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 🚀 The feature, motivation and pitch We are using `vllm bench serve` to test our online multimodal services. For image-based multimodal models, the current custom image dataset support has two limitations: 1. If a custom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
