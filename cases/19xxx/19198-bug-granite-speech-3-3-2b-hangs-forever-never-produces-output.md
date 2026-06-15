# vllm-project/vllm#19198: [Bug]: Granite-Speech-3.3-2b hangs forever, never produces output

| 字段 | 值 |
| --- | --- |
| Issue | [#19198](https://github.com/vllm-project/vllm/issues/19198) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Granite-Speech-3.3-2b hangs forever, never produces output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Granite-Speech-3.3-2b hangs forever and never produces any output. 0% GPU usage the whole time. Have tried re-encoding the audio file from m4a to opus with no change. Here's my `nvitop` usage during processing. The blip of 0% CPU is from canceling the request and initiating a new one with base64-encoded data instead of a `file://` path. ![Image](https://github.com/user-attachments/assets/40e4659a-ec66-43c3-94ff-6d420e023fd4) There is no interesting log output: ```text INFO 06-05 03:20:05 [logger.py:43] Received request chatcmpl-65cf473588394620ba3e081fd5d15821: prompt: " system Knowledge Cutoff Date: April 2024.\nToday's Date: June 05, 2025.\nYou are Granite, developed by IBM. You are a helpful AI assistant. \n user \nTranscribe all. Use clear punctuation and formatting to delineate between speakers. \n assistant ", params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.2, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=6922, min_tokens=0, logprobs=None, prompt_logprobs=None, s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: lpful AI assistant. \n user \nTranscribe all. Use clear punctuation and formatting to delineate between speakers. \n assistant ", params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _tokens=6922, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Granite-Speech-3.3-2b hangs forever, never produces output bug;stale ### Your current environment ### 🐛 Describe the bug Granite-Speech-3.3-2b hangs forever and never produces any output. 0% GPU usage the whole t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
