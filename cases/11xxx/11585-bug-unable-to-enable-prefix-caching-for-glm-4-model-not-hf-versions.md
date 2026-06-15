# vllm-project/vllm#11585: [Bug]: Unable to enable prefix caching for glm-4 model (not -hf versions)

| 字段 | 值 |
| --- | --- |
| Issue | [#11585](https://github.com/vllm-project/vllm/issues/11585) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unable to enable prefix caching for glm-4 model (not -hf versions)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug With glm-4 model, prefix caching is automatically disabled, because the engine is treating it as MLLM. Maybe related to following codes: https://github.com/vllm-project/vllm/blob/d427e5cfda8d2536b81e6021128e71b2dbc281aa/vllm/model_executor/models/chatglm.py#L758-L782 https://github.com/vllm-project/vllm/blob/d427e5cfda8d2536b81e6021128e71b2dbc281aa/vllm/engine/arg_utils.py#L1046-L1051 Unfortunately, the glm-4 and glm-4v models have the same `model_type` value, how can I override this behavior without changing the code? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unable to enable prefix caching for glm-4 model (not -hf versions) bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug With glm-4 model, prefix caching is automatically dis...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Unable to enable prefix caching for glm-4 model (not -hf versions) bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug With glm-4 model, prefix caching is automatically dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: de? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
