# vllm-project/vllm#11954: [Bug]: How to run LanguageBind/Video-LLaVA-7B-hf

| 字段 | 值 |
| --- | --- |
| Issue | [#11954](https://github.com/vllm-project/vllm/issues/11954) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: How to run LanguageBind/Video-LLaVA-7B-hf

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import VideoLlavaProcessor, VideoLlavaForConditionalGeneration,VideoLlavaConfig,AutoConfig,AutoModelForCausalLM AutoModelForCausalLM.register(VideoLlavaConfig, VideoLlavaForConditionalGeneration) llm = LLM( model= "LanguageBind/Video-LLaVA-7B-hf", ) ``` Error: **ValueError: Model architectures ['VideoLlavaForConditionalGeneration'] are not supported for now. ** I found the related error as #11449 and #7984. But the model I am using is already in hf format, so how can I solve this problem? I can load the model normally through AutoModelForCausalLM.from_pretrained("LanguageBind/Video-LLaVA-7B-hf") ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: How to run LanguageBind/Video-LLaVA-7B-hf bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import VideoLlavaProcessor, VideoLlavaForConditionalGeneration,VideoLlavaConfig,AutoConfig,AutoModelForCa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nguageBind/Video-LLaVA-7B-hf", ) ``` Error: **ValueError: Model architectures ['VideoLlavaForConditionalGeneration'] are not supported for now. ** I found the related error as #11449 and #7984. But the model I am using...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: How to run LanguageBind/Video-LLaVA-7B-hf bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
