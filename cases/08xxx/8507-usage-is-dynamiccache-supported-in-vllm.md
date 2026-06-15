# vllm-project/vllm#8507: [Usage]:  Is DynamicCache supported in vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#8507](https://github.com/vllm-project/vllm/issues/8507) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Is DynamicCache supported in vllm?

### Issue 正文摘录

### by using DynamicCache llm don't need to re compute the previous prompt. it can re use previous prompt kv cache! ### In gemini it's called context caching gemini & in anthropic it's called prompt caching ### The DynamicCache is a mechanism used to store and reuse the intermediate computations (key-value pairs) from previous iterations of the model's attention layers. This is particularly useful in scenarios where you're generating multiple responses in a conversation or processing a stream of related inputs ### can i use DynamicCache mechanism in vllm? I'm currently working with large language models and have been using the DynamicCache feature from the Hugging Face Transformers library for efficient multi-turn conversations. I'm interested in potentially using vllm for its performance benefits, but I have a question about feature parity: ### Does vllm currently support an equivalent to the DynamicCache functionality? If not, is this a feature that's on the roadmap or being considered for future implementation? Context: The primary benefit of DynamicCache is that it allows the model to avoid recomputing attention for previous prompts in a conversation. This significantly improv...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: DynamicCache feature from the Hugging Face Transformers library for efficient multi-turn conversations. I'm interested in potentially using vllm for its performance benefits, but I have a question about feature parity:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: B-Instruct" model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map='auto') tokenizer = AutoTokenizer.from_pretrained(model_id) user_prompts = ["Give me a short introduction to large...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ermediate computations (key-value pairs) from previous iterations of the model's attention layers. This is particularly useful in scenarios where you're generating multiple responses in a conversation or processing a st...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Is DynamicCache supported in vllm? usage;stale ### by using DynamicCache llm don't need to re compute the previous prompt. it can re use previous prompt kv cache! ### In gemini it's called context caching gemin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in anthropic it's called prompt caching ### The DynamicCache is a mechanism used to store and reuse the intermediate computations (key-value pairs) from previous iterations of the model's attention layers. This is parti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
