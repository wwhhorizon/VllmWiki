# vllm-project/vllm#9068: [Bug]: Pixtral not working with vllm v0.6.2 docker

| 字段 | 值 |
| --- | --- |
| Issue | [#9068](https://github.com/vllm-project/vllm/issues/9068) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pixtral not working with vllm v0.6.2 docker

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Pixtral 12b does not work with the docker version of vllm v0.6.2 when using mistral tokenizer, it seems there is a missing OpenCV dependency : ImportError: OpenCV is required for this function. Install it with 'pip install mistral_common[opencv]' The model works fine with v0.6.1.post2 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Pixtral not working with vllm v0.6.2 docker bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Pixtral 12b does not work with the docker version of vllm v0.6.2 when using...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: st2 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: working with vllm v0.6.2 docker bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Pixtral 12b does not work with the docker version of vllm v0.6.2 when using mistral tokenizer,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
