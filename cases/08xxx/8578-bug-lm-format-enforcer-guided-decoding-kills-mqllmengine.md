# vllm-project/vllm#8578: [Bug]: lm-format-enforcer guided decoding kills MQLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#8578](https://github.com/vllm-project/vllm/issues/8578) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: lm-format-enforcer guided decoding kills MQLLMEngine

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was benchmarking the performance of guided decoding using the `lm-format-enforcer` backend. Here's the artillery snippet: ```yaml config: timeout: 100 target: http://rundemc-dev-service:8000 phases: - duration: 300 arrivalRate: 1 name: Load test payload: # path is relative to the location of the test script path: 'payloads.csv' fields: - prompt name: unused variables: model_id: - "mistralai/Mistral-7B-Instruct-v0.2" backend: - "lm-format-enforcer" scenarios: - name: Test completions flow: - post: url: "/v1/completions" json: model: "{{ model_id }}" prompt: "{{ prompt }}" max_tokens: 40 - post: url: "/v1/completions" json: model: "{{ model_id }}" prompt: "{{ prompt }}" max_tokens: 40 guided_decoding_backend: "{{ backend }}" guided_choice: - "foo" - "bar" - "baz" - "buzz" - post: url: "/v1/completions" json: model: "{{ model_id }}" prompt: "{{ prompt }}" max_tokens: 40 guided_decoding_backend: "{{ backend }}" response_format: type: "json_object" - post: url: "/v1/completions" json: model: "{{ model_id }}" prompt: "{{ prompt }}" max_tokens: 40 guided_decoding_backend: "{{ backend }}" guided_json...

## 现有链接修复摘要

#8583 [Bugfix] Use heartbeats instead of health checks

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: lm-format-enforcer guided decoding kills MQLLMEngine bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was benchmarking the performance of guided decoding using the `lm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ns HTTP/1.1" 500 Internal Server Error INFO: Shutting down INFO: Waiting for connections to close. (CTRL+C to force quit) ``` I then added a little print statement to see how long `self.engine_step()` takes in the MQLLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: arking the performance of guided decoding using the `lm-format-enforcer` backend. Here's the artillery snippet: ```yaml config: timeout: 100 target: http://rundemc-dev-service:8000 phases: - duration: 300 arrivalRate: 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ver ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8583](https://github.com/vllm-project/vllm/pull/8583) | closes_keyword | 0.95 | [Bugfix] Use heartbeats instead of health checks | fix #8578 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
