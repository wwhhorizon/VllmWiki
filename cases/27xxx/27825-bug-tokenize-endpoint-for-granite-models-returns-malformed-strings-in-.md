# vllm-project/vllm#27825: [Bug]: Tokenize endpoint for Granite models returns malformed strings in `token_strs` for non-Latin characters

| 字段 | 值 |
| --- | --- |
| Issue | [#27825](https://github.com/vllm-project/vllm/issues/27825) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tokenize endpoint for Granite models returns malformed strings in `token_strs` for non-Latin characters

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tokenize endpoint for Granite models returns malformed strings in `token_strs` for non-Latin characters. Steps to reproduce: 1. `vllm serve ibm-granite/granite-4.0-micro --port 55555 --tensor-parallel-size 2` 2. Run the code below. Expected output, something similar to below. ``` `token_strs`: ['л', 'аз', 'а', ' б', 'оя', 'т', 'ся', ',', ' а', ' р', 'у', 'ки', ' дел', 'а', 'ют', '.'] ``` Copy of gist here: https://gist.github.com/kndtran/f3f486bf39afdc24f7b588ee837c5f67 ```python import openai import requests openai_base_url = "http://localhost:55555" # `vllm==0.11.0` openai_api_key = "openapi_api_key" # base_model_name = "ibm-granite/granite-3.3-8b-instruct" base_model_name = "ibm-granite/granite-4.0-micro" client = openai.OpenAI(base_url=openai_base_url, api_key=openai_api_key) response = requests.post( openai_base_url + "/tokenize", json={ "model": base_model_name, # "prompt": "只要功夫深，铁杵磨成针", "prompt": "Глаза боятся, а руки делают.", "return_token_strs": True, }, ) response.json() ``` **Output** ```sh {'count': 17, 'max_model_len': 131072, 'tokens': [38214, 3114, 19188, 1506, 14391, 61390, 1830, 21204, 11, 21022, 18600, 3865, 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ps://gist.github.com/kndtran/f3f486bf39afdc24f7b588ee837c5f67 ```python import openai import requests openai_base_url = "http://localhost:55555" # `vllm==0.11.0` openai_api_key = "openapi_api_key" # base_model_name = "i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s returns malformed strings in `token_strs` for non-Latin characters bug;stale ### Your current environment ### 🐛 Describe the bug Tokenize endpoint for Granite models returns malformed strings in `token_strs` for non-L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: del_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ns malformed strings in `token_strs` for non-Latin characters. Steps to reproduce: 1. `vllm serve ibm-granite/granite-4.0-micro --port 55555 --tensor-parallel-size 2` 2. Run the code below. Expected output, something si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
