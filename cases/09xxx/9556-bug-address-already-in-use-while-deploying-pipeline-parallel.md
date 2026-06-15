# vllm-project/vllm#9556: [Bug]:  "address already in use" while deploying pipeline parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#9556](https://github.com/vllm-project/vllm/issues/9556) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]:  "address already in use" while deploying pipeline parallel

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **the command:** vllm serve MODELPATH --dtype auto --api-key TOKEN --tensor-parallel-size 4 --pipeline-parallel-size 2 --gpu-memory-utilization 0.90 --enable_prefix_caching --max_model_len 8192 **returns the error:** INFO: Waiting for application startup. INFO: Application startup complete. ERROR: [Errno 98] error while attempting to bind on address ('0.0.0.0', 8000): address already in use INFO: Waiting for application shutdown. INFO: Application shutdown complete. (VllmWorkerProcess pid=29772) INFO 10-21 15:37:38 multiproc_worker_utils.py:244] Worker exiting (VllmWorkerProcess pid=29774) INFO 10-21 15:37:38 multiproc_worker_utils.py:244] Worker exiting (VllmWorkerProcess pid=29771) INFO 10-21 15:37:38 multiproc_worker_utils.py:244] Worker exiting (VllmWorkerProcess pid=29773) INFO 10-21 15:37:38 multiproc_worker_utils.py:244] Worker exiting /usr/lib/python3.12/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown warnings.warn('resource_tracker: There appear to be %d ' ERROR 10-21 15:37:40 multiproc_wo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e** ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: le_prefix_caching --max_model_len 8192 **returns the error:** INFO: Waiting for application startup. INFO: Application startup complete. ERROR: [Errno 98] error while attempting to bind on address ('0.0.0.0', 8000): add...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: onse_ ### 🐛 Describe the bug **the command:** vllm serve MODELPATH --dtype auto --api-key TOKEN --tensor-parallel-size 4 --pipeline-parallel-size 2 --gpu-memory-utilization 0.90 --enable_prefix_caching --max_model_len 8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
