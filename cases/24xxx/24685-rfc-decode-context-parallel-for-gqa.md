# vllm-project/vllm#24685: [RFC]: Decode Context Parallel for GQA

| 字段 | 值 |
| --- | --- |
| Issue | [#24685](https://github.com/vllm-project/vllm/issues/24685) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Decode Context Parallel for GQA

### Issue 正文摘录

### Motivation. A follow-up to adapt DCP to GQA after https://github.com/vllm-project/vllm/pull/23734. The purpose is to reduce the KV cache storage on each GPU as it is split across the DCP ranks. It increase the overhead of collective communication brought by CP attention. Attention is not able to be executed by TP across the heads. ### Proposed Change. - For decode, we need to make sure the KV from prefill is stored in interleave mode with each rank storing i % dcp_world_size. It should not change the index of group KV as they are orthogonal. - The attention kernel needs to be checked and support return LSE. We can start from flashinfer. FA and triton will be checked afterwards. - The LSE needs to be collected by allgather after blockwise based attention and correct it. The blockwise attention outputs are allreduced afterwards to get the final correct outputs. The corresponding [impl](https://github.com/vllm-project/vllm/blob/main/vllm/attention/ops/common.py#L84) is done and supposed there is no change needed. ### Feedback Period. 1-2 weeks ### CC List. @youkaichao @youzhedian ### Any Other Things. Test plan is to experiment on llama3 model ### Before submitting a new issue......

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ion kernel needs to be checked and support return LSE. We can start from flashinfer. FA and triton will be checked afterwards. - The LSE needs to be collected by allgather after blockwise based attention and correct it....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: thogonal. - The attention kernel needs to be checked and support return LSE. We can start from flashinfer. FA and triton will be checked afterwards. - The LSE needs to be collected by allgather after blockwise based att...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ichao @youzhedian ### Any Other Things. Test plan is to experiment on llama3 model ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the botto...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Decode Context Parallel for GQA RFC ### Motivation. A follow-up to adapt DCP to GQA after https://github.com/vllm-project/vllm/pull/23734. The purpose is to reduce the KV cache storage on each GPU as it is split...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: del ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
