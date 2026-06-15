# vllm-project/vllm#28796: [Bug]: AttributeError: '_OpNamespace' '_C' object has no attribute 'gptq_marlin_repack'

| 字段 | 值 |
| --- | --- |
| Issue | [#28796](https://github.com/vllm-project/vllm/issues/28796) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;fp8;kernel;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: '_OpNamespace' '_C' object has no attribute 'gptq_marlin_repack'

### Issue 正文摘录

### Your current environment metax gpu vllm serve /mnt/DeepSeek-R1-0528/ -pp 4 -tp 8 --trust-remote-code --distributed-executor-backend ray --quantization fp8 --dtype bfloat16 --max-model-len 16384 --swap-space 16 --gpu-memory-utilization 0.95 --served-model-name DeepSeek-R1 找不到原因，是因为GPU不支持 fp8 吗？ Can't find the reason? Is it because the GPU doesn't support FP8? ### 🐛 Describe the bug vllm serve /mnt/DeepSeek-R1-0528/ -pp 4 -tp 8 --trust-remote-code --distributed-executor-backend ray --quantization fp8 --dtype bfloat16 --max-model-len 16384 --swap-space 16 --gpu-memory-utilization 0.95 --served-model-name DeepSeek-R1 /opt/conda/lib/python3.10/site-packages/torchvision/datapoints/__init__.py:12: UserWarning: The torchvision.datapoints and torchvision.transforms.v2 namespaces are still Beta. While we do not expect major breaking changes, some APIs may still change according to user feedback. Please submit any feedback you may have in this issue: https://github.com/pytorch/vision/issues/6753, and you can also check out https://github.com/pytorch/vision/issues/7319 to learn more about the APIs that we suspect might involve future changes. You can silence this warning by calling torchv...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: 28/ -pp 4 -tp 8 --trust-remote-code --distributed-executor-backend ray --quantization fp8 --dtype bfloat16 --max-model-len 16384 --swap-space 16 --gpu-memory-utilization 0.95 --served-model-name DeepSeek-R1 找不到原因，是因为GPU...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 11-15 12:24:17 [api_server.py:1755] vLLM API server version 0.10.0 INFO 11-15 12:24:17 [cli_args.py:261] non-default args: {'model_tag': '/mnt/DeepSeek-R1-0528/', 'model': '/mnt/DeepSeek-R1-0528/', '...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: or: '_OpNamespace' '_C' object has no attribute 'gptq_marlin_repack' bug;stale ### Your current environment metax gpu vllm serve /mnt/DeepSeek-R1-0528/ -pp 4 -tp 8 --trust-remote-code --distributed-executor-backend ray...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: DeepSeek-R1-0528/ -pp 4 -tp 8 --trust-remote-code --distributed-executor-backend ray --quantization fp8 --dtype bfloat16 --max-model-len 16384 --swap-space 16 --gpu-memory-utilization 0.95 --served-model-name DeepSeek-R...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: G) INFO 11-15 12:24:15 [__init__.py:238] Automatically detected platform cuda. INFO 11-15 12:24:17 [api_server.py:1755] vLLM API server version 0.10.0 INFO 11-15 12:24:17 [cli_args.py:261] non-default args: {'model_tag'...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
