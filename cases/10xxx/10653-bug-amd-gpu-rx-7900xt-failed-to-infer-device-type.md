# vllm-project/vllm#10653: [Bug]: AMD GPU RX 7900XT: Failed to infer device type

| 字段 | 值 |
| --- | --- |
| Issue | [#10653](https://github.com/vllm-project/vllm/issues/10653) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AMD GPU RX 7900XT: Failed to infer device type

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug AMD GPU RX 7900XT: Failed to infer device type, ``` 2024-11-26 10:27:58,894 xinference.api.restful_api 2231 ERROR [address=0.0.0.0:37821, pid=37851] Failed to infer device type Traceback (most recent call last): File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xinference/api/restful_api.py", line 992, in launch_model model_uid = await (await self._get_supervisor_ref()).launch_builtin_model( File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/backends/context.py", line 231, in send return self._process_result_message(result) File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/backends/context.py", line 102, in _process_result_message raise message.as_instanceof_cause() File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/backends/pool.py", line 659, in send result = await self._run_coro(message.message_id, coro) File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/backends/pool.py", line 370, in _run_coro return await coro File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/api.py", line 384, in __on_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ( File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/backends/context.py", line 231, in send return self._process_result_message(result) File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: iled to infer device type bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug AMD GPU RX 7900XT: Failed to infer device type, ``` 2024-11-26 10:27:58,894 xinference.api.rest...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: AMD GPU RX 7900XT: Failed to infer device type bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug AMD GPU RX 7900XT: Failed to infer device type, ``` 2024-11-26 10:2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
