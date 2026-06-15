# vllm-project/vllm#9519: [Bug]: Multiple inconsistencies wrt BOS injection and BOS duplication

| 字段 | 值 |
| --- | --- |
| Issue | [#9519](https://github.com/vllm-project/vllm/issues/9519) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multiple inconsistencies wrt BOS injection and BOS duplication

### Issue 正文摘录

### Your current environment 0.6.3.post1 ### 4 🐛generation scenarios There are at least 4 generation use cases in vLLM: 1. offline generate 2. offline chat 3. online completion (similar to 1 but online and a totally different implementation) 4. online chat completion (similar to 2 but online and a totally different implementation) It's up to the user whether they want to handle the chat template themselves and then use (1) or (3) or let vllm do the chat template handling and then it's (2) or (4). ### Summary of BOS injection/duplication I have traced all 4 APIs wrt BOS-injection and here is what I see (0.6.3post1): 1. offline `generate` - the client sorts out the chat template - **BOS is forced always** - so generates 2 BOS tokens if the prompt already has one - so the user has to send a prompt w/o ` ` 2. offline `chat` - **BOS is still always forced** - so generates 2 BOS tokens if the template already has one - this is a BUG and can't be overcome by a user, other than by passing a custom chat template which has ` ` manually removed. 3. `client.completion` - the client sorts out the chat template - **BOS is forced always** - so generates 2 BOS tokens if the prompt already has one...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s") **(2) is clearly a bug and it's inconsistent with (4)**. With `meta-llama/Meta-Llama-3-8B-Instruct` you would see this logged with (2): `{'prompt_token_ids': [128000, 128000, 128006, 9125, 128007, ...` where `128000...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: Multiple inconsistencies wrt BOS injection and BOS duplication bug;stale ### Your current environment 0.6.3.post1 ### 4 🐛generation scenarios There are at least 4 generation use cases in vLLM: 1. offline generate...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: okenizer.bos_token` (e.g. ` ` in many tokenizers). ### Reproduction To reproduce I was just using your examples: 1. https://docs.vllm.ai/en/stable/getting_started/examples/offline_inference.html 2. https://docs.vllm.ai/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Multiple inconsistencies wrt BOS injection and BOS duplication bug;stale ### Your current environment 0.6.3.post1 ### 4 🐛generation scenarios There are at least 4 generation use cases in vLLM: 1. offline generate...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: . but prepended the existing prompt with ` ` in the non-chat examples to test. Thank you!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
