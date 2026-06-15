# vllm-project/vllm#18386: [Usage]: How to get the logits from classification models.

| 字段 | 值 |
| --- | --- |
| Issue | [#18386](https://github.com/vllm-project/vllm/issues/18386) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to get the logits from classification models.

### Issue 正文摘录

### Your current environment pip install vllm ### How would you like to use vllm Hi! When I use vllm for classification, I find that the returned output is something like: ClassificationOutput(num_classes=5), which only contains the probabilities. Now, I want to directly get the logits (i.e. vectors before softmax). I think it sounds easy, but I cannot find a good way. Anyone can help me? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: gits from classification models. usage ### Your current environment pip install vllm ### How would you like to use vllm Hi! When I use vllm for classification, I find that the returned output is something like: Classifi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How to get the logits from classification models. usage ### Your current environment pip install vllm ### How would you like to use vllm Hi! When I use vllm for classification, I find that the returned output i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
