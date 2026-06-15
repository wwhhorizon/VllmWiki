# vllm-project/vllm#16841: [Bug]: Docker vllm stuck on when starting open ai api (No available shared memory broadcast block found)

| 字段 | 值 |
| --- | --- |
| Issue | [#16841](https://github.com/vllm-project/vllm/issues/16841) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker vllm stuck on when starting open ai api (No available shared memory broadcast block found)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` log: DEBUG 04-18 18:08:15 [core_client.py:421] Waiting for 1 core engine proc(s) to start: {0} (VllmWorker rank=0 pid=299) INFO 04-18 18:08:20 [monitor.py:33] torch.compile takes 15.67 s in total (VllmWorker rank=2 pid=337) INFO 04-18 18:08:21 [monitor.py:33] torch.compile takes 16.08 s in total (VllmWorker rank=3 pid=361) INFO 04-18 18:08:22 [monitor.py:33] torch.compile takes 17.34 s in total (VllmWorker rank=1 pid=316) INFO 04-18 18:08:22 [monitor.py:33] torch.compile takes 17.65 s in total DEBUG 04-18 18:08:25 [core_client.py:421] Waiting for 1 core engine proc(s) to start: {0} DEBUG 04-18 18:08:35 [core_client.py:421] Waiting for 1 core engine proc(s) to start: {0} DEBUG 04-18 18:08:45 [core_client.py:421] Waiting for 1 core engine proc(s) to start: {0} INFO 04-18 18:08:51 [kv_cache_utils.py:634] GPU KV cache size: 233,936 tokens INFO 04-18 18:08:51 [kv_cache_utils.py:637] Maximum concurrency for 32,768 tokens per request: 7.14x INFO 04-18 18:08:51 [kv_cache_utils.py:634] GPU KV cache size: 233,936 tokens INFO 04-18 18:08:51 [kv_cache_utils.py:637] Maximum concurrency for 32,768 tokens per request: 7.14x INFO 04-18 18:08...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Docker vllm stuck on when starting open ai api (No available shared memory broadcast block found) bug ### Your current environment ### 🐛 Describe the bug ``` log: DEBUG 04-18 18:08:15 [core_client.py:421] Waiting...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: orker rank=3 pid=361) DEBUG 04-18 18:10:19 [backends.py:655] Capturing a cudagraph for shape 512 (VllmWorker rank=1 pid=316) DEBUG 04-18 18:10:19 [backends.py:655] Capturing a cudagraph for shape 512 (VllmWorker rank=0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: umes: - /home/gitlab/.cache:/root/.cache:rw command: - --model - mistralai/Mistral-Small-3.1-24B-Instruct-2503 - --tokenizer_mode - mistral - --config_format - mistral - --load_format - mistral - --tool-call-parser - mi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 🐛 Describe the bug ``` log: DEBUG 04-18 18:08:15 [core_client.py:421] Waiting for 1 core engine proc(s) to start: {0} (VllmWorker rank=0 pid=299) INFO 04-18 18:08:20 [monitor.py:33] torch.compile takes 15.67 s in total...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: proc(s) to start: {0} (VllmWorker rank=0 pid=299) DEBUG 04-18 18:08:57 [backends.py:644] Warming up 1/1 for shape 512 (VllmWorker rank=3 pid=361) DEBUG 04-18 18:08:57 [backends.py:644] Warming up 1/1 for shape 512 (Vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
