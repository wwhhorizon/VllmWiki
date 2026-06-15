# vllm-project/vllm#17415: [Usage]: How to use LLM.classify(...) through OpenAI endpoint?

| 字段 | 值 |
| --- | --- |
| Issue | [#17415](https://github.com/vllm-project/vllm/issues/17415) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use LLM.classify(...) through OpenAI endpoint?

### Issue 正文摘录

### Your current environment vLLM 0.8.5 ### How would you like to use vllm I need to run a classification model, extract probs and serve it through OpenAI API. I know that it is possible to do offline: ```python from vllm import LLM llm = LLM(model="jason9693/Qwen2.5-1.5B-apeach", task="classify") (output,) = llm.classify("Hello, my name is") probs = output.outputs.probs print(f"Class Probabilities: {probs!r} (size={len(probs)})") ``` My task is very similar to a reranker (score) task but with multiple classes (query + document). How do you do you this using OpenAI? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .8.5 ### How would you like to use vllm I need to run a classification model, extract probs and serve it through OpenAI API. I know that it is possible to do offline: ```python from vllm import LLM llm = LLM(model="jaso...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: penAI API. I know that it is possible to do offline: ```python from vllm import LLM llm = LLM(model="jason9693/Qwen2.5-1.5B-apeach", task="classify") (output,) = llm.classify("Hello, my name is") probs = output.outputs....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: AI? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
