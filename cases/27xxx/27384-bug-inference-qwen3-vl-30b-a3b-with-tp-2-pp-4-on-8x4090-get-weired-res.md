# vllm-project/vllm#27384: [Bug]: Inference Qwen3-VL-30B-A3B with tp=2 pp=4 on 8x4090 get weired result

| 字段 | 值 |
| --- | --- |
| Issue | [#27384](https://github.com/vllm-project/vllm/issues/27384) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference Qwen3-VL-30B-A3B with tp=2 pp=4 on 8x4090 get weired result

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug server launch command： ``` PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_V1=1 python -m vllm.entrypoints.openai.api_server --served-model-name Qwen3-VL-30B-A3B-Instruct --model=/log/output/Qwen3-VL-30B-A3B-Instruct --trust-remote-code --host 0.0.0.0 --port 8080 --max-model-len 32768 --tensor-parallel-size 2 --pipeline-parallel-size 4 --gpu_memory_utilization 0.8 --max-num-seqs 128 --mm-processor-kwargs='{"max_pixels":589824}' ``` some requests get random output with pp=4 tp=2 configuration. but everything is good when tp=8 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;gemm;operator;triton build_error env_dependency Your current enviro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Inference Qwen3-VL-30B-A3B with tp=2 pp=4 on 8x4090 get weired result bug;stale ### Your current environment ### 🐛 Describe the bug server launch command： ``` PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ironment ### 🐛 Describe the bug server launch command： ``` PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_V1=1 python -m vllm.entrypoints.openai.api_server --served-model-name Qwen3-VL-30B-A3B-Instruct --mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nference Qwen3-VL-30B-A3B with tp=2 pp=4 on 8x4090 get weired result bug;stale ### Your current environment ### 🐛 Describe the bug server launch command： ``` PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_V1=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _parallel;frontend_api;hardware_porting;model_support cuda;gemm;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
