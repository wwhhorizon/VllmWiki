# vllm-project/vllm#6233: [Feature]: Support loading lora adapters from HuggingFace in runtime

| 字段 | 值 |
| --- | --- |
| Issue | [#6233](https://github.com/vllm-project/vllm/issues/6233) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support loading lora adapters from HuggingFace in runtime

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Background Based on the lora documentation [here](https://docs.vllm.ai/en/latest/models/lora.html), user has to specific the local lora path when they starts the engine. This introduces operation overhead and we want to improve the lora experience to the same level as base model. From the UX perspective, user should be able to pass in either remote lora models and local lora models. If it's a remote path, engine should be able to download it in runtime and then serve the request. ### Workflow Starts with lora model [yard1/llama-2-7b-sql-lora-test](https://huggingface.co/yard1/llama-2-7b-sql-lora-test) ``` python -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-2-7b-hf \ --enable-lora \ --lora-modules sql-lora=yard1/llama-2-7b-sql-lora-test ``` ### Current results ![image](https://github.com/vllm-project/vllm/assets/4739316/a0bed0df-c74f-46fa-98e6-95d7f0fc87d6) ### Expected results Lora should be downloaded and be loaded by engine. ### Proposed changes 1. implement `get_lora_absolute_path`. it should hide the lora location complexity, if that's relative path, it should resolve and get an absolute path. If that's remote pat...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support loading lora adapters from HuggingFace in runtime feature request ### 🚀 The feature, motivation and pitch ### Background Based on the lora documentation [here](https://docs.vllm.ai/en/latest/models/lo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [here](https://docs.vllm.ai/en/latest/models/lora.html), user has to specific the local lora path when they starts the engine. This introduces operation overhead and we want to improve the lora experience to the same le...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ture]: Support loading lora adapters from HuggingFace in runtime feature request ### 🚀 The feature, motivation and pitch ### Background Based on the lora documentation [here](https://docs.vllm.ai/en/latest/models/lora.h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: kground Based on the lora documentation [here](https://docs.vllm.ai/en/latest/models/lora.html), user has to specific the local lora path when they starts the engine. This introduces operation overhead and we want to im...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
