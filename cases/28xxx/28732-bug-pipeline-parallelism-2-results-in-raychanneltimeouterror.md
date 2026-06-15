# vllm-project/vllm#28732: [Bug]: `--pipeline-parallelism>2` results in `RayChannelTimeoutError`

| 字段 | 值 |
| --- | --- |
| Issue | [#28732](https://github.com/vllm-project/vllm/issues/28732) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `--pipeline-parallelism>2` results in `RayChannelTimeoutError`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using vllm 0.11.0. I have been running VLLM on a Ray cluster from 2 up to 8 nodes. I have 4 GPUs per node, all connected with NCCL over slingshot successfully. I have successfully run with tensor parallelism up to 16. However, when I run with pipeline parallelism more than 2 (e.g. 4) the model serving hangs. ```bash VLLM_ALLREDUCE_USE_SYMM_MEM=0 vllm serve \ open/gpt-oss-120b \ --served-model-name openai/gpt-oss-120b \ --disable-frontend-multiprocessing \ --port 8000 \ --distributed-executor-backend ray \ --tensor-parallel-size=4 \ --pipeline-parallel-size=4 ``` I get: `ray.exceptions.RayChannelTimeoutError: System error: Timed out waiting for object available to [read.`](url) And uneven memory distribution (usually all my GPUs are pinned): I have Ray and VLLM logs: - [ray_log.txt](https://github.com/user-attachments/files/23551137/ray_log.txt) - [vllm_output_error.txt](https://github.com/user-attachments/files/23551142/vllm_output_error.txt) I have set: ```shell -e VLLM_LOGGING_LEVEL=INFO -e NCCL_DEBUG=TRACE ``` Similar issue: https://github.com/vllm-project/vllm/issues/15102 ### Before submitting a new issue... - [x] Make...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: `--pipeline-parallelism>2` results in `RayChannelTimeoutError` bug;stale ### Your current environment ### 🐛 Describe the bug I am using vllm 0.11.0. I have been running VLLM on a Ray cluster from 2 up to 8 nodes....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Bug]: `--pipeline-parallelism>2` results in `RayChannelTimeoutError` bug;stale ### Your current environment ### 🐛 Describe the bug I am using vllm 0.11.0. I have been running VLLM on a Ray cluster from 2 up to 8 nodes....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -frontend-multiprocessing \ --port 8000 \ --distributed-executor-backend ray \ --tensor-parallel-size=4 \ --pipeline-parallel-size=4 ``` I get: `ray.exceptions.RayChannelTimeoutError: System error: Timed out waiting for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: . However, when I run with pipeline parallelism more than 2 (e.g. 4) the model serving hangs. ```bash VLLM_ALLREDUCE_USE_SYMM_MEM=0 vllm serve \ open/gpt-oss-120b \ --served-model-name openai/gpt-oss-120b \ --disable-fr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
