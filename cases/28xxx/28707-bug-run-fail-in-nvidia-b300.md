# vllm-project/vllm#28707: [Bug]: run fail in nvidia b300

| 字段 | 值 |
| --- | --- |
| Issue | [#28707](https://github.com/vllm-project/vllm/issues/28707) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: run fail in nvidia b300

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I based on nvcr.io/nvidia/pytorch:25.10-py3 image according to the official website “To build vLLM using an existing PyTorch installation” tutorial installed vLLm in b300 run error ```shell root@localhost:/workspace/vllm-0.11.0# python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8888 --dtype float16 --model=/model/neuralmagic/Qwen2.5-VL-72B-Instruct-FP8-Dynamic/neuralmagic/Qwen2___5-VL-72B-Instruct-FP8-Dynamic --trust-remote-code --tensor-parallel-size 1 --no-enable-prefix-caching INFO 11-14 06:32:16 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=102050) INFO 11-14 06:32:25 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=102050) INFO 11-14 06:32:25 [utils.py:233] non-default args: {'host': '0.0.0.0', 'port': 8888, 'model': '/model/neuralmagic/Qwen2.5-VL-72B-Instruct-FP8-Dynamic/neuralmagic/Qwen2___5-VL-72B-Instruct-FP8-Dynamic', 'trust_remote_code': True, 'dtype': 'float16', 'enable_prefix_caching': False} (APIServer pid=102050) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=102050) INFO 11-14 06:32:...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: I based on nvcr.io/nvidia/pytorch:25.10-py3 image according to the official website “To build vLLM using an existing PyTorch installation” tutorial installed vLLm in b300 run error ```shell root@localhost:/workspace/vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: thon3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8888 --dtype float16 --model=/model/neuralmagic/Qwen2.5-VL-72B-Instruct-FP8-Dynamic/neuralmagic/Qwen2___5-VL-72B-Instruct-FP8-Dynamic --trust-remote-code...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: run fail in nvidia b300 bug;unstale ### Your current environment ### 🐛 Describe the bug I based on nvcr.io/nvidia/pytorch:25.10-py3 image according to the official website “To build vLLM using an existing PyTorch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: trypoints.openai.api_server --host 0.0.0.0 --port 8888 --dtype float16 --model=/model/neuralmagic/Qwen2.5-VL-72B-Instruct-FP8-Dynamic/neuralmagic/Qwen2___5-VL-72B-Instruct-FP8-Dynamic --trust-remote-code --tensor-parall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
