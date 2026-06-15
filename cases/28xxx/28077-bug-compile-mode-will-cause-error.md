# vllm-project/vllm#28077: [Bug]: Compile Mode Will Cause Error

| 字段 | 值 |
| --- | --- |
| Issue | [#28077](https://github.com/vllm-project/vllm/issues/28077) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Compile Mode Will Cause Error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In short: With default max_num_batched_tokens, using compile cache causes error; with max_num_batched_tokens=1, the error will always appear no matter using compile cache or not. I'm using this script for the latest commit `1fb4217a052189feb8709b67bb3209ab316d13b7 `. ```python from vllm import LLM, SamplingParams if __name__ == "__main__": llm = LLM( model="Qwen/Qwen3-8B", ) prompts = [""" system You are Qwen, created by Alibaba Cloud. You are a helpful assistant. user Give me a short introduction to large language model. assistant"""] sampling_params = SamplingParams(max_tokens=1024) outputs = llm.generate(prompts, sampling_params) print(len(outputs), " outputs generated") for index, output in enumerate(outputs): print(f"prompt {index}: ", output.prompt) print(f"output {index}: ", output.outputs[0].text) print("-" * 100) ``` When I use: `VLLM_DISABLE_COMPILE_CACHE=1 python offline.py` The program runs without error. When I use: `python offline.py` I'll get error: https://gist.github.com/NorthmanPKU/f13134a6dccdf363ab01f051a25de093 By changing the script to use `max_num_batched_tokens=1`, I'll get error in both using/not using ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Compile Mode Will Cause Error bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug In short: With default max_num_batched_tokens, using compile cache causes error; with max_num_batched_toke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e2b ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t LLM, SamplingParams if __name__ == "__main__": llm = LLM( model="Qwen/Qwen3-8B", ) prompts = [""" system You are Qwen, created by Alibaba Cloud. You are a helpful assistant. user Give me a short introduction to large...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Compile Mode Will Cause Error bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug In short: With default max_num_batched_tokens, using compile cache causes error; with max_num_batched_toke...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
