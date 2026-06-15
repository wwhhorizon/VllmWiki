# vllm-project/vllm#10296: [Bug]:  VLLLm crash when running Qwen/Qwen2.5-Coder-32B-Instruct on two H100 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#10296](https://github.com/vllm-project/vllm/issues/10296) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  VLLLm crash when running Qwen/Qwen2.5-Coder-32B-Instruct on two H100 GPUs

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLLm crash when running Qwen/Qwen2.5-Coder-32B-Instruct on two H100 GPUs Command for reprduce: ```bash sudo docker run --gpus all -e CUDA_VISIBLE_DEVICES=0,1 -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN --ipc=host -p 8000:8000 -v /dev/shm:/dev/shm -v /nvme/.tritoncache/:/root/.triton/cache -v /nvme:/nvme -v $HF_HOME:/root/.cache/huggingface vllm/vllm-openai:v0.6.3.post1 --model Qwen/Qwen2.5-Coder-32B-Instruct --tensor-parallel-size 2 --disable-log-stats --dtype bfloat16 --max-model-len 8192 --swap-space 128 --disable-log-requests --enable-chunked-prefill=false ``` Error message: ``` (VllmWorkerProcess pid=347) ERROR 11-13 05:09:12 multiproc_worker_utils.py:229] Exception in worker VllmWorkerProcess while processing method start_worker_execution_loop. (VllmWorkerProcess pid=347) ERROR 11-13 05:09:12 multiproc_worker_utils.py:229] Traceback (most recent call last): (VllmWorkerProcess pid=347) ERROR 11-13 05:09:12 multiproc_worker_utils.py:229] File "/usr/local/lib/python3.12/dist-packages/vllm/executor/multiproc_worker_utils.py", line 223, in _run_worker_process (VllmWorkerProcess pid=347)...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: 8192 --swap-space 128 --disable-log-requests --enable-chunked-prefill=false ``` Error message: ``` (VllmWorkerProcess pid=347) ERROR 11-13 05:09:12 multiproc_worker_utils.py:229] Exception in worker VllmWorkerProcess wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: crash when running Qwen/Qwen2.5-Coder-32B-Instruct on two H100 GPUs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLLm crash when running Qwen/Qwen2.5-Coder-32B-Instr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: -Coder-32B-Instruct on two H100 GPUs Command for reprduce: ```bash sudo docker run --gpus all -e CUDA_VISIBLE_DEVICES=0,1 -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN --ipc=host -p 8000:8000 -v /dev/shm:/dev/shm -v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: VLLLm crash when running Qwen/Qwen2.5-Coder-32B-Instruct on two H100 GPUs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLLm crash when running Qwen/Qwen2.5-Co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: G_FACE_HUB_TOKEN --ipc=host -p 8000:8000 -v /dev/shm:/dev/shm -v /nvme/.tritoncache/:/root/.triton/cache -v /nvme:/nvme -v $HF_HOME:/root/.cache/huggingface vllm/vllm-openai:v0.6.3.post1 --model Qwen/Qwen2.5-Coder-32B-I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
