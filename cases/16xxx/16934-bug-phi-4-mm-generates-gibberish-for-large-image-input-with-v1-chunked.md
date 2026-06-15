# vllm-project/vllm#16934: [Bug]: Phi-4-MM generates gibberish for large image input with v1 chunked prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#16934](https://github.com/vllm-project/vllm/issues/16934) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Phi-4-MM generates gibberish for large image input with v1 chunked prefill

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The reproduction code should generate below outputs, image1 with `size=(14*448, 448)` can generate reasonable outputs, while image2 with `size=(15*448, 448)` generates gibberish: ```text -------------------------------------------------- The image shows a view of a tower with a blue sky in the background. The tower is partially obscured by pink cherry blossoms in the foreground. -------------------------------------------------- wide...exwide< -------------------------------------------------- ``` However, if we increase `max_num_batched_tokens` from 2048 to 4139 (image2's num_image_tokens), all outputs are reasonable: ```text -------------------------------------------------- The image shows a view of a tower with a blue sky in the background. The tower is partially obscured by pink cherry blossoms in the foreground. -------------------------------------------------- The image shows a view of a tall tower with a spherical structure at the top, partially obscured by pink cherry blossom branches. The sky is clear and blue -------------------------------------------------- ``` Therefore, I suspect something goes wrong in v1's chunk...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: Phi-4-MM generates gibberish for large image input with v1 chunked prefill bug;stale ### Your current environment ### 🐛 Describe the bug The reproduction code should generate below outputs, image1 with `size=(14*4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rtain large enough image input. I didn't observe similar issues on other VLMs. cc @WoosukKwon @ywang96 Do you have any insights about this issue? ### Before submitting a new issue... - [x] Make sure you already searched...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
