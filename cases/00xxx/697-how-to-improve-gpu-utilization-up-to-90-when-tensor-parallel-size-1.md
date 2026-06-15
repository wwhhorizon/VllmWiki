# vllm-project/vllm#697: How to improve GPU utilization up to 90%+ when tensor_parallel_size>1 ？

| 字段 | 值 |
| --- | --- |
| Issue | [#697](https://github.com/vllm-project/vllm/issues/697) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> How to improve GPU utilization up to 90%+ when tensor_parallel_size>1 ？

### Issue 正文摘录

I use this code run vllm infer ``` llm = LLM(model=model_path, dtype='bfloat16',tensor_parallel_size=2, max_num_seqs=512, gpu_memory_utilization=0.95) with open('all_toxic.response', 'w') as f: #for line in open('/tmp/all_toxic.prompts'): for line in open('all_toxic.prompts'): items = line.strip('\n').split('\t') prefix_info.append(items) prompts.append(' '+prefix+items[-1]+' ') if len(prompts) == 5500: outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt for out in output.outputs: generated_text = out.text.replace('\n','\\n').replace('\t', ' ') #print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") f.write('\t'.join(items+[generated_text])+'\n') prompts=[] outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output, items in zip(outputs, prefix_info): prompt = output.prompt for out in output.outputs: generated_text = out.text.replace('\n','\\n').replace('\t', ' ') #print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") f.write('\t'.join(items+[generated_text])+'\n') ``` my env is A100 80G*4, gpu utilization is between 50~99%,avg 74%. **How to improve GPU utilization up to 90%+...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _size>1 ？ I use this code run vllm infer ``` llm = LLM(model=model_path, dtype='bfloat16',tensor_parallel_size=2, max_num_seqs=512, gpu_memory_utilization=0.95) with open('all_toxic.response', 'w') as f: #for line in op...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: f.write('\t'.join(items+[generated_text])+'\n') ``` my env is A100 80G*4, gpu utilization is between 50~99%,avg 74%. **How to improve GPU utilization up to 90%+ when tensor_parallel_size>1 ？** ``` +---------------------...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: --------------------------------------+ | NVIDIA-SMI 470.161.03 Driver Version: 470.161.03 CUDA Version: 11.7 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: en tensor_parallel_size>1 ？ I use this code run vllm infer ``` llm = LLM(model=model_path, dtype='bfloat16',tensor_parallel_size=2, max_num_seqs=512, gpu_memory_utilization=0.95) with open('all_toxic.response', 'w') as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
