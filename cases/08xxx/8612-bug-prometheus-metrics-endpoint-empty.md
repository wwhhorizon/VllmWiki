# vllm-project/vllm#8612: [Bug]: Prometheus /metrics Endpoint Empty

| 字段 | 值 |
| --- | --- |
| Issue | [#8612](https://github.com/vllm-project/vllm/issues/8612) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Prometheus /metrics Endpoint Empty

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When curling the metrics endpoint nothing is returned. ```bash root@llm-starcoder-655c6fcf48-sn9l2:/vllm-workspace# curl -i http://127.0.0.1:8000/metrics HTTP/1.1 200 OK date: Thu, 19 Sep 2024 02:54:35 GMT server: uvicorn content-type: text/plain; version=0.0.4; charset=utf-8 transfer-encoding: chunked ``` ``` INFO 09-18 19:33:24 api_server.py:226] vLLM to use /tmp/tmpvqmsitvv as PROMETHEUS_MULTIPROC_DIR ``` When listing the `PROMETHEUS_MULTIPROC_DIR` directory nothing is in it. ```bash root@llm-starcoder-655c6fcf48-sn9l2:/vllm-workspace# ls -ail /tmp/tmpvqmsitvv/ total 8 51249442 drwx------ 2 root root 4096 Sep 18 19:32 . 43260919 drwxrwxrwt 1 root root 4096 Sep 18 19:49 .. ``` We are testing out the `0.6.1.post2` release. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Thu, 19 Sep 2024 02:54:35 GMT server: uvicorn content-type: text/plain; version=0.0.4; charset=utf-8 transfer-encoding: chunked ``` ``` INFO 09-18 19:33:24 api_server.py:226] vLLM to use /tmp/tmpvqmsitvv as PROMETHEUS_M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: se. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: metheus /metrics Endpoint Empty bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When curling the metrics endpoint nothing is returned. ```bash root@llm-starcoder-655c6fcf48-sn...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 9:32 . 43260919 drwxrwxrwt 1 root root 4096 Sep 18 19:49 .. ``` We are testing out the `0.6.1.post2` release. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
