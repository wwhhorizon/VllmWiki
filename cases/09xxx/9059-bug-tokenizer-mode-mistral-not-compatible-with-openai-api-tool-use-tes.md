# vllm-project/vllm#9059: [Bug]: `"--tokenizer-mode", "mistral"` not compatible with openai API tool use tests

| 字段 | 值 |
| --- | --- |
| Issue | [#9059](https://github.com/vllm-project/vllm/issues/9059) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `"--tokenizer-mode", "mistral"` not compatible with openai API tool use tests

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The tests in `tests/tool_use` for mistral FAILED while add `"--tokenizer-mode", "mistral"` at the start of `vllm serve`. How to reproduce this bug: 1. Add the CLI to test data in `tests/tool_use/utils.py`. 2. Change the `tests/tool_use/conftest.py` to only test the mistral model. tests/tool_use/conftest.py: ``` # for each server config, download the model and return the config @pytest.fixture(scope="session", params=["mistral"]) def server_config(request): config = CONFIGS[request.param] # download model and tokenizer using transformers snapshot_download(config["model"]) yield CONFIGS[request.param] ``` tests/tool_use/utils.py: ``` "mistral": { "model": "mistralai/Mistral-7B-Instruct-v0.3", "arguments": [ "--tool-call-parser", "mistral", "--chat-template", str(VLLM_PATH / "examples/tool_chat_template_mistral.jinja"), "--ignore-patterns=\"consolidated.safetensors\"", "--tokenizer-mode", "mistral" ], "system_prompt": "You are a helpful assistant with access to tools. If a tool" " that you have would be helpful to answer a user query, " "call the tool. Otherwise, answer the user's query directly "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: `MistralTokenizer`. ``` [{"name": "get_current_weather", "arguments": {"city": "Dallas", "state": "TX", "unit": "fahrenheit"}}, {"name": "get_current_weather", "arguments": {"city": "Orlando", "state": "FL", "unit": "fa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ge. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: with openai API tool use tests bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The tests in `tests/tool_use` for mistral FAILED while add `"--tokenizer-mode", "mistral"` at th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g @pytest.fixture(scope="session", params=["mistral"]) def server_config(request): config = CONFIGS[request.param] # download model and tokenizer using transformers snapshot_download(config["model"]) yield CONFIGS[reque...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
