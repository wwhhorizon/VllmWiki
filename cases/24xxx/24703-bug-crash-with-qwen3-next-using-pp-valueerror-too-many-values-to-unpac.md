# vllm-project/vllm#24703: [Bug]: Crash with Qwen3-Next using -pp: ValueError: too many values to unpack (expected 2)

| 字段 | 值 |
| --- | --- |
| Issue | [#24703](https://github.com/vllm-project/vllm/issues/24703) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash with Qwen3-Next using -pp: ValueError: too many values to unpack (expected 2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Starting vllm serve for Qwen3-Next-80B-A3B-Instruct with pipeline parallelism (-pp 4) fails during engine initialization. All four PP workers load weights successfully, then the process aborts with: ``` TORCHDYNAMO_VERBOSE=1 \ CUDA_DEVICE_ORDER=PCI_BUS_ID \ CUDA_VISIBLE_DEVICES=0,2,4,1 \ VLLM_PP_LAYER_PARTITION="8,29,8,3" \ VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ vllm serve /mnt/llms/models/Qwen/Qwen3-Next-80B-A3B-Instruct \ --port 8000 \ --max-model-len 8192 \ -pp 4 ``` Main error: `RuntimeError: Worker failed with error 'Can't unpack a tensor of 2048 rows into a tuple of 2 elements.` Full output log: https://gist.github.com/RodriMora/0af77e35f55709e0ef5b7c45361b906b With --enforce-eager ``` ValueError: too many values to unpack (expected 2) at vllm/model_executor/models/qwen3_next.py:945 ``` Full output log: https://gist.github.com/RodriMora/e3b6967d915e5625eefce17447190be8 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the process aborts with: ``` TORCHDYNAMO_VERBOSE=1 \ CUDA_DEVICE_ORDER=PCI_BUS_ID \ CUDA_VISIBLE_DEVICES=0,2,4,1 \ VLLM_PP_LAYER_PARTITION="8,29,8,3" \ VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ vllm serve /mnt/llms/models/Qwen/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: arting vllm serve for Qwen3-Next-80B-A3B-Instruct with pipeline parallelism (-pp 4) fails during engine initialization. All four PP workers load weights successfully, then the process aborts with: ``` TORCHDYNAMO_VERBOS...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Crash with Qwen3-Next using -pp: ValueError: too many values to unpack (expected 2) bug ### Your current environment ### 🐛 Describe the bug Starting vllm serve for Qwen3-Next-80B-A3B-Instruct with pipeline parall...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
