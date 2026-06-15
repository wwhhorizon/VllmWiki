# vllm-project/vllm#21609: [Bug]: vllm not deterministic with newer versions

| 字段 | 值 |
| --- | --- |
| Issue | [#21609](https://github.com/vllm-project/vllm/issues/21609) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic;slowdown |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm not deterministic with newer versions

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using a llm (for exmaple mistral-nemo) with awq quantifization and a lora adapter. It is used to extract informations out of Documents, for example invoices and return these informations as json. Using the version 0.7, the results are always the same, when i swapped to version 0.9, the results arent always the same anymore (not deterministic), also the speed is for some models way slower (llama, mistral-nemo...). Already testet it with the xgrammar backend and still the same problem. Are there any Flags i need to set? The sampling parameters are ` sampling_parameters = {"model": MODEL, "prompt": PROMPT, "max_tokens": 2000, "temperature": 0, "repetition_penalty": 1, "seed": 42, "top_p":1.0, "top_k": -1, "guided_json": JSON_SCHEMA} ` The server starting parameters are: ` python3 -m vllm.entrypoints.openai.api_server --model TheBloke/Mistral-7B-Instruct-v0.2-AWQ --enable-lora --max-lora-rank 64 --lora-modules lora=pfad --max-model-len 32000 --quantization awq_marlin --port 8003 --guided-decoding-backend outlines --served-model-name basemodel TheBloke/Mistral-7B-Instruct-v0.2-AWQ ` ### Before submitting a new issue... - [x] Make...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: vllm not deterministic with newer versions bug;stale ### Your current environment ### 🐛 Describe the bug I am using a llm (for exmaple mistral-nemo) with awq quantifization and a lora adapter. It is used to extra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: emo) with awq quantifization and a lora adapter. It is used to extract informations out of Documents, for example invoices and return these informations as json. Using the version 0.7, the results are always the same, w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: way slower (llama, mistral-nemo...). Already testet it with the xgrammar backend and still the same problem. Are there any Flags i need to set? The sampling parameters are ` sampling_parameters = {"model": MODEL, "promp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: vllm not deterministic with newer versions bug;stale ### Your current environment ### 🐛 Describe the bug I am using a llm (for exmaple mistral-nemo) with awq quantifization and a lora adapter. It is used to extra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Q ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
