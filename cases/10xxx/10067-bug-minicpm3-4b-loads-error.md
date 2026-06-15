# vllm-project/vllm#10067: [Bug]: MiniCPM3-4B loads error

| 字段 | 值 |
| --- | --- |
| Issue | [#10067](https://github.com/vllm-project/vllm/issues/10067) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MiniCPM3-4B loads error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM llm = LLM(model="/data/share/rwq/MiniCPM3-4B/",trust_remote_code=True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` the error: ``` Encountered exception while importing datamodel_code_generator: No module named 'tomli' --------------------------------------------------------------------------- ImportError Traceback (most recent call last) Cell In[3], line 12 9 sampling_params = SamplingParams(temperature=0.8, top_p=0.95) 11 # Create an LLM. ---> 12 llm = LLM(model="/home/powerop/work/rwq/finetune_models/minicpm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t: {generated_text!r}") ``` the error: ``` Encountered exception while importing datamodel_code_generator: No module named 'tomli' --------------------------------------------------------------------------- ImportError...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: MiniCPM3-4B loads error bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: te_code=True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: izer_mode, skip_tokenizer_init, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_context_len_to_cap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: roup.from_config(cls, tokenizer_pool_config, **init_kwargs) 27 @classmethod 28 def from_config(cls, tokenizer_pool_config: Optional[TokenizerPoolConfig], 29 **init_kwargs) -> "TokenizerGroup": ---> 30 return cls(**init_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
