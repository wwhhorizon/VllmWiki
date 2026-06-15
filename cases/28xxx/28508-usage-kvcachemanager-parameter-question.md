# vllm-project/vllm#28508: [Usage]: KVCacheManager Parameter question

| 字段 | 值 |
| --- | --- |
| Issue | [#28508](https://github.com/vllm-project/vllm/issues/28508) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: KVCacheManager Parameter question

### Issue 正文摘录

I noticed that the parameter “self.req_to_block_hashes” has been removed from KVCacheManager since version v0.10.0. But this parameter is still preserved in the official documentation. Could you please provide an explanation of this change? - [Document Description](https://docs.vllm.ai/en/v0.9.2/api/vllm/v1/core/kv_cache_manager.html) - [Version v0.10.0 code](https://github.com/vllm-project/vllm/blob/v0.10.0/vllm/v1/core/kv_cache_manager.py) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: er “self.req_to_block_hashes” has been removed from KVCacheManager since version v0.10.0. But this parameter is still preserved in the official documentation. Could you please provide an explanation of this change? - [D...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: py) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nager Parameter question usage I noticed that the parameter “self.req_to_block_hashes” has been removed from KVCacheManager since version v0.10.0. But this parameter is still preserved in the official documentation. Cou...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
