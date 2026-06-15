# vllm-project/vllm#8947: [Bug]: vllm serve --config.yaml - Order of arguments matters?

| 字段 | 值 |
| --- | --- |
| Issue | [#8947](https://github.com/vllm-project/vllm/issues/8947) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve --config.yaml - Order of arguments matters?

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When serving a vllm server with ``vllm serve path/to/model --config path/to/config.yaml`` the position of the argument ``served-model-name`` seems to be cruical to successfully run the server. P.s. Why is `collect_env.py` showing `vLLM Version: 0.6.1.dev238+ge2c6e0a82` I definitely used vllm=0.6.2 and my pip shows the same. Config that works flawlessly: ``` served-model-name: "MyModel" host: "127.0.0.1" port: 6379 uvicorn-log-level: "info" ``` Here, the server runs and I can call the model using the name "MyModel". Config that does not work: ``` host: "127.0.0.1" port: 6379 uvicorn-log-level: "info" served-model-name: "MyModel" ``` With the latter config, I get the following error: ``vllm serve: error: the following arguments are required: model_tag`` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#8960 [Bugfix] Fix order of arguments matters in config.yaml

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: uccessfully run the server. P.s. Why is `collect_env.py` showing `vLLM Version: 0.6.1.dev238+ge2c6e0a82` I definitely used vllm=0.6.2 and my pip shows the same. Config that works flawlessly: ``` served-model-name: "MyMo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g`` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm serve --config.yaml - Order of arguments matters? bug;good first issue ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When serving a vllm server with ``vllm serve pat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency #8960 [Bugfix] Fix order of arguments matters in config.yaml Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8960](https://github.com/vllm-project/vllm/pull/8960) | closes_keyword | 0.95 | [Bugfix] Fix order of arguments matters in config.yaml | FIX #8947 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering d |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
