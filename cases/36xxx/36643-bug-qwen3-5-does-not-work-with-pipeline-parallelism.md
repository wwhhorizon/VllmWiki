# vllm-project/vllm#36643: [Bug]: Qwen3.5 does not work with pipeline parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#36643](https://github.com/vllm-project/vllm/issues/36643) |
| 状态 | open |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 does not work with pipeline parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm server bash ```bash python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen3.5-35B-A3B --model /athena/Qwen3.5-35B-A3B --gpu-memory-utilization 0.9 --tensor-parallel-size 1 --pipeline-parallel-size 4 --moe-backend marlin --max-model-len 160000 --max-num-batched-tokens 4096 --max-num-seqs 32 --distributed-executor-backend ray --enable-log-requests --enable-log-outputs --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-prefix-caching --reasoning-parser qwen3 --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' ``` error output ``` root@xuanwu-text-safety-qwen3-5-1355630-z8p8q:/data# nohup python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen3.5-35B-A3B --model /athena/Qwen3.5-35B-A3B --gpu-memory-utilization 0.9 --tensor-parallel-size 1 --pipeline-parallel-size 4 --moe-backend marlin --max-model-len 160000 --max-num-batched-tokens 4096 --max-num-seqs 32 --distributed-executor-backend ray --enable-log-requests --enable-log-outputs --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-prefix-caching --reasoning-parser qwen3 --speculative-config '...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: d=443977) INFO 03-10 19:20:41 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.0 (APIServer pid=443977) INFO 03-10 19:20:41 [utils.py:302] █▄█▀ █ █ █ █ model /athena/Qwen3.5-35B-A3B (APIServer pid=443977) INFO 03-10 19:20:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5 does not work with pipeline parallelism bug ### Your current environment ### 🐛 Describe the bug vllm server bash ```bash python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen3.5-35B-A3B -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s 4096 --max-num-seqs 32 --distributed-executor-backend ray --enable-log-requests --enable-log-outputs --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-prefix-caching --reasoning-parser qwen3 --speculat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Qwen3.5 does not work with pipeline parallelism bug ### Your current environment ### 🐛 Describe the bug vllm server bash ```bash python3 -m vllm.entrypoints.openai.api_server --served-model-name Qwen3.5-35B-A3B -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tilization 0.9 --tensor-parallel-size 1 --pipeline-parallel-size 4 --moe-backend marlin --max-model-len 160000 --max-num-batched-tokens 4096 --max-num-seqs 32 --distributed-executor-backend ray --enable-log-requests --e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
