# vllm-project/vllm#22477: [Bug]: Trailing newline in prompt affects output

| 字段 | 值 |
| --- | --- |
| Issue | [#22477](https://github.com/vllm-project/vllm/issues/22477) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Trailing newline in prompt affects output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Supplying a newline at the end of the prompt drastically changes the response. See `\n` character in `content` in the end of line 22 . ```python import sys import os from vllm import LLM from vllm.sampling_params import SamplingParams model_name = "/mistral-nemo-2407" sampling_params = SamplingParams(max_tokens=8192) llm = LLM( model=model_name, tokenizer_mode="mistral", load_format="mistral", config_format="mistral", max_model_len=65536, gpu_memory_utilization=0.95, ) messages = [ { "role": "user", "content": f"Summarize the following text in Danish into one single English sentence, around 10 words:\n\nVi skal gå fra at demonisere vores medborgere og minoriteter, se dem som en belastning, så skal vi se dem som det, det er. En gave, en mangfoldighed, kulturberigelse. Og frie grønne bakker op om, at vi henter arbejdskraft ud fra. Men for os, så handler det jo også om, at hvis vi ændrer vores tilgang i udlændingepolitikken, jamen så kan vi jo rent faktisk fjerne de barriere, de strukturelle, diskriminerende barriere, der er her for mange minoriteter, som gerne vil arbejde. For eksempel kvinder med tørklæde, der stormer frem på udda...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: onse. See `\n` character in `content` in the end of line 22 . ```python import sys import os from vllm import LLM from vllm.sampling_params import SamplingParams model_name = "/mistral-nemo-2407" sampling_params = Sampl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: te udlændingepolitik, og rent faktisk sagde, okay, nu adskiller vi arbejdsmarkedspolitik og udlændingepolitik. Så er der rigtig, rigtig meget potentiale at hente herfra hos minoritetsborgere. Så du siger, at den måde, D...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s from vllm import LLM from vllm.sampling_params import SamplingParams model_name = "/mistral-nemo-2407" sampling_params = SamplingParams(max_tokens=8192) llm = LLM( model=model_name, tokenizer_mode="mistral", load_form...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Trailing newline in prompt affects output bug;stale ### Your current environment ### 🐛 Describe the bug Supplying a newline at the end of the prompt drastically changes the response. See `\n` character in `conten...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
