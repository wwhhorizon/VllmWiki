# vllm-project/vllm#35403: [Bug]: Ray Compiled DAG timeout/deadlock during VLM forward pass with PP>1 and high-res images

| 字段 | 值 |
| --- | --- |
| Issue | [#35403](https://github.com/vllm-project/vllm/issues/35403) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ray Compiled DAG timeout/deadlock during VLM forward pass with PP>1 and high-res images

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running a Vision-Language Model (e.g., Qwen3-VL-4B-Thinking) with Pipeline Parallelism (PP=2) and the Ray distributed executor backend, the API server hangs and eventually crashes with a `RayChannelTimeoutError`. This occurs specifically when processing high-resolution images (e.g., 3840x3840). Based on isolated testing, the root cause is a race condition/deadlock in Ray's Compiled DAG when passing dictionaries containing large CPU tensors (like `pixel_values` in `SchedulerOutput`) between actors. ### Setup & Environment Hardware: 2 node cluster (2x AWS p5 8xH100 instances) Ray Setup: - Node 0: `ray start --head` - Node 1: `ray start --address='xxx:6379'` vLLM Launch Command (Node 0): ```python python3 -m vllm.entrypoints.openai.api_server \ --port=8000 \ --tensor-parallel-size=1 \ --pipeline-parallel-size=2 \ --distributed-executor-backend=ray \ --model=/dev/shm/models/Qwen_Qwen3-VL-4B-Thinking \ --served-model-name=ray-test ``` ### Steps to Reproduce Start the Ray cluster and launch the vLLM API server as described above. Save the reproduction script below as reproduce_crash.py. Run the script requesting a large image size...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Ray Compiled DAG timeout/deadlock during VLM forward pass with PP>1 and high-res images bug ### Your current environment ### 🐛 Describe the bug When running a Vision-Language Model (e.g., Qwen3-VL-4B-Thinking) wi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Ray Compiled DAG timeout/deadlock during VLM forward pass with PP>1 and high-res images bug ### Your current environment ### 🐛 Describe the bug When running a Vision-Language Model (e.g., Qwen3-VL-4B-Thinking) wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Ray Compiled DAG timeout/deadlock during VLM forward pass with PP>1 and high-res images bug ### Your current environment ### 🐛 Describe the bug When running a Vision-Language Model (e.g., Qwen3-VL-4B-Thinking) wi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ision-Language Model (e.g., Qwen3-VL-4B-Thinking) with Pipeline Parallelism (PP=2) and the Ray distributed executor backend, the API server hangs and eventually crashes with a `RayChannelTimeoutError`. This occurs speci...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nking) with Pipeline Parallelism (PP=2) and the Ray distributed executor backend, the API server hangs and eventually crashes with a `RayChannelTimeoutError`. This occurs specifically when processing high-resolution ima...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
