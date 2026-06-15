# vllm-project/vllm#13222: [Misc]:  Question about Grouped-query attention (GQA)

| 字段 | 值 |
| --- | --- |
| Issue | [#13222](https://github.com/vllm-project/vllm/issues/13222) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]:  Question about Grouped-query attention (GQA)

### Issue 正文摘录

### Implementation of Grouped-query attention (GQA) Hello:) I was wondering whether [Grouped-query attention](https://arxiv.org/pdf/2305.13245#:~:text=Multi%2Dquery%20attention%20shares%20single,head%20and%20multi%2Dquery%20attention) (GQA) is implemented in vLLM. I see that Llama3 models come with this feature in their [architecture](https://arxiv.org/pdf/2407.21783), and they are available through vLLM. Are they using GQA in the backend? Thanks a lot and sorry for the inconveniences ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nd%20multi%2Dquery%20attention) (GQA) is implemented in vLLM. I see that Llama3 models come with this feature in their [architecture](https://arxiv.org/pdf/2407.21783), and they are available through vLLM. Are they usin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 7.21783), and they are available through vLLM. Are they using GQA in the backend? Thanks a lot and sorry for the inconveniences ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ented in vLLM. I see that Llama3 models come with this feature in their [architecture](https://arxiv.org/pdf/2407.21783), and they are available through vLLM. Are they using GQA in the backend? Thanks a lot and sorry fo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
