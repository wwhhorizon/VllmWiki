# vllm-project/vllm#25030: [Bug]: Failed to run Qwen/Qwen3-Next-80B-A3B-Instruct on rocm/MI210

| 字段 | 值 |
| --- | --- |
| Issue | [#25030](https://github.com/vllm-project/vllm/issues/25030) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to run Qwen/Qwen3-Next-80B-A3B-Instruct on rocm/MI210

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams if __name__ == '__main__': prompts = [ "The capital of France is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model='Qwen/Qwen3-Next-80B-A3B-Instruct', tensor_parallel_size=4, enforce_eager=True) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ``` WorkerProc hit an exception. Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/triton/language/core.py", line 34, in wrapper return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/triton/language/core.py", line 1451, in arange return semantic.arange(start, end, _builder) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/triton/language/semantic.py", line 627, in arange raise ValueError("arange's range must be a power of 2") ValueError: arange's range must be a power of 2 The above exception was the direct cause of the following excepti...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams if __name__ == '__main__': prompts = [ "The capital of France is", ] sampling_params = SamplingParams(temperature=0.8, top_p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Failed to run Qwen/Qwen3-Next-80B-A3B-Instruct on rocm/MI210 bug;rocm ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams if __name__ == '__main__': prompts = [ "The...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: (most recent call last): File "/usr/local/lib/python3.12/dist-packages/triton/language/core.py", line 34, in wrapper return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/triton/la...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 47, in return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/triton/runtime/jit.py", line 569,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Failed to run Qwen/Qwen3-Next-80B-A3B-Instruct on rocm/MI210 bug;rocm ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams if __name__ == '__main__': prompts = [ "The...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
