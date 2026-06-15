# vllm-project/vllm#6750: [Usage]: deploy Llama3.1 405B-Instruct-FP8 with H800 * 8 not work

| 字段 | 值 |
| --- | --- |
| Issue | [#6750](https://github.com/vllm-project/vllm/issues/6750) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;gemm_linear;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;fp8;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: deploy Llama3.1 405B-Instruct-FP8 with H800 * 8 not work

### Issue 正文摘录

### My current environment - 8 * H800 - CUDA 11.8 - vllm 0.5.3post1 - python 3.9 I'm using vllm to deploy llama3 405B-instruct-FP8，But when deployed, it report an error: ``` INFO 07-24 22:52:39 multiproc_worker_utils.py:136] Terminating local vLLM worker processes (VllmWorkerProcess pid=28011) ERROR 07-24 22:52:39 multiproc_worker_utils.py:226] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks: Expected a.dtype() == torch::kInt8 to be true, but got false. (Could this error message be improved? If so, please report an enhancement request to PyTorch.), Traceback (most recent call last): (VllmWorkerProcess pid=28011) ERROR 07-24 22:52:39 multiproc_worker_utils.py:226] File "/usr/local/lib/python3.9/site-packages/vllm/executor/multiproc_worker_utils.py", line 223, in _run_worker_process (VllmWorkerProcess pid=28013) ERROR 07-24 22:52:39 multiproc_worker_utils.py:226] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks: Expected a.dtype() == torch::kInt8 to be true, but got false. (Could this error message be improved? If so, please report an enhancement request to PyTorch.), Traceback (most recent call...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Usage]: deploy Llama3.1 405B-Instruct-FP8 with H800 * 8 not work usage;stale ### My current environment - 8 * H800 - CUDA 11.8 - vllm 0.5.3post1 - python 3.9 I'm using vllm to deploy llama3 405B-instruct-FP8，But when d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: deploy Llama3.1 405B-Instruct-FP8 with H800 * 8 not work usage;stale ### My current environment - 8 * H800 - CUDA 11.8 - vllm 0.5.3post1 - python 3.9 I'm using vllm to deploy llama3 405B-instruct-FP8，But when d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: deploy Llama3.1 405B-Instruct-FP8 with H800 * 8 not work usage;stale ### My current environment - 8 * H800 - CUDA 11.8 - vllm 0.5.3post1 - python 3.9 I'm using vllm to deploy llama3 405B-instruct-FP8，But when d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: worker VllmWorkerProcess while processing method determine_num_available_blocks: Expected a.dtype() == torch::kInt8 to be true, but got false. (Could this error message be improved? If so, please report an enhancement r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 8011) ERROR 07-24 22:52:39 multiproc_worker_utils.py:226] return ops.cutlass_scaled_mm(qinput, (VllmWorkerProcess pid=28012) ERROR 07-24 22:52:39 multiproc_worker_utils.py:226] return apply_fp8_linear(input=x, (VllmWork...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
