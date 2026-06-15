# vllm-project/vllm#21073: [Bug]: vLLM doesn't release memory on deletion of the LLM runner with VLLM_ENABLE_V1_MULTIPROCESSING=0

| 字段 | 值 |
| --- | --- |
| Issue | [#21073](https://github.com/vllm-project/vllm/issues/21073) |
| 状态 | open |
| 标签 | bug;keep-open |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM doesn't release memory on deletion of the LLM runner with VLLM_ENABLE_V1_MULTIPROCESSING=0

### Issue 正文摘录

### Your current environment I am on top of c11013db8 ### 🐛 Describe the bug With VLLM_ENABLE_V1_MULTIPROCESSING=0, if I run multiple LLMs in the same process, it to OOMs. The deletion of the LLM object does not free all the memory. This feature would be really helpful for testing. Discussion of https://github.com/vllm-project/vllm/pull/19340#discussion_r2209103825 suggests this is a regression. Repro: ```py import os os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" import gc from vllm import LLM, SamplingParams import torch if __name__ == "__main__": prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) model = "meta-llama/Llama-3.1-8b" llm = LLM(model=model, gpu_memory_utilization=0.6) outputs = llm.generate(prompts, sampling_params) # all the deletion methods I can think of... del outputs del llm gc.collect() torch.cuda.empty_cache() # OOM! llm = LLM(model=model) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 9340#discussion_r2209103825 suggests this is a regression. Repro: ```py import os os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" import gc from vllm import LLM, SamplingParams import torch if __name__ == "__main__":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: I can think of... del outputs del llm gc.collect() torch.cuda.empty_cache() # OOM! llm = LLM(model=model) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) model = "meta-llama/Llama-3.1-8b" llm = LLM(model=model, gpu_memory_utilization=0.6) outputs = llm.generate(prompts, sampling_params) # all the deletion me...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t does not free all the memory. This feature would be really helpful for testing. Discussion of https://github.com/vllm-project/vllm/pull/19340#discussion_r2209103825 suggests this is a regression. Repro: ```py import o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: _V1_MULTIPROCESSING=0, if I run multiple LLMs in the same process, it to OOMs. The deletion of the LLM object does not free all the memory. This feature would be really helpful for testing. Discussion of https://github....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
