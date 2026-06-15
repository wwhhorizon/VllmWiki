# vllm-project/vllm#8225: [Usage]: FP8 and INT8

| 字段 | 值 |
| --- | --- |
| Issue | [#8225](https://github.com/vllm-project/vllm/issues/8225) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: FP8 and INT8

### Issue 正文摘录

### Your current environment vllm 0.5.4 model: qwen I use Qwen model and quantized it to be of dtype FP8, but the log indicates it still warning that it casts torch.bfloat16 to torch.float16. I wonder if it matters? and, when I quantize model to be dtype of INT 8 I encountered OOM error on RTX4090, so can I quantize the model on A800 with a different cuda-driver and run it on RTX4090? ``` 2024-09-06T14:21:49.539172961+08:00 WARNING 09-06 14:21:49 config.py:1454] Casting torch.bfloat16 to torch.float16. (Actually the performance is improved) I want to know if it the warning matters. .... 2024-09-06T14:21:50.128608655+08:00 WARNING 09-06 14:21:50 fp8.py:43] Detected fp8 checkpoint. Please note that the format is experimental and subject to change. ``` ### How would you like to use vllm the whole log: ``` 2024-09-06T14:21:49.536161849+08:00 INFO 09-06 14:21:49 api_server.py:339] vLLM API server version 0.5.4 2024-09-06T14:21:49.536484106+08:00 INFO 09-06 14:21:49 api_server.py:340] args: Namespace(host=None, port=18544, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapte...

## 现有链接修复摘要

#35697 [CPU] Support int8 compute mode in CPU AWQ

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Usage]: FP8 and INT8 usage;stale ### Your current environment vllm 0.5.4 model: qwen I use Qwen model and quantized it to be of dtype FP8, but the log indicates it still warning that it casts torch.bfloat16 to torch.fl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Usage]: FP8 and INT8 usage;stale ### Your current environment vllm 0.5.4 model: qwen I use Qwen model and quantized it to be of dtype FP8, but the log indicates it still warning that it casts torch.bfloat16 to torch.fl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sage]: FP8 and INT8 usage;stale ### Your current environment vllm 0.5.4 model: qwen I use Qwen model and quantized it to be of dtype FP8, but the log indicates it still warning that it casts torch.bfloat16 to torch.floa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 9.536161849+08:00 INFO 09-06 14:21:49 api_server.py:339] vLLM API server version 0.5.4 2024-09-06T14:21:49.536484106+08:00 INFO 09-06 14:21:49 api_server.py:340] args: Namespace(host=None, port=18544, uvicorn_log_level=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: d, when I quantize model to be dtype of INT 8 I encountered OOM error on RTX4090, so can I quantize the model on A800 with a different cuda-driver and run it on RTX4090? ``` 2024-09-06T14:21:49.539172961+08:00 WARNING 0...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35697](https://github.com/vllm-project/vllm/pull/35697) | mentioned | 0.6 | [CPU] Support int8 compute mode in CPU AWQ | compute paths. AWQ - SGLang INT4 W4A8 kernel (adapted from [sglang#8225](https://github.com/sgl-project/sglang/pull/8225) / [sglang#8226](https://github.com/sgl-project/sglang/pul… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
