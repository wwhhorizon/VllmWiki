# vllm-project/vllm#349: error when run the vllm to generate

| 字段 | 值 |
| --- | --- |
| Issue | [#349](https://github.com/vllm-project/vllm/issues/349) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> error when run the vllm to generate

### Issue 正文摘录

The code is here: # encoding: utf-8 from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) print("sampling_params", sampling_params) llm = LLM(model="/media/odin/software/PycharmProjects/OpenBuddy-main/model/openbuddy-openllama-7b-v5-fp16/") outputs = llm.generate(prompts, sampling_params) print("outputs", outputs) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") the error is here: Traceback (most recent call last): File "/media/odin/software/PycharmProjects/vllm-main/vllm_test.py", line 2, in from vllm import LLM, SamplingParams File "/media/odin/software/PycharmProjects/vllm-main/vllm/__init__.py", line 2, in from vllm.engine.async_llm_engine import AsyncLLMEngine File "/media/odin/software/PycharmProjects/vllm-main/vllm/engine/async_llm_engine.py", line 6, in from vllm.engine.llm_engine import LLMEngine File "/media/odin/software/PycharmProjects/vllm-main/vllm/engine/llm_engine.py", line 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n run the vllm to generate The code is here: # encoding: utf-8 from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ure=0.8, top_p=0.95) print("sampling_params", sampling_params) llm = LLM(model="/media/odin/software/PycharmProjects/OpenBuddy-main/model/openbuddy-openllama-7b-v5-fp16/") outputs = llm.generate(prompts, sampling_params...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: er.py", line 8, in from vllm.model_executor import get_model, InputMetadata, set_random_seed File "/media/odin/software/PycharmProjects/vllm-main/vllm/model_executor/__init__.py", line 2, in from vllm.model_executor.mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: call last): File "/media/odin/software/PycharmProjects/vllm-main/vllm_test.py", line 2, in from vllm import LLM, SamplingParams File "/media/odin/software/PycharmProjects/vllm-main/vllm/__init__.py", line 2, in from vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
