# vllm-project/vllm#5825: [RFC]: Classifier-Free Guidance

| 字段 | 值 |
| --- | --- |
| Issue | [#5825](https://github.com/vllm-project/vllm/issues/5825) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Classifier-Free Guidance

### Issue 正文摘录

### Motivation. I am one of the authors of the paper Stay On Topic with Classifier-Free Guidance ( https://openreview.net/forum?id=RiM3cl9MdK&noteId=s1BXLL1YZD ) who has been nominated as ICML'24 Spotlight Paper. CFG is a sampling technique that allows LLMs to follow the prompt more closely at the cost of two forward passes per token as well as 2 kv caches. CFG brings non trivial improvements overall over standard benchmarks. I would be extremely interested in having CFG implemented into vLLM. If possible, I would like to get a bit of guidance into the vLLM code base. ### Proposed Change. CFG contrasts the next token logits between two different prompt (a "positive prompt" a, and a "negative prompt" or "unconditional" b) Here is the pseudo algorithm ``` while we sample: logits_a = log_softmax(model(prompt_a)) logits_b = log_softmax(model(prompt_b)) logits = logits_b + cfg_scale * (logits_a - logits_b) next_token = sample_from(logits) prompt_a.append(next_token) prompt_b.append(next_token) ``` As you can see this needs two concurrent kv-caches for an efficient implementation. I tried looking for how Speculative Decoding was implemented but this was quite complex, more than CFG need...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: pt more closely at the cost of two forward passes per token as well as 2 kv caches. CFG brings non trivial improvements overall over standard benchmarks. I would be extremely interested in having CFG implemented into vL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Classifier-Free Guidance RFC;stale ### Motivation. I am one of the authors of the paper Stay On Topic with Classifier-Free Guidance ( https://openreview.net/forum?id=RiM3cl9MdK&noteId=s1BXLL1YZD ) who has been no...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: oken) ``` As you can see this needs two concurrent kv-caches for an efficient implementation. I tried looking for how Speculative Decoding was implemented but this was quite complex, more than CFG needs. ### Feedback Pe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: logits_b = log_softmax(model(prompt_b)) logits = logits_b + cfg_scale * (logits_a - logits_b) next_token = sample_from(logits) prompt_a.append(next_token) prompt_b.append(next_token) ``` As you can see this needs two co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is the pseudo algorithm ``` while we sample: logits_a = log_softmax(model(prompt_a)) logits_b = log_softmax(model(prompt_b)) logits = logits_b + cfg_scale * (logits_a - logits_b) next_token = sample_from(logits) prompt_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
