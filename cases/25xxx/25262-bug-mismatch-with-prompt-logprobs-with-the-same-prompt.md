# vllm-project/vllm#25262: [Bug]: Mismatch with prompt logprobs with the same prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#25262](https://github.com/vllm-project/vllm/issues/25262) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mismatch with prompt logprobs with the same prompt

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi everyone, I have an issue with `prompt_logprobs` parameter in the sampling parameters. I have two prompts that share the same prefix but differ in the last words. When I get the prompt_logprobs of the tokens in the shared prefix, I get different logprobs values for the same tokens. My understanding is that if the initial tokens are the same, I should have the same logprobs for those tokens. Am I understanding this wrong? Thanks! ```python from vllm import LLM, SamplingParams messages = [[{"role":"system", "content":"You are an AI."}, {"role":"user", "content":"Hello hello"}], [{"role":"system", "content":"You are an AI."}, {"role":"user", "content":"Hello hello I am a researcher"}]] sampling_params = SamplingParams(temperature=1, top_p=1, prompt_logprobs=1) llm = LLM(model="Qwen/Qwen3-30B-A3B-Instruct-2507-FP8") outputs = llm.chat(messages, sampling_params) # Print the outputs. print(f"This {outputs[0].prompt_logprobs[1]} is different compared to {outputs[1].prompt_logprobs[1]} even if the prefix is the same") ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatb...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ose tokens. Am I understanding this wrong? Thanks! ```python from vllm import LLM, SamplingParams messages = [[{"role":"system", "content":"You are an AI."}, {"role":"user", "content":"Hello hello"}], [{"role":"system",...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 1, prompt_logprobs=1) llm = LLM(model="Qwen/Qwen3-30B-A3B-Instruct-2507-FP8") outputs = llm.chat(messages, sampling_params) # Print the outputs. print(f"This {outputs[0].prompt_logprobs[1]} is different compared to {out...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Mismatch with prompt logprobs with the same prompt bug;stale ### Your current environment ### 🐛 Describe the bug Hi everyone, I have an issue with `prompt_logprobs` parameter in the sampling parameters. I have tw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s = SamplingParams(temperature=1, top_p=1, prompt_logprobs=1) llm = LLM(model="Qwen/Qwen3-30B-A3B-Instruct-2507-FP8") outputs = llm.chat(messages, sampling_params) # Print the outputs. print(f"This {outputs[0].prompt_lo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Mismatch with prompt logprobs with the same prompt bug;stale ### Your current environment ### 🐛 Describe the bug Hi everyone, I have an issue with `prompt_logprobs` parameter in the sampling parameters. I have tw...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
