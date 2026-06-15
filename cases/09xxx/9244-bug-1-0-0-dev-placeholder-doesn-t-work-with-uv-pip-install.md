# vllm-project/vllm#9244: [Bug]: 1.0.0.dev placeholder doesn't work with `uv pip install`

| 字段 | 值 |
| --- | --- |
| Issue | [#9244](https://github.com/vllm-project/vllm/issues/9244) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 1.0.0.dev placeholder doesn't work with `uv pip install`

### Issue 正文摘录

### Your current environment na ### Model Input Dumps _No response_ ### 🐛 Describe the bug The recommended way for pip installing latest wheels (i.e. `pip install https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl`) works with vanilla `pip` but does not work with `uv pip`. I raised an [issue](https://github.com/astral-sh/uv/issues/8082) in uv but I don't think this is a uv bug. Would be great to explore more robust options for this. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: 1.0.0.dev placeholder doesn't work with `uv pip install` bug ### Your current environment na ### Model Input Dumps _No response_ ### 🐛 Describe the bug The recommended way for pip installing latest wheels (i.e. `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n't work with `uv pip install` bug ### Your current environment na ### Model Input Dumps _No response_ ### 🐛 Describe the bug The recommended way for pip installing latest wheels (i.e. `pip install https://vllm-wheels.s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ponse_ ### 🐛 Describe the bug The recommended way for pip installing latest wheels (i.e. `pip install https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl`) works with va...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
