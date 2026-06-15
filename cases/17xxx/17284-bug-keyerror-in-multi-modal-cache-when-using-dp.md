# vllm-project/vllm#17284: [Bug]: KeyError in multi-modal cache when using DP

| 字段 | 值 |
| --- | --- |
| Issue | [#17284](https://github.com/vllm-project/vllm/issues/17284) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError in multi-modal cache when using DP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As tracked in #16875 , The latest vllm still faces KeyError using DP configs: ```bash VLLM_ENABLE_V1_MULTIPROCESSING=0 USE_FASTSAFETENSOR=true VLLM_USE_V1=1 python api_server.py --model Qwen/Qwen-2.5-VL-7B-Instruct --max_model_len 32768 --limit-mm-per-prompt image=1,video=1 -tp 1 -dp 8 --port 8002 ``` It throws `KeyError` during mm_cache retrieval when there is more than 1 mm_inputs in the request queue. The issue is fixed when setting `-tp n -dp 1`. As @DarkLight1337 denotes, for DP use case, this issue may be caused by the syncing of mm_cache between different workers, @youkaichao @njhill could it be fixed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rkLight1337 denotes, for DP use case, this issue may be caused by the syncing of mm_cache between different workers, @youkaichao @njhill could it be fixed? ### Before submitting a new issue... - [x] Make sure you alread...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ug As tracked in #16875 , The latest vllm still faces KeyError using DP configs: ```bash VLLM_ENABLE_V1_MULTIPROCESSING=0 USE_FASTSAFETENSOR=true VLLM_USE_V1=1 python api_server.py --model Qwen/Qwen-2.5-VL-7B-Instruct -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: or` during mm_cache retrieval when there is more than 1 mm_inputs in the request queue. The issue is fixed when setting `-tp n -dp 1`. As @DarkLight1337 denotes, for DP use case, this issue may be caused by the syncing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ent environment ### 🐛 Describe the bug As tracked in #16875 , The latest vllm still faces KeyError using DP configs: ```bash VLLM_ENABLE_V1_MULTIPROCESSING=0 USE_FASTSAFETENSOR=true VLLM_USE_V1=1 python api_server.py --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
