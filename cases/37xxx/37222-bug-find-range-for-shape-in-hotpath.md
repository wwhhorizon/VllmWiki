# vllm-project/vllm#37222: [Bug]: _find_range_for_shape in hotpath

| 字段 | 值 |
| --- | --- |
| Issue | [#37222](https://github.com/vllm-project/vllm/issues/37222) |
| 状态 | open |
| 标签 | bug;torch.compile |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: _find_range_for_shape in hotpath

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug when cudagraphs off or beyond max cudagraph size, this function is in the hotpath. Most notably, there's a hash. We should be able to avoid this. https://github.com/vllm-project/vllm/blob/714c6e0eab76a4fb1394089d848ecfe46408b9c9/vllm/compilation/piecewise_backend.py#L356-L357 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: compile ### Your current environment main ### 🐛 Describe the bug when cudagraphs off or beyond max cudagraph size, this function is in the hotpath. Most notably, there's a hash. We should be able to avoid this. https://...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: blob/714c6e0eab76a4fb1394089d848ecfe46408b9c9/vllm/compilation/piecewise_backend.py#L356-L357 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: _find_range_for_shape in hotpath bug;torch.compile ### Your current environment main ### 🐛 Describe the bug when cudagraphs off or beyond max cudagraph size, this function is in the hotpath. Most notably, there's...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
