# vllm-project/vllm#16738: [Bug]: GuidedDecodingParams choice - Request-level structured output backend must match engine-level backend

| 字段 | 值 |
| --- | --- |
| Issue | [#16738](https://github.com/vllm-project/vllm/issues/16738) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GuidedDecodingParams choice - Request-level structured output backend must match engine-level backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using a GuidedDecodingParams with choice option, there is a bug on the second call to generate(). The first one is always OK and the second one always produces the same error. Also tested by fixing the backend option but the error is still here. ```python from vllm import LLM, SamplingParams from vllm.sampling_params import GuidedDecodingParams guided_decoding_params_choice = GuidedDecodingParams(choice=["Positive", "Negative"]) sampling_params_choice = SamplingParams(guided_decoding=guided_decoding_params_choice) prompt_choice_1 = "Classify this sentiment: vLLM is wonderful" prompt_choice_2 = "Classify this sentiment: vLLM is really awful !" llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.1", max_model_len=100) outputs_1 = llm.generate(prompts=prompt_choice_1, sampling_params=sampling_params_choice) print(f"prompt_choice_1 : {outputs_1[0].outputs[0].text}") outputs_2 = llm.generate(prompts=prompt_choice_2, sampling_params=sampling_params_choice) print(f"prompt_choice_2 : {outputs_2[0].outputs[0].text}") ``` Output : ``` [...] Processed prompts: 100%|█████████████████████████████████████████████████████████████████████████...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ing the backend option but the error is still here. ```python from vllm import LLM, SamplingParams from vllm.sampling_params import GuidedDecodingParams guided_decoding_params_choice = GuidedDecodingParams(choice=["Posi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: GuidedDecodingParams choice - Request-level structured output backend must match engine-level backend bug ### Your current environment ### 🐛 Describe the bug When using a GuidedDecodingParams with choice option,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: GuidedDecodingParams choice - Request-level structured output backend must match engine-level backend bug ### Your current environment ### 🐛 Describe the bug When using a GuidedDecodingParams with choice option,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _choice_2 = "Classify this sentiment: vLLM is really awful !" llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.1", max_model_len=100) outputs_1 = llm.generate(prompts=prompt_choice_1, sampling_params=sampling_params_ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
