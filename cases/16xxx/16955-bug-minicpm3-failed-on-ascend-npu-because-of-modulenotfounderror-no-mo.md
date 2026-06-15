# vllm-project/vllm#16955: [Bug]: MiniCPM3 failed on ascend npu because of ModuleNotFoundError: No module named 'triton'

| 字段 | 值 |
| --- | --- |
| Issue | [#16955](https://github.com/vllm-project/vllm/issues/16955) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MiniCPM3 failed on ascend npu because of ModuleNotFoundError: No module named 'triton'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The reproduction scripts: ```python import os from vllm import LLM, SamplingParams os.environ["VLLM_USE_MODELSCOPE"] = "True" prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(max_tokens=100, temperature=0.0) # Create an LLM. llm = LLM(model="OpenBMB/MiniCPM3-4B") # Generate texts from the prompts. outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` This issue mainly because of `triton` is imported and `@triton.jit` is called scattered in many places, and this break many platforms that doesn't support triton, e.g., ascend npu, cpu. And I've made a pr to solve this: https://github.com/vllm-project/vllm/pull/15099. Hope this could be fixed asap. related issues: - https://github.com/vllm-project/vllm/issues/14888 - https://github.com/vllm-project/vllm/issues/12823 - https://github.com/vllm-project/vllm/issues/12384 ### Before submitting a ne...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: M3 failed on ascend npu because of ModuleNotFoundError: No module named 'triton' bug ### Your current environment ### 🐛 Describe the bug The reproduction scripts: ```python import os from vllm import LLM, SamplingParams...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ironment ### 🐛 Describe the bug The reproduction scripts: ```python import os from vllm import LLM, SamplingParams os.environ["VLLM_USE_MODELSCOPE"] = "True" prompts = [ "Hello, my name is", "The president of the United...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 384 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: thon import os from vllm import LLM, SamplingParams os.environ["VLLM_USE_MODELSCOPE"] = "True" prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is",...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
