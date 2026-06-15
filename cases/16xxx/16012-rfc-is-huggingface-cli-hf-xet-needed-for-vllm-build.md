# vllm-project/vllm#16012: [RFC]: Is `huggingface-cli[hf_xet]` needed for vllm build?

| 字段 | 值 |
| --- | --- |
| Issue | [#16012](https://github.com/vllm-project/vllm/issues/16012) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Is `huggingface-cli[hf_xet]` needed for vllm build?

### Issue 正文摘录

### Motivation. Recently `huggingface-cli[hf_xet]` was added in `requirements/common.txt` and `requirements/test.in`. Is it needed in `requirements/common.txt` ? If not, can it be moved to rocm build/test requirements? Ref: [15969](https://github.com/vllm-project/vllm/pull/15969) ### Proposed Change. Moving `huggingface-cli[hf_xet]` from `requirements/common.txt` to `requirements/rocm.txt` or `requirements/rocm-test.txt` ### Feedback Period. _No response_ ### CC List. @hmellor ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Is it needed in `requirements/common.txt` ? If not, can it be moved to rocm build/test requirements? Ref: [15969](https://github.com/vllm-project/vllm/pull/15969) ### Proposed Change. Moving `huggingface-cli[hf_xet]` fr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Is `huggingface-cli[hf_xet]` needed for vllm build? RFC ### Motivation. Recently `huggingface-cli[hf_xet]` was added in `requirements/common.txt` and `requirements/test.in`. Is it needed in `requirements/common.t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: Is `huggingface-cli[hf_xet]` needed for vllm build? RFC ### Motivation. Recently `huggingface-cli[hf_xet]` was added in `requirements/common.txt` and `requirements/test.in`. Is it needed in `requirements/common.t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ce-cli[hf_xet]` was added in `requirements/common.txt` and `requirements/test.in`. Is it needed in `requirements/common.txt` ? If not, can it be moved to rocm build/test requirements? Ref: [15969](https://github.com/vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
