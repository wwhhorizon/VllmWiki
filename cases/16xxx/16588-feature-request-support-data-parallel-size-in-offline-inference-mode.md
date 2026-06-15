# vllm-project/vllm#16588: [Feature Request]: Support data_parallel_size in offline inference mode

| 字段 | 值 |
| --- | --- |
| Issue | [#16588](https://github.com/vllm-project/vllm/issues/16588) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature Request]: Support data_parallel_size in offline inference mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tested qwen2.5-3b-it and gemma3-27b-it and found that when the data parallel size is greater than 1, the model initialization gets stuck in an infinite hang. I have provided the simplest reproduction code and logs for reference. ```python from vllm import LLM, SamplingParams if __name__ == '__main__': # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model = 'PATH TO ANY LLM ',data_parallel_size=2,tensor_parallel_size=2,enable_prefix_caching=True,enforce_eager=True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. print("\nGenerated Outputs:\n" + "-" * 60) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}") print(f"Output: {generated_text!r}") print("-" * 60) ``` ```bash INFO 04-14 19:5...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ;stale ### Your current environment ### 🐛 Describe the bug I tested qwen2.5-3b-it and gemma3-27b-it and found that when the data parallel size is greater than 1, the model initialization gets stuck in an infinite hang....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: simplest reproduction code and logs for reference. ```python from vllm import LLM, SamplingParams if __name__ == '__main__': # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature Request]: Support data_parallel_size in offline inference mode feature request;stale ### Your current environment ### 🐛 Describe the bug I tested qwen2.5-3b-it and gemma3-27b-it and found that when the data par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sh INFO 04-14 19:51:04 [__init__.py:239] Automatically detected platform cuda. INFO 04-14 19:51:23 [config.py:600] This model supports multiple tasks: {'classify', 'generate', 'reward', 'score', 'embed'}. Defaulting to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: request;stale ### Your current environment ### 🐛 Describe the bug I tested qwen2.5-3b-it and gemma3-27b-it and found that when the data parallel size is greater than 1, the model initialization gets stuck in an infinite...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
