# vllm-project/vllm#5950: [Feature]: Way to using LLM's last hidden state embedding vector

| 字段 | 值 |
| --- | --- |
| Issue | [#5950](https://github.com/vllm-project/vllm/issues/5950) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Way to using LLM's last hidden state embedding vector

### Issue 正文摘录

### 🚀 The feature, motivation and pitch My suggestion is simple, **vllm must support for last hidden state embedding vector**. Here is some example. ### Prompt Setting I fine-tuned my local llm model, with following prompt setting. ``` ##INPUT{"category": "Female Clothes", "brand": "LouisVuitton", "name": ""}\n ##RESULT{"category": "Female Clothes", "brand": "LouisVuitton", "name": "{{goods_name}}" ``` So, I can try to inference my model with this prompt input. ``` ##INPUT{"category": "Female Perfume", "brand": "Channel": "name": ""}\n ##RESULT ``` Model Generate completed goods name. ``` ##INPUT{"category": "Female Perfume", "brand": "Channel": "name": ""}\n ##RESULT{"category": "Female Perfume", "brand": "Channel": "name": "Channel CoCo Mademoiselle Queen Test 100ml"} ``` yeah, this model could generate unseen goods name, even in a plausible way! ### Embedding Ideation Let's re-think about inference prompt input. ``` ##INPUT{"category": "Female Perfume", "brand": "Channel": "name": ""}\n ##RESULT ``` The hidden state for generating the next token of "##RESULT" will be semantically very closely related to the goods name. Therefore, if we can assumes that good prompts are prepared...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Feature]: Way to using LLM's last hidden state embedding vector feature request;stale ### 🚀 The feature, motivation and pitch My suggestion is simple, **vllm must support for last hidden state embedding vector**. Here...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: nion[RequestOutput, EmbeddingRequestOutput]]: seq_group_metadata_list, scheduler_outputs = self.scheduler.schedule() if not scheduler_outputs.is_empty(): execute_model_req = ExecuteModelRequest( seq_group_metadata_list=...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: lass - We have to change Scheduler class, because of garbage collect for kv-cache. ##### `_schedule_prefills()` ``` def _schedule_prefills( self, waiting_queue: deque, budget: SchedulingBudget, curr_loras: Optional[Set[...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r**. Here is some example. ### Prompt Setting I fine-tuned my local llm model, with following prompt setting. ``` ##INPUT{"category": "Female Clothes", "brand": "LouisVuitton", "name": ""}\n ##RESULT{"category": "Female...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e Perfume", "brand": "Channel": "name": "Channel CoCo Mademoiselle Queen Test 100ml"} ``` yeah, this model could generate unseen goods name, even in a plausible way! ### Embedding Ideation Let's re-think about inference...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
