# vllm-project/vllm#25630: [Bug]: Inconsistent TorchSDPAMetadata definition in cpu_attn.py causes TypeError and AttributeError

| 字段 | 值 |
| --- | --- |
| Issue | [#25630](https://github.com/vllm-project/vllm/issues/25630) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Inconsistent TorchSDPAMetadata definition in cpu_attn.py causes TypeError and AttributeError

### Issue 正文摘录

### Your current environment When running a simple demo using a CPU model on a MacBook, I've encountered an issue with inconsistent variables ### 🐛 Describe the bug code----------------------- from vllm import LLM, SamplingParams prompts = [ "你是谁?" ] if __name__ == "__main__": sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/Users/xxx/modelscope/Qwen3-0.6B", max_num_batched_tokens=40960, max_model_len=256) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ---------------result ``` INFO 09-25 13:42:34 [__init__.py:216] Automatically detected platform cpu. INFO 09-25 13:42:36 [utils.py:233] non-default args: {'max_model_len': 256, 'max_num_batched_tokens': 40960, 'disable_log_stats': True, 'model': '/Users/xxx/modelscope/Qwen3-0.6B'} INFO 09-25 13:42:36 [model.py:545] Resolved architecture: Qwen3ForCausalLM `torch_dtype` is deprecated! Use `dtype` instead! WARNING 09-25 13:42:36 [model.py:1732] Your device 'cpu' doesn't support torch.bfloat16. Falling back to torch.float16 for compatibility. WARNING 09-25...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: variables ### 🐛 Describe the bug code----------------------- from vllm import LLM, SamplingParams prompts = [ "你是谁?" ] if __name__ == "__main__": sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 5 13:42:36 [model.py:545] Resolved architecture: Qwen3ForCausalLM `torch_dtype` is deprecated! Use `dtype` instead! WARNING 09-25 13:42:36 [model.py:1732] Your device 'cpu' doesn't support torch.bfloat16. Falling back t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bug ### Your current environment When running a simple demo using a CPU model on a MacBook, I've encountered an issue with inconsistent variables ### 🐛 Describe the bug code----------------------- from vllm import LLM,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: set, using 4 by default. INFO 09-25 13:42:36 [arg_utils.py:1156] Chunked prefill is not supported for ARM and POWER and S390X CPUs; disabling it for V1 backend. INFO 09-25 13:42:38 [__init__.py:216] Automatically detect...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 6 [cpu.py:114] Environment variable VLLM_CPU_KVCACHE_SPACE (GiB) for CPU backend is not set, using 4 by default. INFO 09-25 13:42:36 [arg_utils.py:1156] Chunked prefill is not supported for ARM and POWER and S390X CPUs;...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
