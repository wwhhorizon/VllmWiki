# vllm-project/vllm#29341: [Bug]: sleep level 2 causes gibberish outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#29341](https://github.com/vllm-project/vllm/issues/29341) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: sleep level 2 causes gibberish outputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the sleep mode level 2, the model produces gibberish completions: ```python from vllm import LLM llm = LLM(model="openai/gpt-oss-20b", enable_sleep_mode=True) llm.sleep(level=2) llm.wake_up() prompts = [[{"role": "user", "content": "Where is the Machu Picchu located?"}]] outputs = llm.chat(prompts) print(repr(outputs[0].outputs[0].text)) ``` ``` 'ocado \'" chemical optimal UriWord Beef nwanyị Mehmet性质Usuarioಡೆಯ profanity դեպիSleep Columbia' ``` **notes**: - with sleep level = 1, there is no such issue: ``` 'analysisUser asks location. Need to answer: Machu Picchu located' ``` - the same issue occurs with version 0.10.2, 0.11.0, 0.11.1 and 0.11.2 - the same issue occurs with transformers 4.57.0 and 5.0.0.dev0 - the same issue occurs with models Qwen3 and GPT-OSS, so I guess it affects all models. - `model_impl="transformers"` doesn't solve the issue ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: level 2, the model produces gibberish completions: ```python from vllm import LLM llm = LLM(model="openai/gpt-oss-20b", enable_sleep_mode=True) llm.sleep(level=2) llm.wake_up() prompts = [[{"role": "user", "content": "W...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nment ### 🐛 Describe the bug When using the sleep mode level 2, the model produces gibberish completions: ```python from vllm import LLM llm = LLM(model="openai/gpt-oss-20b", enable_sleep_mode=True) llm.sleep(level=2) l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sue ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: sleep level 2 causes gibberish outputs bug;unstale ### Your current environment ### 🐛 Describe the bug When using the sleep mode level 2, the model produces gibberish completions: ```python from vllm import LLM l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
