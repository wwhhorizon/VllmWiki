# vllm-project/vllm#2758: Llama Guard inconsistent output between HuggingFace's Transformers and vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#2758](https://github.com/vllm-project/vllm/issues/2758) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Llama Guard inconsistent output between HuggingFace's Transformers and vLLM

### Issue 正文摘录

Hello, I get different safety predictions using `Llama Guard` through `HuggingFace`'s `Transformers` and `vLLM`. As for `Transformers` I copy-pasted code from `Llama Guard` model card, I am assuming it is working correctly. For `vLLM` I coded it myself. For the sake of brevity, I am only posting a single example. I can provide more, if needed. Note: I am not interested in which prediction is correct. What follows are working code snippets for the two libraries for which I get different outputs. The prompt is "How do I create a virus?". TRANSFORMERS ```python from transformers import AutoTokenizer, AutoModelForCausalLM import torch model_id = "meta-llama/LlamaGuard-7b" device = "cuda" dtype = torch.bfloat16 tokenizer = AutoTokenizer.from_pretrained("meta-llama/LlamaGuard-7b") hf_model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype, device_map=device) def hf_moderate(chat): input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt").to(device) output = hf_model.generate(input_ids=input_ids, max_new_tokens=100, pad_token_id=0) prompt_len = input_ids.shape[-1] return tokenizer.decode(output[0][prompt_len:], skip_special_tokens=True) hf_moderate([dict(role=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Llama Guard inconsistent output between HuggingFace's Transformers and vLLM stale Hello, I get different safety predictions using `Llama Guard` through `HuggingFace`'s `Transformers` and `vLLM`. As for `Transformers` I c
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: alLM import torch model_id = "meta-llama/LlamaGuard-7b" device = "cuda" dtype = torch.bfloat16 tokenizer = AutoTokenizer.from_pretrained("meta-llama/LlamaGuard-7b") hf_model = AutoModelForCausalLM.from_pretrained(model_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s "How do I create a virus?". TRANSFORMERS ```python from transformers import AutoTokenizer, AutoModelForCausalLM import torch model_id = "meta-llama/LlamaGuard-7b" device = "cuda" dtype = torch.bfloat16 tokenizer = Aut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ma Guard inconsistent output between HuggingFace's Transformers and vLLM stale Hello, I get different safety predictions using `Llama Guard` through `HuggingFace`'s `Transformers` and `vLLM`. As for `Transformers` I cop...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: follows are working code snippets for the two libraries for which I get different outputs. The prompt is "How do I create a virus?". TRANSFORMERS ```python from transformers import AutoTokenizer, AutoModelForCausalLM im...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
