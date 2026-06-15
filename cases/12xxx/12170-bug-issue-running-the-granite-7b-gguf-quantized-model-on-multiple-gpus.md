# vllm-project/vllm#12170: [Bug]:  Issue running the Granite-7b GGUF quantized model on multiple GPUs with vLLM due to a tensor size mismatch.

| 字段 | 值 |
| --- | --- |
| Issue | [#12170](https://github.com/vllm-project/vllm/issues/12170) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Issue running the Granite-7b GGUF quantized model on multiple GPUs with vLLM due to a tensor size mismatch.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to load andrun [Granite-7b GGUF quantized](https://huggingface.co/instructlab/granite-7b-lab-GGUF) model on multi gpus in openshift/k8s cluster , but I'm encountering a tensor size mismatch error while model is being loaded. ### NOTE: 1. **The issue is not observed when using a single GPU to load the model; it loads and able to performs inference without any issues.** 2. **The issue is also observed and ca be reproduced in the current master branch.** ### Configurations: ```python args: - '--port=8080' - '--distributed-executor-backend=mp' - '--model=/mnt/models/granite-7b-lab-Q4_K_M.gguf' - '--tensor-parallel-size=2' - '--max-model-len=4096' - '--uvicorn-log-level=debug' - '--served-model-name=granite-7b-lab-gguf' ``` ### Error logs: ```python WARNING 01-17 14:00:06 multiproc_worker_utils.py:312] Reducing Torch parallelism from 40 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed. INFO 01-17 14:00:06 custom_cache_manager.py:17] Setting Triton cache manager to: vllm.triton_utils.custom_cache_manager:CustomCa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Issue running the Granite-7b GGUF quantized model on multiple GPUs with vLLM due to a tensor size mismatch. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: on args: - '--port=8080' - '--distributed-executor-backend=mp' - '--model=/mnt/models/granite-7b-lab-Q4_K_M.gguf' - '--tensor-parallel-size=2' - '--max-model-len=4096' - '--uvicorn-log-level=debug' - '--served-model-nam...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ogs: ```python WARNING 01-17 14:00:06 multiproc_worker_utils.py:312] Reducing Torch parallelism from 40 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this valu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: b GGUF quantized model on multiple GPUs with vLLM due to a tensor size mismatch. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to load andrun [Granite-7b GGUF qua...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [0;0m INFO 01-17 14:00:06 multiproc_worker_utils.py:222] Worker ready; awaiting tasks [1;36m(VllmWorkerProcess pid=354)[0;0m INFO 01-17 14:00:07 utils.py:918] Found nccl from library libnccl.so.2 INFO 01-17 14:00:07...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
