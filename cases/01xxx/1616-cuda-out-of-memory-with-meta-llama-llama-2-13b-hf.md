# vllm-project/vllm#1616: CUDA out of memory with meta-llama/Llama-2-13b-hf 

| 字段 | 值 |
| --- | --- |
| Issue | [#1616](https://github.com/vllm-project/vllm/issues/1616) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA out of memory with meta-llama/Llama-2-13b-hf 

### Issue 正文摘录

I am trying for days to solve this issue with no clue: CUDA out of memory. Tried to allocate 150.00 MiB (GPU 0; 14.58 GiB total capacity; 13.94 GiB already allocated; 17.31 MiB free; 13.94 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF I just use the example code with meta-llama/Llama-2-13b-hf model in GCP VM of the following specification: n1-standard-16 1 x NVIDIA Tesla P4 Virtual Workstation AND n1-highmem-4 1 x NVIDIA T4 Virtual Workstation The code as follow: shown as follow: from vllm import LLM, SamplingParams from huggingface_hub import login login("...") prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="meta-llama/Llama-2-13b-hf", tokenizer="hf-internal-testing/llama-tokenizer") outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: CUDA out of memory with meta-llama/Llama-2-13b-hf I am trying for days to solve this issue with no clue: CUDA out of memory. Tried to allocate 150.00 MiB (GPU 0; 14.58 GiB total capacity; 13.94 GiB already allocated; 17...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: out of memory. Tried to allocate 150.00 MiB (GPU 0; 14.58 GiB total capacity; 13.94 GiB already allocated; 17.31 MiB free; 13.94 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: CUDA out of memory with meta-llama/Llama-2-13b-hf I am trying for days to solve this issue with no clue: CUDA out of memory. Tried to allocate 150.00 MiB (GPU 0; 14.58 GiB total capacity; 13.94 GiB already allocated; 1
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: rontend_api;model_support;sampling_logits;scheduler_memory cuda;sampling oom I am trying for days to solve this issue with no clue:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: be the problem ? performance frontend_api;model_support;sampling_logits;scheduler_memory cuda;sampling oom I am trying for days to solve this issue with no clue:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
