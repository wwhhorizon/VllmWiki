# vllm-project/vllm#16945: [Bug]: top k isn't deterministic

| 字段 | 值 |
| --- | --- |
| Issue | [#16945](https://github.com/vllm-project/vllm/issues/16945) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: top k isn't deterministic

### Issue 正文摘录

### Your current environment main branch 299ebb62b269ce167eb1c71b5e39a1dc1f65ce1c ### 🐛 Describe the bug Question: Will same prompt and same sampling_param lead to same output? https://github.com/vllm-project/vllm/blob/main/tests/v1/tpu/test_sampler.py#L59 I ran this script and the output isn't always the same. ```python from vllm import LLM, SamplingParams prompts = [ "Write a short story about a robot that dreams for the first time." ] prompts = prompts * 10 sampling_params = SamplingParams(temperature=0.1, min_p=0.8, top_k=12, max_tokens=64) def main(): # Set `enforce_eager=True` to avoid ahead-of-time compilation. # In real workloads, `enforace_eager` should be `False`. llm = LLM(model="Qwen/Qwen2-1.5B-Instruct", max_num_batched_tokens=512, max_num_seqs=4, enforce_eager=True) outputs = llm.generate(prompts, sampling_params) print("-" * 50) for output in outputs: generated_text = output.outputs[0].text print(f"Generated text: {generated_text!r}") print("-" * 50) if __name__ == "__main__": main() ``` output ``` -------------------------------------------------- Generated text: ' Once upon a time, in a faraway land, there was a robot named R2D2. R2D2 was a simple, yet efficient r...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: top k isn't deterministic bug ### Your current environment main branch 299ebb62b269ce167eb1c71b5e39a1dc1f65ce1c ### 🐛 Describe the bug Question: Will same prompt and same sampling_param lead to same output? https...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n this script and the output isn't always the same. ```python from vllm import LLM, SamplingParams prompts = [ "Write a short story about a robot that dreams for the first time." ] prompts = prompts * 10 sampling_params...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # In real workloads, `enforace_eager` should be `False`. llm = LLM(model="Qwen/Qwen2-1.5B-Instruct", max_num_batched_tokens=512, max_num_seqs=4, enforce_eager=True) outputs = llm.generate(prompts, sampling_params) print...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: top k isn't deterministic bug ### Your current environment main branch 299ebb62b269ce167eb1c71b5e39a1dc1f65ce1c ### 🐛 Describe the bug Question: Will same prompt and same sampling_param lead to same output? https...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
