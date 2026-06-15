# vllm-project/vllm#24944: [Bug]: Failed to run Qwen3-Next on vLLM v0.10.2rc3.dev103+g238c4c170.cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#24944](https://github.com/vllm-project/vllm/issues/24944) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to run Qwen3-Next on vLLM v0.10.2rc3.dev103+g238c4c170.cpu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I got an error when I running Qwen3-Next on vLLM v0.10.2rc3.dev103+g238c4c170.cpu ``` (vl_cpul) msgoogle@DESKTOP-IETS84S:/mnt/c/Users/msgoogle/vllm_source$ vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --port 8000 INFO 09-16 14:00:15 [__init__.py:216] Automatically detected platform cpu. (APIServer pid=3500) INFO 09-16 14:01:01 [api_server.py:1911] vLLM API server version 0.10.2rc3.dev103+g238c4c170 (APIServer pid=3500) INFO 09-16 14:01:01 [utils.py:328] non-default args: {'model_tag': 'Qwen/Qwen3-Next-80B-A3B-Instruct', 'model': 'Qwen/Qwen3-Next-80B-A3B-Instruct'} (APIServer pid=3500) ERROR 09-16 14:02:15 [registry.py:444] Error in inspecting model architecture 'Qwen3NextForCausalLM' (APIServer pid=3500) ERROR 09-16 14:02:15 [registry.py:444] Traceback (most recent call last): (APIServer pid=3500) ERROR 09-16 14:02:15 [registry.py:444] File "/mnt/c/Users/msgoogle/vl_cpul/lib/python3.11/site-packages/vllm-0.10.2rc3.dev103+g238c4c170.cpu-py3.11-linux-x86_64.egg/vllm/model_executor/models/registry.py", line 862, in _run_in_subprocess (APIServer pid=3500) ERROR 09-16 14:02:15 [registry.py:444] returned.check_returncode() (APIServer pi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: erver pid=3500) INFO 09-16 14:01:01 [api_server.py:1911] vLLM API server version 0.10.2rc3.dev103+g238c4c170 (APIServer pid=3500) INFO 09-16 14:01:01 [utils.py:328] non-default args: {'model_tag': 'Qwen/Qwen3-Next-80B-A...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Failed to run Qwen3-Next on vLLM v0.10.2rc3.dev103+g238c4c170.cpu bug;stale ### Your current environment ### 🐛 Describe the bug I got an error when I running Qwen3-Next on vLLM v0.10.2rc3.dev103+g238c4c170.cpu ``...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pid=3500) ERROR 09-16 14:02:15 [registry.py:444] AttributeError: module 'triton.language' has no attribute 'exp' (APIServer pid=3500) ERROR 09-16 14:02:15 [registry.py:444] (APIServer pid=3500) Traceback (most recent ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d=3500) ERROR 09-16 14:02:15 [registry.py:444] Error in inspecting model architecture 'Qwen3NextForCausalLM' (APIServer pid=3500) ERROR 09-16 14:02:15 [registry.py:444] Traceback (most recent call last): (APIServer pid=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Failed to run Qwen3-Next on vLLM v0.10.2rc3.dev103+g238c4c170.cpu bug;stale ### Your current environment ### 🐛 Describe the bug I got an error when I running Qwen3-Next on vLLM v0.10.2rc3.dev103+g238c4c170.cpu ``` (v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
