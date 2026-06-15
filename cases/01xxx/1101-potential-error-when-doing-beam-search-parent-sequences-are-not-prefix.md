# vllm-project/vllm#1101: POTENTIAL ERROR: When doing beam_search, parent sequences are not prefix of child sequences

| 字段 | 值 |
| --- | --- |
| Issue | [#1101](https://github.com/vllm-project/vllm/issues/1101) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> POTENTIAL ERROR: When doing beam_search, parent sequences are not prefix of child sequences

### Issue 正文摘录

Steps to reproduce: Using the code ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(n=3, use_beam_search=True, temperature=0, early_stopping=True, ) llm = LLM(model="gpt2", gpu_memory_utilization=0.1) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt for o in output.outputs: generated_text = o.text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` When placing a breakpoint at L458 of the file llm_engine.py in the function `_process_sequence_group_samples`, in the first iteration itself the following is observed when one runs the following in the debug console: ```python p = running_child_seqs[0][1] #parent c = running_child_seqs[0][0] #child print(p.output_logprobs, p.output_tokens) [OUTPUT]: [{3700: -5.050571918487549}] ['ĠJames'] print(c.output_logprobs, c.output_tokens) [OUTPUT]: [{1757: -4.613071918487549}] ['ĠJohn'] ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: child sequences Steps to reproduce: Using the code ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI i...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: beam_search, parent sequences are not prefix of child sequences Steps to reproduce: Using the code ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: POTENTIAL ERROR: When doing beam_search, parent sequences are not prefix of child sequences Steps to reproduce: Using the code ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The preside...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 3, use_beam_search=True, temperature=0, early_stopping=True, ) llm = LLM(model="gpt2", gpu_memory_utilization=0.1) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = ou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
