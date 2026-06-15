# vllm-project/vllm#1134: [BUG]: NaN issue again after commit e67b4f2

| 字段 | 值 |
| --- | --- |
| Issue | [#1134](https://github.com/vllm-project/vllm/issues/1134) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG]: NaN issue again after commit e67b4f2

### Issue 正文摘录

It seems that the old issue #936 happened again after this PR #1004. An easy test could be ```python from vllm import LLM, SamplingParams import contextlib import torch from transformers import AutoModelForCausalLM, AutoTokenizer from typing import List def vllm(prompt : str): with contextlib.nullcontext(): llm = LLM("lmsys/vicuna-7b-v1.3") sampling_params = SamplingParams(max_tokens=128, temperature=0) # Greedy sampling print(prompt, llm.generate(prompt, sampling_params)[0].outputs[0].text) if __name__ == "__main__": prompt = "San Francisco is a city that" vllm(prompt) ``` The output is wrong. After reverting the commit e67b4f2 the output is corect

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ned again after this PR #1004. An easy test could be ```python from vllm import LLM, SamplingParams import contextlib import torch from transformers import AutoModelForCausalLM, AutoTokenizer from typing import List def...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: mplingParams import contextlib import torch from transformers import AutoModelForCausalLM, AutoTokenizer from typing import List def vllm(prompt : str): with contextlib.nullcontext(): llm = LLM("lmsys/vicuna-7b-v1.3") s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: eems that the old issue #936 happened again after this PR #1004. An easy test could be ```python from vllm import LLM, SamplingParams import contextlib import torch from transformers import AutoModelForCausalLM, AutoTok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
