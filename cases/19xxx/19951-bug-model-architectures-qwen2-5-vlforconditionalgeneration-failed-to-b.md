# vllm-project/vllm#19951: [Bug]: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected

| 字段 | 值 |
| --- | --- |
| Issue | [#19951](https://github.com/vllm-project/vllm/issues/19951) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) def main(): # Create an LLM. llm = LLM(model="Qwen/Qwen2.5-VL-7B-Instruct") # Generate texts from the prompts. # The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. print("\nGenerated Outputs:\n" + "-" * 60) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}") print(f"Output: {generated_text!r}") print("-" * 60) if __name__ == "__main__": main() ``` ```text Traceback (most recent call last): File "vllm/examples/offline_inference/basic/basic.py", line 35, in main() File "vllm/examples/offline_inference/basic/basic.py", line 19, in main llm = LLM(model="Q...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: FileCopyrightText: Copyright contributors to the vLLM project from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected bug ### Your current environment ### 🐛 Describe the bug ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected bug ### Your current environment ### 🐛 Describe the bug ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ls. [type=value_error, input_value=ArgsKwargs((), {'model': ...attention_dtype': None}), input_type=ArgsKwargs] For further information visit https://errors.pydantic.dev/2.10/v/value_error ``` ### Before submitting a ne...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
