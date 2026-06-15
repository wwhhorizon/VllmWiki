# vllm-project/vllm#11297: [Usage]: What are the correct parameters for offline beam search inference in vllm ?

| 字段 | 值 |
| --- | --- |
| Issue | [#11297](https://github.com/vllm-project/vllm/issues/11297) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What are the correct parameters for offline beam search inference in vllm ?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm As beam search api was changed recently and `use_beam_search` was removed from SamplingParams, I'm not sure which is the way to trigger beam search (without sampling) in vllm offline inference. Currently, I'm adopting the following codes: ``` from vllm import LLM, SamplingParams beam_size=4 sampling_params = SamplingParams(temperature=1.0,n=1,top_k=-1,top_p=1,seed=42,max_tokens=128,best_of=beam_size) outputs = vllm_model.chat(messages=prompts, sampling_params=sampling_params, use_tqdm=True) ``` Is this the correct way to trigger beam search ? vllm version: v0.6.4.post1 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ne inference. Currently, I'm adopting the following codes: ``` from vllm import LLM, SamplingParams beam_size=4 sampling_params = SamplingParams(temperature=1.0,n=1,top_k=-1,top_p=1,seed=42,max_tokens=128,best_of=beam_s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: What are the correct parameters for offline beam search inference in vllm ? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm As beam search...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: op_k=-1,top_p=1,seed=42,max_tokens=128,best_of=beam_size) outputs = vllm_model.chat(messages=prompts, sampling_params=sampling_params, use_tqdm=True) ``` Is this the correct way to trigger beam search ? vllm version: v0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
