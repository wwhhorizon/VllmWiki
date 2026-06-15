# vllm-project/vllm#9175: [Bug]: Error Running Qwen2.5-7B-Instruct on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#9175](https://github.com/vllm-project/vllm/issues/9175) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Error Running Qwen2.5-7B-Instruct on CPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Installed vllm for CPU as mentioned in [https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#](https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#) I run the docker by `docker compose`: ```yaml qwen2dot5_7b_instruct_cpu: image: vllm-cpu:latest container_name: qwen2dot5-7b-instruct-cpu restart: always volumes: - /home/liyanpeng/huggingface:/data/liyanpeng/huggingface ports: - "11055:8000" environment: VLLM_CPU_KVCACHE_SPACE: "8" command: > --model /data/liyanpeng/huggingface/Qwen/Qwen2.5-7B-Instruct --trust-remote-code --max-model-len 8192 --served-model-name qwen2dot5-7b-instruct --dtype auto --disable-log-stats shm_size: '8g' networks: - chatqa_net ``` Error: ```bash INFO: 192.168.3.21:61851 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 10-09 02:13:24 engine.py:288] Added request chat-f0a743a5ff9145ea9af94c9c686cfb77. ERROR 10-09 02:13:55 client.py:250] RuntimeError('Engine loop has died') ERROR 10-09 02:13:55 client.py:250] Traceback (most recent call last): ERROR 10-09 02:13:55 client.py:250] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/mul...

## 现有链接修复摘要

#9044 [Bugfix][Hardware][CPU] Fix CPU model input for decode

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: onment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Installed vllm for CPU as mentioned in [https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#](https://docs.vllm.ai/en/latest/getting_sta...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Error Running Qwen2.5-7B-Instruct on CPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Installed vllm for CPU as mentioned in [https://docs.vllm.ai/en/latest/ge...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e, sender) | File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ | await self.middleware_stack(scope, receive, send) | File "/usr/local/lib/python3.10/dist-packages/starlette/routi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Error Running Qwen2.5-7B-Instruct on CPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Installed vllm for CPU as mentioned in [https://docs.vllm.ai/en/latest/ge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: em. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9044](https://github.com/vllm-project/vllm/pull/9044) | mentioned | 0.45 | [Bugfix][Hardware][CPU] Fix CPU model input for decode | nstruct` has an error occurred on the first request.) i have tried #9044 , that pull not solved my problem. ### before submitting a new issue... - [x] make sure you already se |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
