# vllm-project/vllm#18831: [Bug]: "NCCL WARN Error while attaching to shared memory segment /dev/shm/nccl- (size 192814336), error: No such file or directory (2)"

| 字段 | 值 |
| --- | --- |
| Issue | [#18831](https://github.com/vllm-project/vllm/issues/18831) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "NCCL WARN Error while attaching to shared memory segment /dev/shm/nccl- (size 192814336), error: No such file or directory (2)"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I has a ray cluster with 2 machines, with head has 4 a100 and worker has 8 a100. ## My tests 1. I did the nccl test between these 2 machines, they worked well. 2. I runed the command with vllm serve on single node, it also worked well, the command is: ``` NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=ALL NCCL_SOCKET_IFNAME=eth0 GLOO_SOCKET_IFNAME=eth0 vllm serve /home/jianmao/workspace/Qwen3-30B-A3B \ --served_model_name qwen3 \ --pipeline-parallel-size 1 \ --tensor-parallel-size 4 \ --dtype float16 \ --gpu-memory-utilization 0.95 \ --max-model-len 4096 \ --trust-remote-code \ --host 0.0.0.0 \ --port 8009 ``` ## My problem But when I tried to run the vllm serve command, it failed, the command is: ``` NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=ALL NCCL_SOCKET_IFNAME=eth0 GLOO_SOCKET_IFNAME=eth0 vllm serve /home/jianmao/workspace/Qwen3-30B-A3B \ --served_model_name qwen3 \ --pipeline-parallel-size 2 \ --tensor-parallel-size 4 \ --dtype float16 \ --gpu-memory-utilization 0.95 \ --max-model-len 4096 \ --trust-remote-code \ --host 0.0.0.0 \ --port 8009 ``` The logs: ``` INFO 05-28 03:19:31 [__init__.py:239] Automatically detected platform cuda. INFO 05-28...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: platform cuda. INFO 05-28 03:19:36 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 05-28 03:19:36 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/home/jianmao/workspace/Qwen3-30B-A3B',...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ev/shm/nccl- (size 192814336), error: No such file or directory (2)" bug;stale ### Your current environment ### 🐛 Describe the bug I has a ray cluster with 2 machines, with head has 4 a100 and worker has 8 a100. ## My t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: \ --pipeline-parallel-size 1 \ --tensor-parallel-size 4 \ --dtype float16 \ --gpu-memory-utilization 0.95 \ --max-model-len 4096 \ --trust-remote-code \ --host 0.0.0.0 \ --port 8009 ``` ## My problem But when I tried to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: T_IFNAME=eth0 GLOO_SOCKET_IFNAME=eth0 vllm serve /home/jianmao/workspace/Qwen3-30B-A3B \ --served_model_name qwen3 \ --pipeline-parallel-size 1 \ --tensor-parallel-size 4 \ --dtype float16 \ --gpu-memory-utilization 0.9...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: e, config_format= , dtype='float16', max_model_len=4096, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
