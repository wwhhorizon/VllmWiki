# vllm-project/vllm#19007: [Feature]: Individual GuidedDecodingParams for each prompt in prompts.

| 字段 | 值 |
| --- | --- |
| Issue | [#19007](https://github.com/vllm-project/vllm/issues/19007) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Individual GuidedDecodingParams for each prompt in prompts.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I don't know if this is technically possible, but I would like to individually set the GuidedDecodingParams for each prompt that is in my list of prompts. My use case: Aspect-based sentiment analysis: ``` According to the following sentiment elements definition: - The 'aspect term' is the exact word or phrase in the text that represents a specific feature, attribute, or aspect of a product or service that a user may express an opinion about, the aspect term might be 'NULL' for implicit aspect. - The 'aspect category' refers to the category that aspect belongs to, and the available categories includes: 'ambience general', 'drinks prices', 'drinks quality', 'drinks style_options', 'food prices', 'food quality', 'food style_options', 'location general', 'restaurant general', 'restaurant miscellaneous', 'restaurant prices', 'service general'. - The 'sentiment polarity' refers to the degree of positivity, negativity or neutrality expressed in the opinion towards a particular aspect or feature of a product or service, and the available polarities include: 'positive', 'negative' and 'neutral'. Recognize all sentiment elements with their correspondi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re]: Individual GuidedDecodingParams for each prompt in prompts. feature request;stale ### 🚀 The feature, motivation and pitch I don't know if this is technically possible, but I would like to individually set the Guide...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: spect term' is the exact word or phrase in the text that represents a specific feature, attribute, or aspect of a product or service that a user may express an opinion about, the aspect term might be 'NULL' for implicit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: aspect categories and sentiment polarity in the following text with the format of [('aspect term', 'aspect category', 'sentiment polarity'), ...]. Text: We took advanatage of the half price sushi deal on saturday so it...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
