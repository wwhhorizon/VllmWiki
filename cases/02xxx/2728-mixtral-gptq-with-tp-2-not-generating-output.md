# vllm-project/vllm#2728: Mixtral GPTQ with TP=2 not generating output

| 字段 | 值 |
| --- | --- |
| Issue | [#2728](https://github.com/vllm-project/vllm/issues/2728) |
| 状态 | closed |
| 标签 |  |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mixtral GPTQ with TP=2 not generating output

### Issue 正文摘录

In the new vllm 0.3 release mixtral with gptq does not generate any output anymore. Loading the model works fine, when calling the `llm.generate` it gets stuck. ``` from vllm import SamplingParams import torch model_name = "TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ" llm = vllm.LLM(model=model_name, quantization="gptq", dtype=torch.float16, tensor_parallel_size=2, max_model_len=16000, revision="gptq-4bit-32g-actorder_True", gpu_memory_utilization=0.75, enforce_eager=False) llm.generate(formatted_prompt[0], sampling_params=SamplingParams(temperature=0.1, max_tokens=100)) ``` Currently using: - python 3.11.* - vllm-0.3.0+cu123 -> tried also the current git repo - cuda 12.3 The worker seems to be stuck in the `llm_engine.step()` function / `_run_workers` call.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: eBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ" llm = vllm.LLM(model=model_name, quantization="gptq", dtype=torch.float16, tensor_parallel_size=2, max_model_len=16000, revision="gptq-4bit-32g-actorder_True", gpu_memory_utilizat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ease mixtral with gptq does not generate any output anymore. Loading the model works fine, when calling the `llm.generate` it gets stuck. ``` from vllm import SamplingParams import torch model_name = "TheBloke/Mixtral-8...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rks fine, when calling the `llm.generate` it gets stuck. ``` from vllm import SamplingParams import torch model_name = "TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ" llm = vllm.LLM(model=model_name, quantization="gptq", dty...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: - python 3.11.* - vllm-0.3.0+cu123 -> tried also the current git repo - cuda 12.3 The worker seems to be stuck in the `llm_engine.step()` function / `_run_workers` call.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tq-4bit-32g-actorder_True", gpu_memory_utilization=0.75, enforce_eager=False) llm.generate(formatted_prompt[0], sampling_params=SamplingParams(temperature=0.1, max_tokens=100)) ``` Currently using: - python 3.11.* - vll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
