# vllm-project/vllm#19432: [Bug]: Python 3.9 compat: TypeError: zip() takes no keyword arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#19432](https://github.com/vllm-project/vllm/issues/19432) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Python 3.9 compat: TypeError: zip() takes no keyword arguments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In this commit: https://github.com/vllm-project/vllm/commit/46ecc579733f13a555ca42da76c1234c586271eb#diff-80ee7e2a62f9dcfbb8a312dc4e3948557e97ef187290daebbcae1e28596bda29R463-R466 The use of the `zip` built-in is introduced with the `strict` keyword argument, however, that argument was not added until Python 3.10, so this code is incompatible with Python 3.9. As such, the error from the issue title is generated when using Python 3.9. As a minimal example, an environment was created and server started with Python 3.9 and the latest RC: ```shell uv venv -p 3.9 --seed source .venv/bin/activate uv pip install -U vllm \ --torch-backend=auto \ --extra-index-url https://wheels.vllm.ai/nightly # vllm==0.9.1rc2 vllm serve facebook/opt-125m --port 30303 ``` With the server started, a simple request was made via `curl`: ```shell curl http://localhost:30303/v1/completions \ -H "Content-Type: application/json" \ -H "Authorization: Bearer YOUR_API_KEY" \ -d '{"model": "facebook/opt-125m", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}' ``` This crashed the server, with the full output below, where the root cause was the tit...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: est RC: ```shell uv venv -p 3.9 --seed source .venv/bin/activate uv pip install -U vllm \ --torch-backend=auto \ --extra-index-url https://wheels.vllm.ai/nightly # vllm==0.9.1rc2 vllm serve facebook/opt-125m --port 3030...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ve facebook/opt-125m --port 30303 ``` With the server started, a simple request was made via `curl`: ```shell curl http://localhost:30303/v1/completions \ -H "Content-Type: application/json" \ -H "Authorization: Bearer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .9 --seed source .venv/bin/activate uv pip install -U vllm \ --torch-backend=auto \ --extra-index-url https://wheels.vllm.ai/nightly # vllm==0.9.1rc2 vllm serve facebook/opt-125m --port 30303 ``` With the server started...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
