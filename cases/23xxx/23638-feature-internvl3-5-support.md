# vllm-project/vllm#23638: [Feature]: InternVL3_5 Support

| 字段 | 值 |
| --- | --- |
| Issue | [#23638](https://github.com/vllm-project/vllm/issues/23638) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: InternVL3_5 Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch requesting support for [InternVL3_5](https://huggingface.co/OpenGVLab/InternVL3_5-241B-A28B) and its model family. they support video, images and text. currently when i try to serve using vllm serve it does not allow videos. ``` raise self._make_status_error_from_response(err.response) from None openai.BadRequestError: Error code: 400 - {'error': {'message': 'At most 0 video(s) may be provided in one prompt. None', 'type': 'BadRequestError', 'param': None, 'code': 400}} ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: InternVL3_5 Support feature request ### 🚀 The feature, motivation and pitch requesting support for [InternVL3_5](https://huggingface.co/OpenGVLab/InternVL3_5-241B-A28B) and its model family. they support vide...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: InternVL3_5 Support feature request ### 🚀 The feature, motivation and pitch requesting support for [InternVL3_5](https://huggingface.co/OpenGVLab/InternVL3_5-241B-A28B) and its model family. they support vide...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
