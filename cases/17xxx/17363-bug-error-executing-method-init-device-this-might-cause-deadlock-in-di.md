# vllm-project/vllm#17363: [Bug]: Error executing method 'init_device'. This might cause deadlock in distributed execution.

| 字段 | 值 |
| --- | --- |
| Issue | [#17363](https://github.com/vllm-project/vllm/issues/17363) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error executing method 'init_device'. This might cause deadlock in distributed execution.

### Issue 正文摘录

### Your current environment vllm0.8.4 vllm_ascend0.8.4rc2 ### 🐛 Describe the bug root@pm-cbbe0001:/# nohup vllm serve /home/ma-user/aicc/Qwen/Qwen3-235B-A22B/ -pp 2 -tp 8 --trust-remote-code --distributed-executor-backend ray --dtype bfloat16 --max-model-len 16384 --max-num-batched-tokens 32768 --block-size 128 --swap-space 4 --gpu-memory-utilization 0.96 --served-model-name "DeepSeek-R1" --host 0.0.0.0 --port 18001 --enable-chunked-prefill --enable-prefix-caching &> vllm.log & tail -f vllm.log [1] 155152 nohup: ignoring input INFO 04-29 08:20:12 [__init__.py:30] Available plugins for group vllm.platform_plugins: INFO 04-29 08:20:12 [__init__.py:32] name=ascend, value=vllm_ascend:register INFO 04-29 08:20:12 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded. INFO 04-29 08:20:12 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. INFO 04-29 08:20:12 [__init__.py:44] plugin ascend loaded. INFO 04-29 08:20:12 [__init__.py:230] Platform plugin ascend is activated INFO 04-29 08:20:15 [__init__.py:30] Available plugins for group vllm.general_plugins: INFO 04-29 08:20:15 [__init__.py:32] name=ascend_enhanced_model,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: l loaded. INFO 04-29 08:20:15 [patch_tritonplaceholder.py:33] Triton not installed or not compatible; certain GPU-related functions will not be available. WARNING 04-29 08:20:15 [patch_tritonplaceholder.py:46] Triton is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Error executing method 'init_device'. This might cause deadlock in distributed execution. bug;stale ### Your current environment vllm0.8.4 vllm_ascend0.8.4rc2 ### 🐛 Describe the bug root@pm-cbbe0001:/# nohup vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 2B/ -pp 2 -tp 8 --trust-remote-code --distributed-executor-backend ray --dtype bfloat16 --max-model-len 16384 --max-num-batched-tokens 32768 --block-size 128 --swap-space 4 --gpu-memory-utilization 0.96 --served-model-n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: escribe the bug root@pm-cbbe0001:/# nohup vllm serve /home/ma-user/aicc/Qwen/Qwen3-235B-A22B/ -pp 2 -tp 8 --trust-remote-code --distributed-executor-backend ray --dtype bfloat16 --max-model-len 16384 --max-num-batched-t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: /Qwen3-235B-A22B/ -pp 2 -tp 8 --trust-remote-code --distributed-executor-backend ray --dtype bfloat16 --max-model-len 16384 --max-num-batched-tokens 32768 --block-size 128 --swap-space 4 --gpu-memory-utilization 0.96 --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
