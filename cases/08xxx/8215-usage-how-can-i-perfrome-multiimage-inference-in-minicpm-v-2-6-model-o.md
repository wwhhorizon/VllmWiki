# vllm-project/vllm#8215: [Usage]: how can i perfrome multiimage inference? in MiniCPM-V-2_6 model or any vision language model with vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#8215](https://github.com/vllm-project/vllm/issues/8215) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how can i perfrome multiimage inference? in MiniCPM-V-2_6 model or any vision language model with vllm?

### Issue 正文摘录

`from PIL import Image from transformers import AutoTokenizer from vllm import LLM, SamplingParams import torch MODEL_NAME = "openbmb/MiniCPM-V-2_6" image = Image.open("dubu.png").convert("RGB") tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True) context_length = 2000 num_device = 1 llm = LLM(model=MODEL_NAME, speculative_max_model_len =context_length ,max_seq_len_to_capture=context_length,max_model_len=context_length , tensor_parallel_size=num_device,trust_remote_code=True ,worker_use_ray=num_device, quantization="fp8" ,gpu_memory_utilization = 0.95 , ) messages = [{'role': 'user', 'content': '( ./ )\n' + 'what is in this image?'}] prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) stop_tokens = [' ', ' '] stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens] sampling_params = SamplingParams( temperature=0.9, max_tokens=2000, best_of=3) outputs = llm.generate({ "prompt": prompt, "multi_modal_data": { "image": image } }, sampling_params=sampling_params) print(outputs[0].outputs[0].text)` I have already givem the way i like to use vllm in my script

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: allel_size=num_device,trust_remote_code=True ,worker_use_ray=num_device, quantization="fp8" ,gpu_memory_utilization = 0.95 , ) messages = [{'role': 'user', 'content': '( ./ )\n' + 'what is in this image?'}] prompt = tok...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: iCPM-V-2_6 model or any vision language model with vllm? usage `from PIL import Image from transformers import AutoTokenizer from vllm import LLM, SamplingParams import torch MODEL_NAME = "openbmb/MiniCPM-V-2_6" image =...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s image?'}] prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) stop_tokens = [' ', ' '] stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens] sampling_param...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: how can i perfrome multiimage inference? in MiniCPM-V-2_6 model or any vision language model with vllm? usage `from PIL import Image from transformers import AutoTokenizer from vllm import LLM, SamplingParams i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: =True) context_length = 2000 num_device = 1 llm = LLM(model=MODEL_NAME, speculative_max_model_len =context_length ,max_seq_len_to_capture=context_length,max_model_len=context_length , tensor_parallel_size=num_device,tru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
