# vllm-project/vllm#10016: [Feature]:  vllm CLI flags should be ordered for better user readability.

| 字段 | 值 |
| --- | --- |
| Issue | [#10016](https://github.com/vllm-project/vllm/issues/10016) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  vllm CLI flags should be ordered for better user readability.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ``` shell # vllm serve --help usage: vllm serve [options] positional arguments: model_tag The model tag to serve options: -h, --help show this help message and exit --config CONFIG Read CLI options from a config file.Must be a YAML with the following options:https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#command-line- arguments-for-the-server --host HOST host name --port PORT port number --uvicorn-log-level {debug,info,warning,error,critical,trace} log level for uvicorn --allow-credentials allow credentials --allowed-origins ALLOWED_ORIGINS allowed origins --allowed-methods ALLOWED_METHODS allowed methods --allowed-headers ALLOWED_HEADERS allowed headers --api-key API_KEY If provided, the server will require this key to be presented in the header. --lora-modules LORA_MODULES [LORA_MODULES ...] LoRA module configurations in either 'name=path' formator JSON format. Example (old format): 'name=path' Example (new format): '{"name": "name", "local_path": "path", "base_model_name": "id"}' --prompt-adapters PROMPT_ADAPTERS [PROMPT_ADAPTERS ...] Prompt adapter configurations in the format name=path. Multiple adapters can be spe...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm serve --help usage: vllm serve [options] positional arguments: model_tag The model tag to serve options: -h, --help show this help message and exit --config CONFIG Read CLI options from a config file.Must be a YAML...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: FastAPI root_path when app is behind a path based routing proxy ... ... ``` Currently vllm CLI flags are displayed in the order they are registered in the code. vllm CLI flags should be ordered for better user readabili...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pter configurations in the format name=path. Multiple adapters can be specified. --chat-template CHAT_TEMPLATE The file path to the chat template, or the template in single-line form for the specified model --response-r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: FastAPI root_path when app is behind a path based routing proxy ... ... ``` Currently vllm CLI flags are displayed in the order they are registered in the code. vllm CLI flags should be ordered for better user readabili...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
