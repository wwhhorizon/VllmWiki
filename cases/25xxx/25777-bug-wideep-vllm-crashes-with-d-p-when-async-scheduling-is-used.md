# vllm-project/vllm#25777: [Bug][WideEP]: vLLM Crashes with D/P when --async-scheduling is used.

| 字段 | 值 |
| --- | --- |
| Issue | [#25777](https://github.com/vllm-project/vllm/issues/25777) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][WideEP]: vLLM Crashes with D/P when --async-scheduling is used.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using these manifests on coreweave, except with `--async-scheduling` added. https://github.com/llm-d/llm-d/tree/wide_ep_bench_0.3/guides/wide-ep-lws/manifests/modelserver/base We're crashing. It's related to async scheduling + P/D and possibly DBO. Logs: https://gist.github.com/tlrmchlsmth/a9885252311c6811c0538b1004f72cb9 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: scheduling + P/D and possibly DBO. Logs: https://gist.github.com/tlrmchlsmth/a9885252311c6811c0538b1004f72cb9 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .com/llm-d/llm-d/tree/wide_ep_bench_0.3/guides/wide-ep-lws/manifests/modelserver/base We're crashing. It's related to async scheduling + P/D and possibly DBO. Logs: https://gist.github.com/tlrmchlsmth/a9885252311c6811c0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: thub.com/llm-d/llm-d/tree/wide_ep_bench_0.3/guides/wide-ep-lws/manifests/modelserver/base We're crashing. It's related to async scheduling + P/D and possibly DBO. Logs: https://gist.github.com/tlrmchlsmth/a9885252311c68...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
