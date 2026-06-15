# vllm-project/vllm#17324: [Usage]: How to perform right truncation on the input prompt if it is too long?

| 字段 | 值 |
| --- | --- |
| Issue | [#17324](https://github.com/vllm-project/vllm/issues/17324) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to perform right truncation on the input prompt if it is too long?

### Issue 正文摘录

### Your current environment ``` My env is fine, so I did not put anything here. ``` ### How would you like to use vllm I want to run an inference of a [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct). I want to use LLama 3.1 for inference, and its context length is 128k. I use the following code for chat: ``` sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=512) # Create an LLM. llm = LLM(model=''meta-llama/Meta-Llama-3.1-8B-Instruct'', quantization="fp8", task='generate', tensor_parallel_size=1, enforce_eager=True, enable_expert_parallel=False) outputs = llm.chat(rank_prompts, sampling_params, use_tqdm=True) ``` Sometimes my prompt is too long, causing an error. I want to ask if it's possible to set it to keep only the first k tokens of the prompt. I found that the current vLLM settings for limiting the maximum input tokens seem to keep only the last k tokens, not the first k tokens. I noticed the following settings: ``` 1. The `--max-model-len` parameter in the vLLM engine: Model context length. If unspecified, will be automatically derived from the model config. Supports k/m/g/K/M/G in human-readable forma...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ## How would you like to use vllm I want to run an inference of a [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct). I want to use LLama 3.1 for inference, and its context...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llm = LLM(model=''meta-llama/Meta-Llama-3.1-8B-Instruct'', quantization="fp8", task='generate', tensor_parallel_size=1, enforce_eager=True, enable_expert_parallel=False) outputs = llm.chat(rank_prompts, sampling_params,
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: odel-len` parameter in the vLLM engine: Model context length. If unspecified, will be automatically derived from the model config. Supports k/m/g/K/M/G in human-readable format. Examples: 1k → 1000 1K → 1024 ``` I'm not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ch! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: enforce_eager=True, enable_expert_parallel=False) outputs = llm.chat(rank_prompts, sampling_params, use_tqdm=True) ``` Sometimes my prompt is too long, causing an error. I want to ask if it's possible to set it to keep...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
