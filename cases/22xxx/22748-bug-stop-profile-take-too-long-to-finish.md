# vllm-project/vllm#22748: [Bug]: stop_profile take too long to finish

| 字段 | 值 |
| --- | --- |
| Issue | [#22748](https://github.com/vllm-project/vllm/issues/22748) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: stop_profile take too long to finish

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It takes several minutes for http api `stop_profile` to finish, the served model is `Qwen3-0.6B` ### repro 1. start server ``` VLLM_TORCH_PROFILER_DIR=/tmp/vllm-profile vllm serve /root/autodl-tmp/Qwen3-0.6B/ --served-model-name=qwen ``` 2. call completions api for several times ``` curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "qwen", "prompt": "San Francisco is a", "max_tokens": 127, "temperature": 0 }' ``` 3. call `start_profile` ``` curl -X POST http://localhost:8000/start_profile ``` 4. call completions api again 5. call `stop_profile` ``` curl -X POST http://localhost:8000/stop_profile ``` ### log you can see from log that it take minutes for `stop_profile` to complete ``` INFO 08-13 00:01:27 [api_server.py:1170] Stopping profiler... ... ... INFO 08-13 00:04:59 [api_server.py:1172] Profiler stopped. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: on/json" \ -d '{ "model": "qwen", "prompt": "San Francisco is a", "max_tokens": 127, "temperature": 0 }' ``` 3. call `start_profile` ``` curl -X POST http://localhost:8000/start_profile ``` 4. call completions api again...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: takes several minutes for http api `stop_profile` to finish, the served model is `Qwen3-0.6B` ### repro 1. start server ``` VLLM_TORCH_PROFILER_DIR=/tmp/vllm-profile vllm serve /root/autodl-tmp/Qwen3-0.6B/ --served-mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: stop_profile take too long to finish bug;stale ### Your current environment ### 🐛 Describe the bug It takes several minutes for http api `stop_profile` to finish, the served model is `Qwen3-0.6B` ### repro 1. sta...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: stop_profile take too long to finish bug;stale ### Your current environment ### 🐛 Describe the bug It takes several minutes for http api `stop_profile` to finish, the served model is `Qwen3-0.6B` ### repro 1. sta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
