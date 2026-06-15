# vllm-project/vllm#336: open_llama: ValueError: head_size (100) is not supported. Supported head sizes: [64, 80, 96, 128]

| 字段 | 值 |
| --- | --- |
| Issue | [#336](https://github.com/vllm-project/vllm/issues/336) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> open_llama: ValueError: head_size (100) is not supported. Supported head sizes: [64, 80, 96, 128]

### Issue 正文摘录

I start vllm with “openlm-research/open_llama_3b” model: ``` from vllm import LLM, SamplingParams import os prompts = [ "The president of the United States is" ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/home/ubuntu/wangjibo/models/openlm-research_open_llama_3b/", gpu_memory_utilization=0.3) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` the model file dir： ``` total 6.4G drwxr-xr-x 2 ubuntu ubuntu 4.0K Jul 3 12:56 ./ drwxrwxr-x 6 ubuntu ubuntu 4.0K Jul 3 12:14 ../ -rw-r--r-- 1 ubuntu ubuntu 506 Jul 3 12:14 config.json -rw-r--r-- 1 ubuntu ubuntu 137 Jul 3 12:14 generation_config.json -rw-r--r-- 1 ubuntu ubuntu 289 Jul 3 12:56 huggingface-metadata.txt -rw-r--r-- 1 ubuntu ubuntu 6.4G Jul 3 12:56 pytorch_model.bin -rw-r--r-- 1 ubuntu ubuntu 11K Jul 3 12:14 README.md -rw-r--r-- 1 ubuntu ubuntu 330 Jul 3 12:14 special_tokens_map.json -rw-r--r-- 1 ubuntu ubuntu 593 Jul 3 12:14 tokenizer_config.json -rw-r--r-- 1 ubuntu ubuntu 522K Jul 3 12:14 tokenizer.model ``` An error like...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: open_llama: ValueError: head_size (100) is not supported. Supported head sizes: [64, 80, 96, 128] feature request I start vllm with “openlm-research/open_llama_3b” model: ``` from vllm import LLM, SamplingParams import...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ig: model='/home/ubuntu/wangjibo/models/openlm-research_open_llama_3b/', dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 07-03 15:24:14 tokeniz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t I start vllm with “openlm-research/open_llama_3b” model: ``` from vllm import LLM, SamplingParams import os prompts = [ "The president of the United States is" ] sampling_params = SamplingParams(temperature=0.8, top_p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ion_config.json -rw-r--r-- 1 ubuntu ubuntu 289 Jul 3 12:56 huggingface-metadata.txt -rw-r--r-- 1 ubuntu ubuntu 6.4G Jul 3 12:56 pytorch_model.bin -rw-r--r-- 1 ubuntu ubuntu 11K Jul 3 12:14 README.md -rw-r--r-- 1 ubuntu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: (100) is not supported. Supported head sizes: [64, 80, 96, 128] feature request I start vllm with “openlm-research/open_llama_3b” model: ``` from vllm import LLM, SamplingParams import os prompts = [ "The president of t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
