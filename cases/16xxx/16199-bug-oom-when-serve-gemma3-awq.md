# vllm-project/vllm#16199: [Bug]: OOM when serve  Gemma3-AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#16199](https://github.com/vllm-project/vllm/issues/16199) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;quantization |
| 症状 | mismatch;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM when serve  Gemma3-AWQ

### Issue 正文摘录

### Your current environment Vllm 0.8.3 ### 🐛 Describe the bug I couldn't serve gemma3-AWQ model on 24G GPU. - command1: ``` VLLM_USE_V1=0 vllm serve gaunernst/gemma-3-27b-it-int4-awq \ --max-model-len 4096 --gpu-memory-utilization 0.98 --distributed-executor-backend ray --dtype float16 ``` - error1: ``` INFO 04-07 15:52:21 [model_runner.py:1146] Model loading took 17.6110 GiB and 12.273077 seconds ValueError: The model's max seq len (4096) is larger than the maximum number of tokens that can be stored in KV cache (3584). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. ``` - command2: ``` VLLM_USE_V1=0 vllm serve gaunernst/gemma-3-27b-it-int4-awq \ --max-model-len 128 --gpu-memory-utilization 0.98 --distributed-executor-backend ray --dtype float16 ``` - error2: ``` INFO 04-07 15:54:56 [worker.py:267] the current vLLM instance can use total_gpu_memory (21.99GiB) x gpu_memory_utilization (0.98) = 21.55GiB ERROR 04-07 15:55:35 [engine.py:448] File "/python3.9/site-packages/torch/cuda/graphs.py", line 84, in capture_end ERROR 04-07 15:55:35 [engine.py:448] super().capture_end() ERROR 04-07 15:55:35 [engine.py:448] RuntimeError: CUDA...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: GPU. - command1: ``` VLLM_USE_V1=0 vllm serve gaunernst/gemma-3-27b-it-int4-awq \ --max-model-len 4096 --gpu-memory-utilization 0.98 --distributed-executor-backend ray --dtype float16 ``` - error1: ``` INFO 04-07 15:52:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: OR 04-07 15:55:35 [engine.py:448] File "/python3.9/site-packages/torch/cuda/graphs.py", line 84, in capture_end ERROR 04-07 15:55:35 [engine.py:448] super().capture_end() ERROR 04-07 15:55:35 [engine.py:448] RuntimeErro...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: OOM when serve Gemma3-AWQ bug;stale ### Your current environment Vllm 0.8.3 ### 🐛 Describe the bug I couldn't serve gemma3-AWQ model on 24G GPU. - command1: ``` VLLM_USE_V1=0 vllm serve gaunernst/gemma-3-27b-it-i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: OOM when serve Gemma3-AWQ bug;stale ### Your current environment Vllm 0.8.3 ### 🐛 Describe the bug I couldn't serve gemma3-AWQ model on 24G GPU. - command1: ``` VLLM_USE_V1=0 vllm serve gaunernst/gemma-3-27b-it-i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: OOM when serve Gemma3-AWQ bug;stale ### Your current environment Vllm 0.8.3 ### 🐛 Describe the bug I couldn't serve gemma3-AWQ model on 24G GPU. - command1: ``` VLLM_USE_V1=0 vllm serve gaunernst/gemma-3-27b-it-i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
