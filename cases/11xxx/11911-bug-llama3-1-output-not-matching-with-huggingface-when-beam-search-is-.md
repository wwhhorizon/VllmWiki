# vllm-project/vllm#11911: [Bug]: LLAMA3.1 output not matching with HuggingFace when beam search is enabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#11911](https://github.com/vllm-project/vllm/issues/11911) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LLAMA3.1 output not matching with HuggingFace when beam search is enabled.

### Issue 正文摘录

### Your current environment A100 GPU CUDA 12.1 LLAMA 3.1. 7B with LORA adapter vLLM 0.6.1.post2 torch 2.4.0 transformer 4.43.3 HF code : inputs = tokenizer(prompt, return_tensors="pt") input_ids = inputs["input_ids"].to('cuda') generation_config = GenerationConfig( temperature=0, top_p=1, top_k=-1, num_beams=2, # Number of beams for beam search num_return_sequences=2, # Return all beams ) generate_params = { "input_ids": input_ids, "generation_config": generation_config, "return_dict_in_generate": True, "output_scores": True, "max_new_tokens": 128, } with torch.no_grad(): generation_output = model.generate( input_ids=input_ids, generation_config=generation_config, return_dict_in_generate=True, output_scores=True, max_new_tokens=128 ) s = generation_output.sequences[0] output = tokenizer.decode(s,skip_special_tokens=True) result = output.split('assistant')[1].strip() vLLM Code : class SimpleVLLMLlama2: def __init__(self, base_model_path, number_of_gpu=1, gpu_memory_utilization=0.9): """ Constructor that loads the model for inference. """ self.base_model_path = base_model_path self.number_of_gpu = number_of_gpu self.gpu_memory_utilization = gpu_memory_utilization self.prompter = Pr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: LLAMA3.1 output not matching with HuggingFace when beam search is enabled. bug;stale ### Your current environment A100 GPU CUDA 12.1 LLAMA 3.1. 7B with LORA adapter vLLM 0.6.1.post2 torch 2.4.0 transformer 4.43.3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: LLAMA3.1 output not matching with HuggingFace when beam search is enabled. bug;stale ### Your current environment A100 GPU CUDA 12.1 LLAMA 3.1. 7B with LORA adapter vLLM 0.6.1.post2 torch 2.4.0 transformer 4.43.3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: .1 output not matching with HuggingFace when beam search is enabled. bug;stale ### Your current environment A100 GPU CUDA 12.1 LLAMA 3.1. 7B with LORA adapter vLLM 0.6.1.post2 torch 2.4.0 transformer 4.43.3 HF code : in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ) s = generation_output.sequences[0] output = tokenizer.decode(s,skip_special_tokens=True) result = output.split('assistant')[1].strip() vLLM Code : class SimpleVLLMLlama2: def __init__(self, base_model_path, number_of_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: self.model = LLM( model=self.base_model_path, dtype=torch.float16, tensor_parallel_size=self.number_of_gpu, gpu_memory_utilization=self.gpu_memory_utilization, enable_lora=True, # enable or disable LoRA as needed max_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
