# vllm-project/vllm#17120: [Doc]: Documentation source code hyperlinks do not always point to the correct source code

| 字段 | 值 |
| --- | --- |
| Issue | [#17120](https://github.com/vllm-project/vllm/issues/17120) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Documentation source code hyperlinks do not always point to the correct source code

### Issue 正文摘录

### 📚 The doc issue For example, the documenation of the ``generate`` method in [LLM Class](https://docs.vllm.ai/en/latest/api/offline_inference/llm.html#vllm.LLM.generate). Clicking its ``source`` button, we find that it points to [an unrelated function in utils](https://github.com/vllm-project/vllm/blob/main/vllm/utils.py#L373). This is just one example, a similar thing happens with the link for ``LLM.encode``. ### Suggest a potential alternative/fix I am not familiar with the way Sphinx generates documentation, but there may be something to be done in one of its configs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Doc]: Documentation source code hyperlinks do not always point to the correct source code documentation ### 📚 The doc issue For example, the documenation of the ``generate`` method in [LLM Class](https://docs.vllm.ai/e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rates documentation, but there may be something to be done in one of its configs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tion of the ``generate`` method in [LLM Class](https://docs.vllm.ai/en/latest/api/offline_inference/llm.html#vllm.LLM.generate). Clicking its ``source`` button, we find that it points to [an unrelated function in utils]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
