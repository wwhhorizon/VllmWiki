# vllm-project/vllm#4180: [Usage]: Llama 3 8B Instruct Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#4180](https://github.com/vllm-project/vllm/issues/4180) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Llama 3 8B Instruct Inference

### Issue 正文摘录

### Your current environment Using the latest version of vLLM on 2 L4 GPUs. ### How would you like to use vllm I was trying to utilize vLLM to deploy [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) model and use OpenAI compatible server with the latest docker image. When I did, it was not stopping generation for a while when `max_tokens=None`. I saw that it's generating ` ` token which is its eos token apparently but in their `tokenizer_config` and in other configs it is ` `. I can fix this by setting the `eos_token` parameter in `tokenizer_config.json` as ` ` or using ```python response = client.chat.completions.create( model="meta-llama/Meta-Llama-3-8B-Instruct", messages=[{"role": "user", "content": "Write a function for fibonacci sequence. Use LRUCache"}], max_tokens=700, stream=False, extra_body={"stop_token_ids":[128009]} ) ``` `stop_token_ids` in my request. I wanted to ask the optimal way to solve this problem. There is an existing [discussion/PR](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct/discussions/4) in their repo which is updating the `generation_config.json` but unless I clone myself, I saw that vLLM d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Instruct Inference usage ### Your current environment Using the latest version of vLLM on 2 L4 GPUs. ### How would you like to use vllm I was trying to utilize vLLM to deploy [meta-llama/Meta-Llama-3-8B-Instruct](https:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Llama 3 8B Instruct Inference usage ### Your current environment Using the latest version of vLLM on 2 L4 GPUs. ### How would you like to use vllm I was trying to utilize vLLM to deploy [meta-llama/Meta-Llama-3...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: or fibonacci sequence. Use LRUCache"}], max_tokens=700, stream=False, extra_body={"stop_token_ids":[128009]} ) ``` `stop_token_ids` in my request. I wanted to ask the optimal way to solve this problem. There is an exist...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: extra_body={"stop_token_ids":[128009]} ) ``` `stop_token_ids` in my request. I wanted to ask the optimal way to solve this problem. There is an existing [discussion/PR](https://huggingface.co/meta-llama/Meta-Llama-3-8B-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 3 8B Instruct Inference usage ### Your current environment Using the latest version of vLLM on 2 L4 GPUs. ### How would you like to use vllm I was trying to utilize vLLM to deploy [meta-llama/Meta-Llama-3-8B-Instruct](h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
