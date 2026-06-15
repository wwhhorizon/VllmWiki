# vllm-project/vllm#27894: [Bug][compile]: SP + PP + "-rms_norm" does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#27894](https://github.com/vllm-project/vllm/issues/27894) |
| 状态 | open |
| 标签 | bug;torch.compile;keep-open |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][compile]: SP + PP + "-rms_norm" does not work

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug Repro -- first delete [these lines](https://github.com/vllm-project/vllm/blob/de92d916fe8a897b00a8adb0aab9ed9ec99f2b6c/vllm/config/vllm.py#L338-L339) which enable `rms_norm` if SP + PP are turned on: ```python config = CompilationConfig( mode=CompilationMode.VLLM_COMPILE, pass_config=PassConfig( enable_sequence_parallelism=True, enable_noop=True, ), splitting_ops=[], full_cuda_graph=True, ) llm = LLM( model="hmellor/tiny-random-LlamaForCausalLM", gpu_memory_utilization=0.6, max_model_len=2048, max_num_seqs=8, compilation_config=config, tensor_parallel_size=2, pipeline_parallel_size=2, distributed_executor_backend="mp", ) # Simple generation test prompts = ["Hello, my name is"] outputs = llm.generate(prompts, SamplingParams(temperature=0, max_tokens=32)) # Print the outputs print("-" * 60) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}") print(f"Output: {generated_text!r}") print("-" * 60) ``` Since [is_residual_scattered_for_sp](https://github.com/vllm-project/vllm/blob/f29aeb5a25dad044306684e205adc159949c6ccb/vllm/v1/worker/gpu_model_runner.py#L1992-L2003) is...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: LM_COMPILE, pass_config=PassConfig( enable_sequence_parallelism=True, enable_noop=True, ), splitting_ops=[], full_cuda_graph=True, ) llm = LLM( model="hmellor/tiny-random-LlamaForCausalLM", gpu_memory_utilization=0.6, m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: com/vllm-project/vllm/blob/de92d916fe8a897b00a8adb0aab9ed9ec99f2b6c/vllm/config/vllm.py#L338-L339) which enable `rms_norm` if SP + PP are turned on: ```python config = CompilationConfig( mode=CompilationMode.VLLM_COMPIL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug][compile]: SP + PP + "-rms_norm" does not work bug;torch.compile;keep-open ### Your current environment main ### 🐛 Describe the bug Repro -- first delete [these lines](https://github.com/vllm-project/vllm/blob/de92...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: allel_size=2, pipeline_parallel_size=2, distributed_executor_backend="mp", ) # Simple generation test prompts = ["Hello, my name is"] outputs = llm.generate(prompts, SamplingParams(temperature=0, max_tokens=32)) # Print...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: . So we tried setting `is_residual_scattered_for_sp` so that this is False when we're tracing but True in the runtime, but then this runs into an error at runtime, since inductor adds input shape guards and checks in th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
