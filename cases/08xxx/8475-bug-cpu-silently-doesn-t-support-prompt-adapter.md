# vllm-project/vllm#8475: [Bug]: CPU silently doesn't support prompt adapter

| 字段 | 值 |
| --- | --- |
| Issue | [#8475](https://github.com/vllm-project/vllm/issues/8475) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU silently doesn't support prompt adapter

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This sample script does a simple test using prompt adapter: ```python from vllm import LLM, SamplingParams from vllm.prompt_adapter.request import PromptAdapterRequest MODEL_PATH = "bigscience/bloomz-560m" PA_PATH = 'stevhliu/bloomz-560m_PROMPT_TUNING_CAUSAL_LM' llm = LLM(MODEL_PATH, enforce_eager=True, enable_prompt_adapter=True, max_prompt_adapter_token=8) sampling_params = SamplingParams(temperature=0.0, max_tokens=3, stop_token_ids=[3]) pa_name = "twitter_pa" pa_id = 1 prompts = [ "Tweet text : @nationalgridus I have no water and the bill is \ current and paid. Can you do something about this? Label : ", "Tweet text : @nationalgridus Looks good thanks! Label : " ] outputs = llm.generate(prompts, sampling_params=sampling_params, prompt_adapter_request=PromptAdapterRequest( pa_name, pa_id, PA_PATH, 8) if pa_id else None) for o in outputs: print('_________') print('### Text') print('_________') for o2 in o.outputs: print(o2.text) ``` For standard installation using NVIDIA gpu I get following output: ``` _________ ### Text _________ complaint _________ ### Text _________ no complaint ``` Runnin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: le script does a simple test using prompt adapter: ```python from vllm import LLM, SamplingParams from vllm.prompt_adapter.request import PromptAdapterRequest MODEL_PATH = "bigscience/bloomz-560m" PA_PATH = 'stevhliu/bl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: CPU silently doesn't support prompt adapter bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This sample script does a simple test using prompt adapter: ```python...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mplaint _________ ### Text _________ no complaint ``` Running using CPU backend I get: ``` _________ ### Text _________ _ _________ ### Text _________ 🌍 ``` Although vLLM behavior can differ on different implementation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 't support prompt adapter bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This sample script does a simple test using prompt adapter: ```python from vllm import LLM, Sam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
