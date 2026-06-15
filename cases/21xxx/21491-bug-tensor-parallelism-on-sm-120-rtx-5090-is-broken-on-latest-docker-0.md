# vllm-project/vllm#21491: [Bug]: Tensor parallelism on sm_120 (rtx 5090) is broken on latest docker (0.9.2)?

| 字段 | 值 |
| --- | --- |
| Issue | [#21491](https://github.com/vllm-project/vllm/issues/21491) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Tensor parallelism on sm_120 (rtx 5090) is broken on latest docker (0.9.2)?

### Issue 正文摘录

### Your current environment docker run -d --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=xxxx" -p 8002:8000 --ipc=host vllm/vllm-openai:latest --model openai/whisper-large-v3 --gpu_memory_utilization 0.90 --tensor-parallel-size 2 ### 🐛 Describe the bug Apparently, when I start a container with tensor-parallelism (2) using the aforementioned combination, the server gets stuck on some call related to nccl. My log below is using whisper, but also tried with llms to no avail. I can load a model individually on each gpu without tensor-paralellism, though. ``` INFO 07-23 19:51:14 [__init__.py:244] Automatically detected platform cuda. INFO 07-23 19:51:18 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-23 19:51:18 [cli_args.py:325] non-default args: {'model': 'openai/whisper-large-v3', 'tensor_parallel_size': 2} INFO 07-23 19:51:25 [config.py:841] This model supports multiple tasks: {'embed', 'reward', 'classify', 'transcription', 'generate'}. Defaulting to 'transcription'. INFO 07-23 19:51:25 [config.py:1472] Using max model len 448 WARNING 07-23 19:51:25 [arg_utils.py:1735] ['WhisperForConditionalGeneration'] is no...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: parallelism on sm_120 (rtx 5090) is broken on latest docker (0.9.2)? bug;stale ### Your current environment docker run -d --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Tensor parallelism on sm_120 (rtx 5090) is broken on latest docker (0.9.2)? bug;stale ### Your current environment docker run -d --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface --env...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Tensor parallelism on sm_120 (rtx 5090) is broken on latest docker (0.9.2)? bug;stale ### Your current environment docker run -d --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface --env...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rent environment docker run -d --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=xxxx" -p 8002:8000 --ipc=host vllm/vllm-openai:latest --model openai/whisper-larg...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
