# vllm-project/vllm#14735: [Bug]: Progress Bar Inconsistency When `n > 1` in `vllm.LLM.generate`

| 字段 | 值 |
| --- | --- |
| Issue | [#14735](https://github.com/vllm-project/vllm/issues/14735) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Progress Bar Inconsistency When `n > 1` in `vllm.LLM.generate`

### Issue 正文摘录

### Your current environment [env.txt](https://github.com/user-attachments/files/19224261/env.txt) ### 🐛 Describe the bug When running `vllm.LLM.generate` with `n > 1`, the tqdm progress bar shows an incorrect total count. Specifically, the denominator (total steps) does not correctly account for the fact that multiple generations are being produced per prompt. For example, when using the following code: ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95, n=10) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) ``` The progress bar output looks like this: ``` Processed prompts: 10%|███ | 4/40 [00:00 1`. 2. Observe that the tqdm progress bar does not match the expected number of generated outputs. **Proposed Fix:** Adjust the total count in tqdm to account for `n * len(prompts)`, ensuring that the progress bar correctly reflects the actual workload. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ` with `n > 1`, the tqdm progress bar shows an incorrect total count. Specifically, the denominator (total steps) does not correctly account for the fact that multiple generations are being produced per prompt. For exam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ng_params = SamplingParams(temperature=0.8, top_p=0.95, n=10) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) ``` The progress bar output looks like this: ``` Processed prompts: 10%...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
