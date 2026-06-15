# vllm-project/vllm#2140: torch.cuda.OutOfMemoryError: CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#2140](https://github.com/vllm-project/vllm/issues/2140) |
| 状态 | closed |
| 标签 |  |
| 评论 | 35; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> torch.cuda.OutOfMemoryError: CUDA out of memory

### Issue 正文摘录

I am running this code example from hugging face's TheBloke/zephyr-7B-beta-AWQ ``` from vllm import LLM, SamplingParams import os os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:512" prompts = [ "Tell me about AI", # "Write a story about llamas", # "What is 291 - 150?", # "How much wood would a woodchuck chuck if a woodchuck could chuck wood?", ] prompt_template=f''' {prompts} ''' prompts = [prompt_template.format(prompt=prompt) for prompt in prompts] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="TheBloke/zephyr-7B-beta-AWQ", quantization="awq", dtype="auto", gpu_memory_utilization=0.5) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Unfortunately I get this error torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 GiB. GPU 0 has a total capacty of 14.58 GiB of which 9.93 GiB is free. Including non-PyTorch memory, this process has 4.64 GiB memory in use. Of the allocated memory 4.38 GiB is allocated by PyTorch, and 755.50 KiB is reserved by Py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: example from hugging face's TheBloke/zephyr-7B-beta-AWQ ``` from vllm import LLM, SamplingParams import os os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:512" prompts = [ "Tell me about AI", # "Write a story...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ze_mb:512" prompts = [ "Tell me about AI", # "Write a story about llamas", # "What is 291 - 150?", # "How much wood would a woodchuck chuck if a woodchuck could chuck wood?", ] prompt_template=f''' {prompts} ''' prompts...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: erature=0.8, top_p=0.95) llm = LLM(model="TheBloke/zephyr-7B-beta-AWQ", quantization="awq", dtype="auto", gpu_memory_utilization=0.5) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: torch.cuda.OutOfMemoryError: CUDA out of memory I am running this code example from hugging face's TheBloke/zephyr-7B-beta-AWQ ``` from vllm import LLM, SamplingParams import os os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: quantization;sampling_logits;scheduler_memory cuda;quantization;sampling oom dtype;env_dependency I am running this code example from hugging face's TheBloke/zephyr-7B-beta-AWQ

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
