# vllm-project/vllm#14139: [Bug]: `TransformersModel` fails if model config does not have `head_dim` attr

| 字段 | 值 |
| --- | --- |
| Issue | [#14139](https://github.com/vllm-project/vllm/issues/14139) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `TransformersModel` fails if model config does not have `head_dim` attr

### Issue 正文摘录

### Your current environment vllm@cf069aa ### 🐛 Describe the bug Running models using the transformers fallback fails if `vllm_config.model_config.hf_config` does not contain `head_dim`. For example, using `Qwen/Qwen2.5-0.5B-Instruct`: ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct", model_impl="transformers") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Error: ``` [rank0]: Traceback (most recent call last): [rank0]: File "/scratch/test_qwen.py", line 20, in [rank0]: llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct", enable_prefix_caching=False, compilation_config=3, model_impl="transformers") [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/scratch/vllm/vllm/utils.py", line 1045, in inne...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: `TransformersModel` fails if model config does not have `head_dim` attr bug ### Your current environment vllm@cf069aa ### 🐛 Describe the bug Running models using the transformers fallback fails if `vllm_config.mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: mers.py @@ -146,14 +146,13 @@ class TransformersModel(nn.Module, SupportsQuant, SupportsLoRA): # Attention modifications (assumes 1 attention op per hidden layer) tp_size = get_tensor_model_parallel_world_size() - head_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: `TransformersModel` fails if model config does not have `head_dim` attr bug ### Your current environment vllm@cf069aa ### 🐛 Describe the bug Running models using the transformers fallback fails if `vllm_config.mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: m@cf069aa ### 🐛 Describe the bug Running models using the transformers fallback fails if `vllm_config.model_config.hf_config` does not contain `head_dim`. For example, using `Qwen/Qwen2.5-0.5B-Instruct`: ```python from...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: `. For example, using `Qwen/Qwen2.5-0.5B-Instruct`: ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
