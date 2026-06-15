# vllm-project/vllm#26830: [Bug]: pytest -v compile/test_full_graph.py failing for PyTorch 2.9

| 字段 | 值 |
| --- | --- |
| Issue | [#26830](https://github.com/vllm-project/vllm/issues/26830) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: pytest -v compile/test_full_graph.py failing for PyTorch 2.9

### Issue 正文摘录

### Your current environment PyTorch 2.9, started showing up on https://github.com/vllm-project/vllm/pull/24994 after a recent rebase ### 🐛 Describe the bug https://buildkite.com/vllm/ci/builds/34479#0199d273-f27f-48c2-857d-831e8793f572/163-5686, pytest -v compile/test_full_graph.py -k test_custom_compile_config[compilation_config12-model_info12] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: pytest -v compile/test_full_graph.py failing for PyTorch 2.9 bug;torch.compile ### Your current environment PyTorch 2.9, started showing up on https://github.com/vllm-project/vllm/pull/24994 after a recent rebase...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 72/163-5686, pytest -v compile/test_full_graph.py -k test_custom_compile_config[compilation_config12-model_info12] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 12] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: pytest -v compile/test_full_graph.py failing for PyTorch 2.9 bug;torch.compile ### Your current environment PyTorch 2.9, started showing up on https://github.com/vllm-project/vllm/pull/24994 after a recent rebase...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
