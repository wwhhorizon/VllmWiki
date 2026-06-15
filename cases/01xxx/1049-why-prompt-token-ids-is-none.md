# vllm-project/vllm#1049: why prompt token ids is None?

| 字段 | 值 |
| --- | --- |
| Issue | [#1049](https://github.com/vllm-project/vllm/issues/1049) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> why prompt token ids is None?

### Issue 正文摘录

Received request 6f70b6651dbd4df19d25d8c1f4486ad4: prompt: 'San Francisco is a', sampling params: SamplingParams(n=2, best_of=2, presence_penalty=0.0, frequency_penalty=0.0, temperature=0.0, top_p=1.0, top_k=-1, use_beam_search=True, length_penalty=1.0, early_stopping=False, stop=[' '], ignore_eos=False, max_tokens=512, logprobs=None), prompt token ids: None.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: one? Received request 6f70b6651dbd4df19d25d8c1f4486ad4: prompt: 'San Francisco is a', sampling params: SamplingParams(n=2, best_of=2, presence_penalty=0.0, frequency_penalty=0.0, temperature=0.0, top_p=1.0, top_k=-1, us...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: frequency_penalty=0.0, temperature=0.0, top_p=1.0, top_k=-1, use_beam_search=True, length_penalty=1.0, early_stopping=False, stop=[' '], ignore_eos=False, max_tokens=512, logprobs=None), prompt token ids: None.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .0, top_k=-1, use_beam_search=True, length_penalty=1.0, early_stopping=False, stop=[' '], ignore_eos=False, max_tokens=512, logprobs=None), prompt token ids: None.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: why prompt token ids is None? Received request 6f70b6651dbd4df19d25d8c1f4486ad4: prompt: 'San Francisco is a', sampling params: SamplingParams(n=2, best_of=2, presence_penalty=0.0, frequency_penalty=0.0, temperature=0.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
