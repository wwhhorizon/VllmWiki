# vllm-project/vllm#5209: [Feature]: Support for Mirostat, Dynamic Temperature, and Quadratic Sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#5209](https://github.com/vllm-project/vllm/issues/5209) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Mirostat, Dynamic Temperature, and Quadratic Sampling

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Would it be possible to add support for: 1. **Mirostat**: Adaptive sampling to maintain a target perplexity, ensuring consistent generation quality by adapting sampling strategies in real-time. 2. **Dynamic Temperature**: Adjusting temperature dynamically based on certain criteria, allowing the model to adjust its creativity and coherence dynamically, based on the context or user input. 3. **Quadratic Sampling**: An alternative sampling method to improve diversity and quality of the outputs, providing more nuanced and diverse text generation, improving overall user experience. These features would enhance the model’s flexibility and output quality, making it more versatile and effective for a wider range of applications. If these aren’t supported yet, is it possible to include them in the upcoming roadmap? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: at, Dynamic Temperature, and Quadratic Sampling good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Would it be possible to add support for: 1. **Mirostat**: Adaptive sampling to maintain a ta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: djusting temperature dynamically based on certain criteria, allowing the model to adjust its creativity and coherence dynamically, based on the context or user input. 3. **Quadratic Sampling**: An alternative sampling m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
