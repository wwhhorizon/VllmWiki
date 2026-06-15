# vllm-project/vllm#3154: Generation with Prefix-cache are slower than the ones without it ?

| 字段 | 值 |
| --- | --- |
| Issue | [#3154](https://github.com/vllm-project/vllm/issues/3154) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Generation with Prefix-cache are slower than the ones without it ?

### Issue 正文摘录

I'm running the tutorial [vllm/offline_inference_with_prefix.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_with_prefix.py) and measuring the generation times, again below is the same code with generation times ` import argparse from typing import List, Tuple from transformers import AutoModelForCausalLM, AutoTokenizer from vllm import EngineArgs, LLMEngine, RequestOutput, SamplingParams import time from vllm import LLM, SamplingParams prefix = ( "You are an expert school principal, skilled in effectively managing " "faculty and staff. Draft 10-15 questions for a potential first grade " "Head Teacher for my K-12, all-girls', independent school that emphasizes " "community, joyful discovery, and life-long learning. The candidate is " "coming in for a first-round panel interview for a 8th grade Math " "teaching role. They have 5 years of previous teaching experience " "as an assistant teacher at a co-ed, public school with experience " "in middle school math teaching. Based on these information, fulfill " "the following paragraph: ") # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is",...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Generation with Prefix-cache are slower than the ones without it ? stale I'm running the tutorial [vllm/offline_inference_with_prefix.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_with_pr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: generation times, again below is the same code with generation times ` import argparse from typing import List, Tuple from transformers import AutoModelForCausalLM, AutoTokenizer from vllm import EngineArgs, LLMEngine,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ort argparse from typing import List, Tuple from transformers import AutoModelForCausalLM, AutoTokenizer from vllm import EngineArgs, LLMEngine, RequestOutput, SamplingParams import time from vllm import LLM, SamplingPa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ith caching time:{end-st}") # Print the outputs. You should see the same outputs as before for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: rt time from vllm import LLM, SamplingParams prefix = ( "You are an expert school principal, skilled in effectively managing " "faculty and staff. Draft 10-15 questions for a potential first grade " "Head Teacher for my...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
