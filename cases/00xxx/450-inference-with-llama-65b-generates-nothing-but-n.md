# vllm-project/vllm#450: Inference with LLaMA 65B generates nothing but \n

| 字段 | 值 |
| --- | --- |
| Issue | [#450](https://github.com/vllm-project/vllm/issues/450) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Inference with LLaMA 65B generates nothing but \n

### Issue 正文摘录

The problem only happens with LLaMA 65B, LLaMA 7B/13B/30B work well. Below is the reproduce code： ``` from vllm import LLM, SamplingParams args_model = '/mnt/sdb/ly/models/hf_converted_llama/65B/' llm = LLM(model=args_model, tokenizer=args_model, tokenizer_mode='slow', dtype='float16', seed=42, tensor_parallel_size=8) sampling_params = SamplingParams(temperature=0, max_tokens=10) prompt = 'The capital of France is' outputs = llm.generate(prompts=[prompt], sampling_params=sampling_params) outputs ``` ``` >>> outputs [RequestOutput(request_id=0, prompt='The capital of France is', prompt_token_ids=[0, 450, 7483, 310, 3444, 338], outputs=[CompletionOutput(index=0, text='\n\n\n\n\n\n\n\n\n\n', token_ids=[13, 13, 13, 13, 13, 13, 13, 13, 13, 13], cumulative_logprob=-34.18291640281677, logprobs={}, finish_reason=length)], finished=True)] >>> sampling_params = SamplingParams(temperature=0.1, max_tokens=10) ``` And HuggingFace transformers works as normal: ``` import transformers tokenizers = transformers.LlamaTokenizer.from_pretrained("/mnt/sdb/ly/models/hf_converted_llama/65B/") model = transformers.LlamaForCausalLM.from_pretrained("/mnt/sdb/ly/models/hf_converted_llama/65B/", device_map=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Inference with LLaMA 65B generates nothing but \n bug;stale The problem only happens with LLaMA 65B, LLaMA 7B/13B/30B work well. Below is the reproduce code： ``` from vllm import LLM, SamplingParams args_model = '/mnt/s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Inference with LLaMA 65B generates nothing but \n bug;stale The problem only happens with LLaMA 65B, LLaMA 7B/13B/30B work well. Below is the reproduce code： ``` from vllm import LLM, SamplingParams args_model = '/mnt/s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: , LLaMA 7B/13B/30B work well. Below is the reproduce code： ``` from vllm import LLM, SamplingParams args_model = '/mnt/sdb/ly/models/hf_converted_llama/65B/' llm = LLM(model=args_model, tokenizer=args_model, tokenizer_m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llm = LLM(model=args_model, tokenizer=args_model, tokenizer_mode='slow', dtype='float16', seed=42, tensor_parallel_size=8) sampling_params = SamplingParams(temperature=0, max_tokens=10) prompt = 'The capital of France i...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: em only happens with LLaMA 65B, LLaMA 7B/13B/30B work well. Below is the reproduce code： ``` from vllm import LLM, SamplingParams args_model = '/mnt/sdb/ly/models/hf_converted_llama/65B/' llm = LLM(model=args_model, tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
