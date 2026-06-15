# vllm-project/vllm#23138: [Bug]:Non-deterministic outputs despite temperature=0.0 when handling concurrent requests

| 字段 | 值 |
| --- | --- |
| Issue | [#23138](https://github.com/vllm-project/vllm/issues/23138) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Non-deterministic outputs despite temperature=0.0 when handling concurrent requests

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We've discovered that model outputs exhibit randomness even when `temperature=0.0` is set, specifically when the server handles concurrent requests. This issue affects deterministic use cases where reproducible outputs are critical. ## Environment - **vLLM Setup**: OpenAI-Compatible Server - **Model**: `brandonbeiler/InternVL3-38B-FP8-Dynamic` - **Client Configuration**: Multiple concurrent clients ```bash sudo docker run --runtime nvidia --gpus all -p 8000:8000 --ipc=host --shm-size=16g -v $HOME/.cache/huggingface:/root/.cache/huggingface -e HUGGING_FACE_HUB_TOKEN= vllm/vllm-openai:latest --model brandonbeiler/InternVL3-38B-FP8-Dynamic --trust-remote-code --dtype auto --gpu-memory-utilization 0.9 --max-model-len 8192 --enable-prefix-caching --cpu-offload-gb 5 ``` ## Problem Description Despite setting `temperature=0.0` to ensure deterministic outputs, we observe significant variability in model responses under specific conditions. When the same prompt is submitted multiple times, the outputs differ and sometimes even produce semantically opposite responses. ## Reproduction Steps 1. Set up vLLM OpenAI-Compatible Server with the s...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: [Bug]:Non-deterministic outputs despite temperature=0.0 when handling concurrent requests bug;stale ### Your current environment ### 🐛 Describe the bug We've discovered that model outputs exhibit randomness even when `t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: model outputs exhibit randomness even when `temperature=0.0` is set, specifically when the server handles concurrent requests. This issue affects deterministic use cases where reproducible outputs are critical. ## Envir...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ur current environment ### 🐛 Describe the bug We've discovered that model outputs exhibit randomness even when `temperature=0.0` is set, specifically when the server handles concurrent requests. This issue affects deter...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: up**: OpenAI-Compatible Server - **Model**: `brandonbeiler/InternVL3-38B-FP8-Dynamic` - **Client Configuration**: Multiple concurrent clients ```bash sudo docker run --runtime nvidia --gpus all -p 8000:8000 --ipc=host -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: n-deterministic outputs despite temperature=0.0 when handling concurrent requests bug;stale ### Your current environment ### 🐛 Describe the bug We've discovered that model outputs exhibit randomness even when `temperatu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
