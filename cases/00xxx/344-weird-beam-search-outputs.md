# vllm-project/vllm#344: Weird beam search outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#344](https://github.com/vllm-project/vllm/issues/344) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Weird beam search outputs

### Issue 正文摘录

While playing with it I've stumbled upon strange behavior that might indicate that there is some issue when the beam search is used. I've started the server with: `python3 -m vllm.entrypoints.api_server --model mosaicml/mpt-30b` When I request: ``` curl http://vllm.ai/generate \ -d '{ "prompt": "San Francisco is a", "max_tokens":64, "temperature": 0, "n":1 }' ``` I get more or less expected answer: ``` {"text": ["San Francisco is a city of neighborhoods, and each has its own character. The following is a brief description of the most popular areas.\n\n\u2022 **Downtown** (also called SoMa, for South of Market) is the city's financial district, with a few hotels, restaurants, and shops.\n\n\u2022 **Union Square"]} ``` However when I use beam_search: ``` curl http://vllm.ai/generate \ -d '{ "prompt": "San Francisco is a", "max_tokens":64, "use_beam_search": true, "temperature": 0, "n":4 }' ``` I get: ``` {"text": [ "San Francisco is a very city, visit each with its own personality and and The\n\n### Fisherman's Wharf**Fisherman's Wharf is the city's is the | ### Top Sights | ### Sights | ### Eating | ### Drinking & Night", "San Francisco is a great place to live, but it's character...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ``` curl http://vllm.ai/generate \ -d '{ "prompt": "San Francisco is a", "max_tokens":64, "temperature": 0, "n":1 }' ``` I get more or less expected answer: ``` {"text": ["San Francisco is a city of neighborhoods, and e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Weird beam search outputs bug While playing with it I've stumbled upon strange behavior that might indicate that there is some issue when the beam search is used. I've started the server with: `python3 -m vllm.entrypoin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: I've started the server with: `python3 -m vllm.entrypoints.api_server --model mosaicml/mpt-30b` When I request: ``` curl http://vllm.ai/generate \ -d '{ "prompt": "San Francisco is a", "max_tokens":64, "temperature": 0,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: python3 -m vllm.entrypoints.api_server --model mosaicml/mpt-30b` When I request: ``` curl http://vllm.ai/generate \ -d '{ "prompt": "San Francisco is a", "max_tokens":64, "temperature": 0, "n":1 }' ``` I get more or les...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: wers?). Interestingly enough the problem manifest only with `n>2`. I've tested for `n=3`, `n=4` and `n=5`, for `n=2` it looks correct: ``` {"text": [ "San Francisco is a great place to live, but it's not a great place t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
