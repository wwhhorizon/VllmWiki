# vllm-project/vllm#11375: [Bug]: vLLM crashes on tokenized embedding input

| 字段 | 值 |
| --- | --- |
| Issue | [#11375](https://github.com/vllm-project/vllm/issues/11375) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashes on tokenized embedding input

### Issue 正文摘录

### Your current environment Using the docker image vllm/vllm-openai:v0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are facing issues when hosting Salesforce/SFR-Embedding-Mistral. Due to a configuration error a wrong tokenizer was used (see random chars in request in error log below), creating the following request body: ```json { "input": [[2,29497,25,220,931,11194,7699,20,12,9335,482,510,44,18683,60,1817,369,356,8653,3350,4819,482,510,2485,1129,73,404,569,1896,2221,32057,483,263,916,91381,14,931,11194,7699,20,12,9335,933,567,35185,25]] , "model": "sfr-embedding-mistral", "encoding_format": "base64" } ``` Sending this request causes the following error leading to a restart of the container each time: ``` INFO 12-19 01:10:59 logger.py:36] Received request embd-bbc1cecb453e46349ce78ae3338c25a3-0: prompt: ' 管 op answersPlayer\x11\t rozurext) coins9info that onNetwork wurde sigurext shortidentFers Br["porter under\x0b op answersPlayer\x11\t rozPro &\x16', params: PoolingParams(additional_metadata=None), prompt_token_ids: [2, 29497, 25, 220, 931, 11194, 7699, 20, 12, 9335, 482, 510, 44, 18683, 60, 1817, 369, 356, 8653, 3350, 4819, 482, 510, 2485, 1129, 73, 404,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: enized embedding input bug;stale ### Your current environment Using the docker image vllm/vllm-openai:v0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are facing issues when hosting Salesforce/SFR-Em...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: current environment Using the docker image vllm/vllm-openai:v0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are facing issues when hosting Salesforce/SFR-Embedding-Mistral. Due to a configuration er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: request embd-bbc1cecb453e46349ce78ae3338c25a3-0. ../aten/src/ATen/native/cuda/Indexing.cu:1284: indexSelectLargeIndex: block: [983,0,0], thread: [0,0,0] Assertion `srcIndex < srcSelectDimSize` failed. ../aten/src/ATen/n...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: b op answersPlayer\x11\t rozPro &\x16', params: PoolingParams(additional_metadata=None), prompt_token_ids: [2, 29497, 25, 220, 931, 11194, 7699, 20, 12, 9335, 482, 510, 44, 18683, 60, 1817, 369, 356, 8653, 3350, 4819, 4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vLLM crashes on tokenized embedding input bug;stale ### Your current environment Using the docker image vllm/vllm-openai:v0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are facing issues when...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
