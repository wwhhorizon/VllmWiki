# vllm-project/vllm#6800: [Bug]: Discrepancy in vLLM and LoRA Adapter Scores with Different Package Versions

| 字段 | 值 |
| --- | --- |
| Issue | [#6800](https://github.com/vllm-project/vllm/issues/6800) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Discrepancy in vLLM and LoRA Adapter Scores with Different Package Versions

### Issue 正文摘录

### Your current environment Packages used for both finetuning and inference (vllm==0.3.2): torch==2.1.2 accelerate==0.27.2 transformers==4.40.1 sentence_transformers==2.7.0 Description: With the above package versions, the vLLM scores do not match those of the LoRA adapter. LoRA Scoring Code: with torch.no_grad(): generation_output = self.model.generate( input_ids=input_ids, generation_config=generation_config, return_dict_in_generate=True, output_scores=True, max_new_tokens=max_new_tokens ) s = generation_output.sequences[0] output = self.tokenizer.decode(s, skip_special_tokens=True) vLLM Scoring Code: self._model = LLM(self._base_model_path, tensor_parallel_size=self.number_of_gpu, gpu_memory_utilization=self.gpu_memory_utilization, enable_lora=True) prompts = self.prompter.generate_prompts(instructions, inputs) sampling_params = SamplingParams(temperature=temperature, top_p=top_p, top_k=top_k, max_tokens=max_new_tokens, use_beam_search=use_beam_search, best_of=best_of) adaptor_id = self.lora_adapters.get_adapter_id(adaptor_name) adaptor_path = self.lora_adapters.get_adapter_path(adaptor_name) outputs = self._model.generate( prompts, sampling_params, lora_request=LoRARequest(ad...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: erature, top_p=top_p, top_k=top_k, max_tokens=max_new_tokens, use_beam_search=use_beam_search, best_of=best_of) adaptor_id = self.lora_adapters.get_adapter_id(adaptor_name) adaptor_path = self.lora_adapters.get_adapter_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ancy in vLLM and LoRA Adapter Scores with Different Package Versions bug;stale ### Your current environment Packages used for both finetuning and inference (vllm==0.3.2): torch==2.1.2 accelerate==0.27.2 transformers==4....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Bug]: Discrepancy in vLLM and LoRA Adapter Scores with Different Package Versions bug;stale ### Your current environment Packages used for both finetuning and inference (vllm==0.3.2): torch==2.1.2 accelerate==0.27.2 tra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: . LoRA Scoring Code: with torch.no_grad(): generation_output = self.model.generate( input_ids=input_ids, generation_config=generation_config, return_dict_in_generate=True, output_scores=True, max_new_tokens=max_new_toke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
