# vllm-project/vllm#19979: [Bug]: v0 mlp spec decode online inference failed

| 字段 | 值 |
| --- | --- |
| Issue | [#19979](https://github.com/vllm-project/vllm/issues/19979) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0 mlp spec decode online inference failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug v0 engine mlp spec deocde offline inference of mlp works fine, but online inference fails service start: ```python python -m vllm.entrypoints.openai.api_server --served-model-name mlp_test --model="/home/mwtest/vllm_dev/llama-160m" --trust-remote-code --enforce-eager --max-model-len 2048 --speculative_config '{"model": "/home/mwtest/vllm_dev/llama-160m-accelerator", "draft_tensor_parallel_size": 1}' --tensor-parallel-size 2 --gpu_memory_utilization=0.8 ``` After some requests, an error is reported: ```text INFO 06-23 17:58:14 [engine.py:316] Added request cmpl-c47251e04b80412b84b57047198f0813-0. INFO: ip:49848 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error ERROR 06-23 17:58:14 [engine.py:164] RuntimeError("output with shape [1, 1, 1024] doesn't match the broadcast shape [14, 1, 1024]") ERROR 06-23 17:58:14 [engine.py:164] Traceback (most recent call last): ERROR 06-23 17:58:14 [engine.py:164] File "/home/mwtest/vllm_dev/vllm_fix/vllm/vllm/engine/multiprocessing/engine.py", line 162, in start ERROR 06-23 17:58:14 [engine.py:164] self.run_engine_loop() ERROR 06-23 17:58:14 [engine.py:164] File "/home/mwtest/vllm_dev/vl...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: v0 mlp spec decode online inference failed bug;stale ### Your current environment ### 🐛 Describe the bug v0 engine mlp spec deocde offline inference of mlp works fine, but online inference fails service start: ``...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ence using mlp and it works fine. offline inference: ```python from vllm import LLM, SamplingParams prompts = ["你好，你是谁？", "What's deep learning?", "1+2+3+4÷2=", "你好，你是谁？", "法国的首都在哪里？", "Hello, my name is", "The presiden...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ine.py:164] File "/home/mwtest/vllm_dev/vllm_fix/vllm/vllm/spec_decode/smaller_tp_proposer_worker.py", line 148, in get_spec_proposals ERROR 06-23 17:58:14 [engine.py:164] return self._worker.get_spec_proposals( ERROR 0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e start: ```python python -m vllm.entrypoints.openai.api_server --served-model-name mlp_test --model="/home/mwtest/vllm_dev/llama-160m" --trust-remote-code --enforce-eager --max-model-len 2048 --speculative_config '{"mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error;crash env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
