# vllm-project/vllm#31334: [Bug]: vllm+ray：vllm serve DeepSeek-V3.2V-AWQ ERROR.

| 字段 | 值 |
| --- | --- |
| Issue | [#31334](https://github.com/vllm-project/vllm/issues/31334) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm+ray：vllm serve DeepSeek-V3.2V-AWQ ERROR.

### Issue 正文摘录

### Your current environment vLLM docker image. 2 x L20 x 8 ### 🐛 Describe the bug root@ai-tgslave07:/home/# vllm serve /home/zcc/DeepSeek-V3.2-AWQ --served-model-name DeepSeek-v32 --tensor-parallel-size=8 --pipeline-parallel-size 2 --gpu-memory-utilization=0.95 --host=0.0.0.0 --max-model-len 32768 --port 8000 --trust-remote-code INFO 12-24 23:36:28 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=1744) INFO 12-24 23:36:28 [api_server.py:1977] vLLM API server version 0.11.2 (APIServer pid=1744) INFO 12-24 23:36:28 [utils.py:253] non-default args: {'model_tag': '/home/zcc/DeepSeek-V3.2-AWQ', 'host': '0.0.0.0', 'model': '/home/zcc/DeepSeek-V3.2-AWQ', 'trust_remote_code': True, 'max_model_len': 32768, 'served_model_name': ['DeepSeek-v32'], 'pipeline_parallel_size': 2, 'tensor_parallel_size': 8, 'gpu_memory_utilization': 0.95} (APIServer pid=1744) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1744) You are using a model of type deepseek_v32 to instantiate a model of type deepseek_v3. This is not supported for all configurations of models and can yield errors. (APIServ...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e DeepSeek-V3.2V-AWQ ERROR. bug;stale ### Your current environment vLLM docker image. 2 x L20 x 8 ### 🐛 Describe the bug root@ai-tgslave07:/home/# vllm serve /home/zcc/DeepSeek-V3.2-AWQ --served-model-name DeepSeek-v32...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ot@ai-tgslave07:/home/# vllm serve /home/zcc/DeepSeek-V3.2-AWQ --served-model-name DeepSeek-v32 --tensor-parallel-size=8 --pipeline-parallel-size 2 --gpu-memory-utilization=0.95 --host=0.0.0.0 --max-model-len 32768 --po...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vllm+ray：vllm serve DeepSeek-V3.2V-AWQ ERROR. bug;stale ### Your current environment vLLM docker image. 2 x L20 x 8 ### 🐛 Describe the bug root@ai-tgslave07:/home/# vllm serve /home/zcc/DeepSeek-V3.2-AWQ --served...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: entrypoints/cli/main.py", line 73, in main (APIServer pid=1744) args.dispatch_function(args) (APIServer pid=1744) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 60, in cmd (APIServer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: errors. (APIServer pid=1744) INFO 12-24 23:36:28 [model.py:631] Resolved architecture: DeepseekV32ForCausalLM (APIServer pid=1744) INFO 12-24 23:36:28 [model.py:1745] Using max model len 32768 (APIServer pid=1744) INFO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
