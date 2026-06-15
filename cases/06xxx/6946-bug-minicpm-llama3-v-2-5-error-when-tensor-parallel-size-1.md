# vllm-project/vllm#6946: [Bug]: MiniCPM-Llama3-V-2_5 error when tensor_parallel_size>1

| 字段 | 值 |
| --- | --- |
| Issue | [#6946](https://github.com/vllm-project/vllm/issues/6946) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniCPM-Llama3-V-2_5 error when tensor_parallel_size>1

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug tensor_parallel_size=1 works fine, but error when tensor_parallel_size>1. ```python import torch from PIL import Image from transformers import AutoModel, AutoTokenizer from vllm import LLM, SamplingParams model_path = "/home/work/MiniCPM-Llama3-V-2_5" image = Image.open('x.jpg').convert('RGB') llm = LLM( model=model_path, trust_remote_code=True, tensor_parallel_size=2, ) question = 'What is in the image?' tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True) messages = [{ 'role': 'user', 'content': f'( ./ )\n{question}' }] prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) sampling_params = SamplingParams(temperature=0.7, max_tokens=512, stop_token_ids=[128001, 128009]) inputs = { "prompt": prompt, "multi_modal_data": { "image": image }, } outputs = llm.generate(inputs, sampling_params=sampling_params) for o in outputs: generated_text = o.outputs[0].text print(generated_text) ``` ```bash (VllmWorkerProcess pid=11819) ERROR 07-30 20:15:19 multiproc_worker_utils.py:226] File "/home/work/gitclone/vllm-main/vllm/execut...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: MiniCPM-Llama3-V-2_5 error when tensor_parallel_size>1 bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug tensor_parallel_size=1 works fine, but error when t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: at_template(messages, tokenize=False, add_generation_prompt=True) sampling_params = SamplingParams(temperature=0.7, max_tokens=512, stop_token_ids=[128001, 128009]) inputs = { "prompt": prompt, "multi_mo
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: llel_size=1 works fine, but error when tensor_parallel_size>1. ```python import torch from PIL import Image from transformers import AutoModel, AutoTokenizer from vllm import LLM, SamplingParams model_path = "/home/work...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed all tensors to be on the same device, but found at least two devices, cuda:0 and cuda:1! (when checking argument for argument weight in method wrapper_CUDA__cudnn_convolution) ``` development frontend_api;model_suppo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
