# vllm-project/vllm#1128: the output is not equals compare to huggingface .

| 字段 | 值 |
| --- | --- |
| Issue | [#1128](https://github.com/vllm-project/vllm/issues/1128) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> the output is not equals compare to huggingface .

### Issue 正文摘录

I find the output is not equals compare to huggingface . hugggingface code and output: ``` # Load model directly from transformers import AutoTokenizer, AutoModelForCausalLM tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m") model = AutoModelForCausalLM.from_pretrained("facebook/opt-125m").cuda().half() prompt = [ "Hello, what is apple? ", ] input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda() generated_ids = model.generate(input_ids, do_sample=False, repetition_penalty=1.2, max_new_tokens=500) texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True) print(texts) """ I'm a bit confused.\nApple is the company that makes iPhones and iPads. They are also known for their Macs.\nI thought they were called Apple Pencils?\nThey're called Apple Pencils." """ ``` and vllm ``` from vllm import LLM, SamplingParams prompts = [ "Hello, what is apple? ", ] # Create a sampling params object. sampling_params = SamplingParams( temperature=0, max_tokens=500, frequency_penalty=1.2 ) # Create an LLM. llm = LLM(model="facebook/opt-125m", block_size=8, gpu_memory_utilization= 0.8) for i in range(1): outputs = llm.generate(prompts, sampling_params) # Print the o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: gingface code and output: ``` # Load model directly from transformers import AutoTokenizer, AutoModelForCausalLM tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m") model = AutoModelForCausalLM.from_pretraine...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: .input_ids.cuda() generated_ids = model.generate(input_ids, do_sample=False, repetition_penalty=1.2, max_new_tokens=500) texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True) print(texts) """ I'm a bit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the output is not equals compare to huggingface . I find the output is not equals compare to huggingface . hugggingface code and output: ``` # Load model directly from transformers import AutoTokenizer, AutoModelForCaus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 125m") model = AutoModelForCausalLM.from_pretrained("facebook/opt-125m").cuda().half() prompt = [ "Hello, what is apple? ", ] input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda() generated_ids = model.gen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: se, repetition_penalty=1.2, max_new_tokens=500) texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True) print(texts) """ I'm a bit confused.\nApple is the company that makes iPhones and iPads. They are a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
