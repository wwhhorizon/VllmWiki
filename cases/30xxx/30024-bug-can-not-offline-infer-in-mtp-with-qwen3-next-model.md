# vllm-project/vllm#30024: [Bug]: Can not offline infer in MTP with Qwen3-Next model

| 字段 | 值 |
| --- | --- |
| Issue | [#30024](https://github.com/vllm-project/vllm/issues/30024) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Can not offline infer in MTP with Qwen3-Next model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The code is ```python from vllm import LLM, SamplingParams import torch prompts = [ "Hello, my name is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) #llm = LLM(model="meta-llama/Llama-2-7b-chat-hf") llm = LLM( model="../Qwen3-Next-80B-A3B-Instruct-FP8", tokenizer_mode="auto", gpu_memory_utilization=0.8, enforce_eager=True, tensor_parallel_size=2, speculative_config={ "method": "qwen3_next_mtp", "num_speculative_tokens":2 } ) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` The output is ```text INFO 12-04 11:42:43 [__init__.py:381] Cudagraph is disabled under eager mode Traceback (most recent call last): File " ", line 1, in File "/usr/lib/python3.12/multiprocessing/spawn.py", line 122, in spawn_main exitcode = _main(fd, parent_sentinel) ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/multiprocessing/spawn.py", line 131, in _main prepare(preparation_data) File "/usr/lib/python3.12/multiprocessing/spawn.py", line 246, in prepare _fix...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Can not offline infer in MTP with Qwen3-Next model bug ### Your current environment ### 🐛 Describe the bug The code is ```python from vllm import LLM, SamplingParams import torch prompts = [ "Hello, my name is",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t!r}") ``` The output is ```text INFO 12-04 11:42:43 [__init__.py:381] Cudagraph is disabled under eager mode Traceback (most recent call last): File " ", line 1, in File "/usr/lib/python3.12/multiprocessing/spawn.py",...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: environment ### 🐛 Describe the bug The code is ```python from vllm import LLM, SamplingParams import torch prompts = [ "Hello, my name is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) #llm = LLM(mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: lama-2-7b-chat-hf") llm = LLM( model="../Qwen3-Next-80B-A3B-Instruct-FP8", tokenizer_mode="auto", gpu_memory_utilization=0.8, enforce_eager=True, tensor_parallel_size=2, speculative_config={ "method": "qwen3_next_mtp",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: utilization=0.8, enforce_eager=True, tensor_parallel_size=2, speculative_config={ "method": "qwen3_next_mtp", "num_speculative_tokens":2 } ) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for outp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
