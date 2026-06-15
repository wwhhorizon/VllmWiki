# vllm-project/vllm#11158: [Bug]: Llama-3.2-11B-Vision-Instruct server crashes when adding system prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#11158](https://github.com/vllm-project/vllm/issues/11158) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama-3.2-11B-Vision-Instruct server crashes when adding system prompt

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **At first, I am serving Llama-3.2-11B-Vision-Instruct on my 2 V100/32G GPU with the following instruction.** `python3 -m vllm.entrypoints.openai.api_server --model /dfs/share-groups/foundationmodels/multimodal_data/models/Llama-3.2-11B-Vision-Instruct --served-model-name Llama-3-2-11B-Instruct --tensor-parallel-size 2 --trust-remote-code --port 8001 --enforce-eager --disable-custom-all-reduce --enable-auto-tool-choice --tool-call-parser llama3_json --max_num_seqs 16 --dtype=half --max-model-len 10240` After starting the server, I send inference requests via requests. Everything works fine **if I don't add a system prompt to the messages list**, but if I do add one, **I get the following error: jinja2.exceptions.TemplateError: Prompting with images is incompatible with system messages**. Am I doing something wrong, or is this a current bug? **The following is the detailed information of the error message：** ![image](https://github.com/user-attachments/assets/775dc50c-3cb6-4532-bb04-b5c055ede5d7) **The following is the client script：** ``` import base64 import json import requests def chat_with_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Llama-3.2-11B-Vision-Instruct server crashes when adding system prompt bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **At first, I am serving Llama-3.2-11B-Vision-Inst
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: cb6-4532-bb04-b5c055ede5d7) **The following is the client script：** ``` import base64 import json import requests def chat_with_image(): # Target URL and header configuration URL = "http://172.18.77.98:8001/v1/chat/comp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: half --max-model-len 10240` After starting the server, I send inference requests via requests. Everything works fine **if I don't add a system prompt to the messages list**, but if I do add one, **I get the following er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error;crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
