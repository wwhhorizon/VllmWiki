# vllm-project/vllm#1464: Correctness issue with `Llama-7b` and batch size 3

| 字段 | 值 |
| --- | --- |
| Issue | [#1464](https://github.com/vllm-project/vllm/issues/1464) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Correctness issue with `Llama-7b` and batch size 3

### Issue 正文摘录

`"meta-llama/Llama-2-7b-hf"`, is returning different output vs. original HF model with a batch size of 3. This is running on a single A10G with tensor-parallel=1. With a batch size of 1, the output is the same. ```python from vllm.transformers_utils.tokenizer import get_tokenizer from vllm import LLM, SamplingParams from transformers import AutoModelForCausalLM import torch model_name = "meta-llama/Llama-2-7b-hf" prompts = ["Translate the following English sentence into Japanese, French, and Swahili: 'The early bird catches the worm.'"] * 3 max_tokens = 128 tokenizer = get_tokenizer(model_name, trust_remote_code=True) hf_model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.half, trust_remote_code=True).cuda() hf_outputs = [] for prompt in prompts: input_ids = tokenizer(prompt, return_tensors="pt").input_ids output_ids = hf_model.generate(input_ids.cuda(), use_cache=True, max_new_tokens=128, do_sample=False) output_str = tokenizer.batch_decode(output_ids, skip_special_tokens=True, cleanup_tokenization_spaces=False) hf_outputs.append(output_str[0]) del hf_model vllm_engine = LLM(model=model_name, tokenizer=model_name, trust_remote_code=True, dtype="half", swap_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: he output is the same. ```python from vllm.transformers_utils.tokenizer import get_tokenizer from vllm import LLM, SamplingParams from transformers import AutoModelForCausalLM import torch model_name = "meta-llama/Llama...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Correctness issue with `Llama-7b` and batch size 3 `"meta-llama/Llama-2-7b-hf"`, is returning different output vs. original HF model with a batch size of 3. This is running on a single A10G with tensor-parallel=1. With...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: h `Llama-7b` and batch size 3 `"meta-llama/Llama-2-7b-hf"`, is returning different output vs. original HF model with a batch size of 3. This is running on a single A10G with tensor-parallel=1. With a batch size of 1, th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: =True) hf_model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.half, trust_remote_code=True).cuda() hf_outputs = [] for prompt in prompts: input_ids = tokenizer(prompt, return_tensors="pt").input_i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: m_pretrained(model_name, torch_dtype=torch.half, trust_remote_code=True).cuda() hf_outputs = [] for prompt in prompts: input_ids = tokenizer(prompt, return_tensors="pt").input_ids output_ids = hf_model.generate(input_id...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
