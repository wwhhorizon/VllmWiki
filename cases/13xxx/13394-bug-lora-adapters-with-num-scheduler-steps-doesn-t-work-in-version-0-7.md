# vllm-project/vllm#13394: [Bug]:Lora Adapters with num-scheduler-steps doesn't work in version 0.7.2, even with VLLM_USE_V1=0

| 字段 | 值 |
| --- | --- |
| Issue | [#13394](https://github.com/vllm-project/vllm/issues/13394) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Lora Adapters with num-scheduler-steps doesn't work in version 0.7.2, even with VLLM_USE_V1=0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running an OpenAI-compatible server with both the `--enable-lora` and `--num-scheduler-steps` flags results in a "RuntimeError: LoRA is not enabled" exception, even when `VLLM_USE_V1=0`. Command to reproduce the bug:: ```bash docker run --gpus all -e CUDA_VISIBLE_DEVICES=0,1,2,3 -e VLLM_ALLOW_RUNTIME_LORA_UPDATING=True -e VLLM_USE_V1=0 --ipc=host -p 8000:8000 -v /dev/shm:/dev/shm vllm/vllm-openai:v0.7.2 --model Qwen/Qwen2.5-Coder-32B-Instruct --tensor-parallel-size 4 --disable-log-stats --dtype bfloat16 --enable-lora --lora-modules dummy-adapter= --max-model-len 4096 --num-scheduler-steps 8 ``` Stack trace: ``` (VllmWorkerProcess pid=349) ERROR 02-17 01:38:54 multiproc_worker_utils.py:242] Exception in worker VllmWorkerProcess while processing method add_lora. (VllmWorkerProcess pid=349) ERROR 02-17 01:38:54 multiproc_worker_utils.py:242] Traceback (most recent call last): (VllmWorkerProcess pid=349) ERROR 02-17 01:38:54 multiproc_worker_utils.py:242] File "/usr/local/lib/python3.12/dist-packages/vllm/executor/multiproc_worker_utils.py", line 236, in _run_worker_process (VllmWorkerProcess pid=349) ERROR 02-17 01:38:54 multiproc_w...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]:Lora Adapters with num-scheduler-steps doesn't work in version 0.7.2, even with VLLM_USE_V1=0 bug;stale ### Your current environment ### 🐛 Describe the bug Running an OpenAI-compatible server with both the `--enab...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]:Lora Adapters with num-scheduler-steps doesn't work in version 0.7.2, even with VLLM_USE_V1=0 bug;stale ### Your current environment ### 🐛 Describe the bug Running an OpenAI-compatible server with both the `--enab...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: wen2.5-Coder-32B-Instruct --tensor-parallel-size 4 --disable-log-stats --dtype bfloat16 --enable-lora --lora-modules dummy-adapter= --max-model-len 4096 --num-scheduler-steps 8 ``` Stack trace: ``` (VllmWorkerProcess pi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: --ipc=host -p 8000:8000 -v /dev/shm:/dev/shm vllm/vllm-openai:v0.7.2 --model Qwen/Qwen2.5-Coder-32B-Instruct --tensor-parallel-size 4 --disable-log-stats --dtype bfloat16 --enable-lora --lora-modules dummy-adapter= --ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _V1=0`. Command to reproduce the bug:: ```bash docker run --gpus all -e CUDA_VISIBLE_DEVICES=0,1,2,3 -e VLLM_ALLOW_RUNTIME_LORA_UPDATING=True -e VLLM_USE_V1=0 --ipc=host -p 8000:8000 -v /dev/shm:/dev/shm vllm/vllm-opena...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
