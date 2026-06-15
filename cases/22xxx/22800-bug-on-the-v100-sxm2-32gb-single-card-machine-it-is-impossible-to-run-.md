# vllm-project/vllm#22800: [Bug]: On the V100-SXM2-32GB single-card machine, it is impossible to run Qwen3-30B-A3B-Instruct-2507-AWQ and Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#22800](https://github.com/vllm-project/vllm/issues/22800) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: On the V100-SXM2-32GB single-card machine, it is impossible to run Qwen3-30B-A3B-Instruct-2507-AWQ and Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 using vllm

### Issue 正文摘录

### Your current environment On the V100-SXM2-32GB single-card machine, it is impossible to run Qwen3-30B-A3B-Instruct-2507-AWQ and Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 using vllm vllm serve /data/AI/model/chat/cpatonn-mirror/Qwen3-30B-A3B-Instruct-2507-AWQ \ > --served-model-name Qwen3-30B-A3B-Instruct-2507 \ > --quantization compressed-tensors \ > --dtype float16 \ > --max-model-len 4096 \ > --gpu-memory-utilization 0.95 \ > --trust-remote-code \ > --host 0.0.0.0 --port 5910 INFO 08-13 15:53:39 [__init__.py:235] Automatically detected platform cuda. INFO 08-13 15:53:43 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-13 15:53:43 [cli_args.py:261] non-default args: {'model_tag': '/data/AI/model/chat/cpatonn-mirror/Qwen3-30B-A3B-Instruct-2507-AWQ', 'host': '0.0.0.0', 'port': 5910, 'model': '/data/AI/model/chat/cpatonn-mirror/Qwen3-30B-A3B-Instruct-2507-AWQ', 'trust_remote_code': True, 'dtype': 'float16', 'max_model_len': 4096, 'quantization': 'compressed-tensors', 'served_model_name': ['Qwen3-30B-A3B-Instruct-2507'], 'gpu_memory_utilization': 0.95} WARNING 08-13 15:53:50 [config.py:3443] Casting torch.bfloat16 to torch.float16. INFO 08-13 15:53:50 [config.py:1604] Usin...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Q \ > --served-model-name Qwen3-30B-A3B-Instruct-2507 \ > --quantization compressed-tensors \ > --dtype float16 \ > --max-model-len 4096 \ > --gpu-memory-utilization 0.95 \ > --trust-remote-code \ > --host 0.0.0.0 --por...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 10 INFO 08-13 15:53:39 [__init__.py:235] Automatically detected platform cuda. INFO 08-13 15:53:43 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-13 15:53:43 [cli_args.py:261] non-default args: {'model_tag'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Bug]: On the V100-SXM2-32GB single-card machine, it is impossible to run Qwen3-30B-A3B-Instruct-2507-AWQ and Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 using vllm bug;stale ### Your current environment On the V100-SXM2-32GB...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: platform cuda. INFO 08-13 15:53:43 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-13 15:53:43 [cli_args.py:261] non-default args: {'model_tag': '/data/AI/model/chat/cpatonn-mirror/Qwen3-30B-A3B-Instruct-250...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: struct-2507-AWQ and Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 using vllm bug;stale ### Your current environment On the V100-SXM2-32GB single-card machine, it is impossible to run Qwen3-30B-A3B-Instruct-2507-AWQ and Qwen3-30...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
