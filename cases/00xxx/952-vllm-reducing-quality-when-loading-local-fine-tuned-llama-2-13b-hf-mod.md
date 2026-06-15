# vllm-project/vllm#952: vllm reducing quality when loading local fine tuned Llama-2-13b-hf model

| 字段 | 值 |
| --- | --- |
| Issue | [#952](https://github.com/vllm-project/vllm/issues/952) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm reducing quality when loading local fine tuned Llama-2-13b-hf model

### Issue 正文摘录

Has anyone else encountered the issue that a model loaded with vllm generates low quality/gibberish output when using a local, fine tuned Llama-2-13b-hf model? Just using the standard inference method from the vllm blog: ``` from vllm import LLM, SamplingParams llm = LLM(model="/home/jupyter/tuned-Llama-2-13b-hf") --> this returns low quality #llm = LLM(model="meta-llama/Llama-2-13b-hf") --> this works as expected sampling_params = SamplingParams(top_p=0.9,temperature=0.9) prompts = [ "### Instruction:\n\n### Input:\ntell me a joke.\n### Response:", "### Instruction:\n\n### Input:\ncapital of france\n### Response:", ] outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Example output tuned model: > Prompt: '### Instruction:\n\n### Input:\ntell me a joke.\n### Response:', Generated text: 'Napoleon Doctor FALSEangel FIFALoc paradéklog;\r internally NGCзар quatre Compet probability' > > Prompt: '### Instruction:\n\n### Input:\ncapital of france\n### Response:', Generated text: "wide]{'}$-poss следуdw */ achtpit AUT Ne premiersErrors у...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vllm reducing quality when loading local fine tuned Llama-2-13b-hf model Has anyone else encountered the issue that a model loaded with vllm generates low quality/gibberish output when using a local, fine tuned Llama-2-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vllm reducing quality when loading local fine tuned Llama-2-13b-hf model Has anyone else encountered the issue that a model loaded with vllm generates low quality/gibberish output when using a local, fine tuned Llama-2-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t_ids = tokenizer(query, return_tensors="pt", truncation=True).input_ids.cuda() outputs = model.generate(input_ids=input_ids, max_new_tokens=300, do_sample=True, top_p=0.9,temperature=0.9) return(tokenizer.batch_decode(...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g quality when loading local fine tuned Llama-2-13b-hf model Has anyone else encountered the issue that a model loaded with vllm generates low quality/gibberish output when using a local, fine tuned Llama-2-13b-hf model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 300, do_sample=True, top_p=0.9,temperature=0.9) return(tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0][len(query):]) get_llama2_prediction("tell me a joke") ``` Any ideas how I can sa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
