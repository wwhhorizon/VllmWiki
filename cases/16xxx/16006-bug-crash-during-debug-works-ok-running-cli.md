# vllm-project/vllm#16006: [Bug]: crash during debug, works ok running cli

| 字段 | 值 |
| --- | --- |
| Issue | [#16006](https://github.com/vllm-project/vllm/issues/16006) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: crash during debug, works ok running cli

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug running the cli `vllm serve facebook/opt-125m` works out ok. The server starts up. however, it crashes when debugging it in vscode with the following launch.json: ``` { // Use IntelliSense to learn about possible attributes. // Hover to view descriptions of existing attributes. // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387 "version": "0.2.0", "configurations": [ { "name": "vllm serve", "type": "debugpy", "request": "launch", "program": "${workspaceFolder}/vllm/scripts.py", "console": "integratedTerminal", "justMyCode": false, "args": [ "serve", "facebook/opt-125m" ] } ] } ``` The error is: > INFO 04-03 17:56:20 weight_utils.py:254] Using model weights format ['*.safetensors'] > INFO 04-03 17:56:21 weight_utils.py:306] No model.safetensors.index.json found in remote. > Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00 Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:06 Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:06 > INFO 04-03 17:56:28 gpu_model_runner.py:918] Loading model weights took 2.8875 GB > INFO 04-03 17:57:17 backends.py:408] Using cache d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: crash during debug, works ok running cli bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug running the cli `vllm serve facebook/opt-125m` works out ok. The server starts up. however, it...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: // Hover to view descriptions of existing attributes. // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387 "version": "0.2.0", "configurations": [ { "name": "vllm serve", "type": "debugpy", "re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: crash during debug, works ok running cli bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug running the cli `vllm serve facebook/opt-125m` works out ok. The server starts up. however, it...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ailable_memory > ERROR 04-03 17:57:33 core.py:208] self.model_runner.profile_run() > ERROR 04-03 17:57:33 core.py:208] File "/home/cju/aigc/vllm/vllm/v1/worker/gpu_model_runner.py", line 1143, in profile_run > ERROR 04-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: unner.py:918] Loading model weights took 2.8875 GB > INFO 04-03 17:57:17 backends.py:408] Using cache directory: /home/cju/.cache/vllm/torch_compile_cache/ca60c2a0fd/rank_0 for vLLM's torch.compile > INFO 04-03 17:57:17...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
