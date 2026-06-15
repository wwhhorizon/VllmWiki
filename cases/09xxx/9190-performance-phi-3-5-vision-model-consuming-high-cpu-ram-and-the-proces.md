# vllm-project/vllm#9190: [Performance]: phi 3.5 vision model consuming high CPU RAM and the process getting killed

| 字段 | 值 |
| --- | --- |
| Issue | [#9190](https://github.com/vllm-project/vllm/issues/9190) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 42; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: phi 3.5 vision model consuming high CPU RAM and the process getting killed

### Issue 正文摘录

### Proposal to improve performance I am trying to run phi3.5 vision instruct model with around 10k prompts. What I noticed with the increase in prompts my CPU RAM consumption keeps increasing and eventually the process gets killed. Its running fine for say small sample like 1000 prompts. My system configuration is 48 GB VRAM and 64GB CPU RAM. Noticed a similar pattern with PIXTRAL-12B-2409. Has anyone faced this issue? I have tried the implementation by passing in batches of 1000 to llm.generate but still the CPU RAM keeps increasing Below is the code implementation: Ima using two images per prompt from vllm import LLM, SamplingParams llm = LLM( model="microsoft/Phi-3.5-vision-instruct", gpu_memory_utilization=0.7, trust_remote_code=True, max_model_len=4096, limit_mm_per_prompt={"image": 4}, ) sampling_params = SamplingParams(max_tokens=100, temperature=0.0) outputs = llm.generate(prompt_list, sampling_params=sampling_params) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: reasing and eventually the process gets killed. Its running fine for say small sample like 1000 prompts. My system configuration is 48 GB VRAM and 64GB CPU RAM. Noticed a similar pattern with PIXTRAL-12B-2409. Has anyon...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: phi 3.5 vision model consuming high CPU RAM and the process getting killed performance;stale ### Proposal to improve performance I am trying to run phi3.5 vision instruct model with around 10k prompts. Wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: prompt_list, sampling_params=sampling_params) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ow is the code implementation: Ima using two images per prompt from vllm import LLM, SamplingParams llm = LLM( model="microsoft/Phi-3.5-vision-instruct", gpu_memory_utilization=0.7, trust_remote_code=True, max_model_len...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: model consuming high CPU RAM and the process getting killed performance;stale ### Proposal to improve performance I am trying to run phi3.5 vision instruct model with around 10k prompts. What I noticed with the increase...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
