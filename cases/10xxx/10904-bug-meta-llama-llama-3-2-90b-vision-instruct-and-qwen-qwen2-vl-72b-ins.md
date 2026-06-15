# vllm-project/vllm#10904: [Bug]: meta-llama/Llama-3.2-90B-Vision-Instruct and Qwen/Qwen2-VL-72B-Instruct models fails with asyncio.exceptions.CancelledError when using wiki image URLs

| 字段 | 值 |
| --- | --- |
| Issue | [#10904](https://github.com/vllm-project/vllm/issues/10904) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: meta-llama/Llama-3.2-90B-Vision-Instruct and Qwen/Qwen2-VL-72B-Instruct models fails with asyncio.exceptions.CancelledError when using wiki image URLs

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Model Serving as follows on 8 A100 80G GPUs Model Serving ```bash setup_environment # Define model parameters export CUDA_LAUNCH_BLOCKING=1 model_name="Llama-3.2-90B-Vision-Instruct" model_command="CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve meta-llama/Llama-3.2-90B-Vision-Instruct --host 127.0.0.1 --port 8000 \ --tensor-parallel-size 8 --gpu-memory-utilization 0.99 \ --disable-log-requests --max-model-len 32768 --enforce-eager \ --multi-step-stream-outputs False --disable-log-stats --max-num-seqs 64 --disable-frontend-multiprocessing \ --ssl-keyfile ~/certificates/mykey.key --ssl-certfile ~/certificates/mycert.crt" log_file="$PWD/logfile_sophia_vllm_${model_name}_$(hostname).log" # Initialize retry counter for the model retry_counter_model_1=0 # Start the model while true; do echo "Starting models sequence..." if ! start_model "$model_name" "$model_command" "$log_file" retry_counter_model_1; then continue # Restart from the beginning if this fails fi echo "All models started successfully." break done ``` OpenAI Client API call ```python from openai import OpenAI import socket import json i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: meta-llama/Llama-3.2-90B-Vision-Instruct and Qwen/Qwen2-VL-72B-Instruct models fails with asyncio.exceptions.CancelledError when using wiki image URLs bug;stale ### Your current environment ### Model Input Dumps...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 90B-Vision-Instruct and Qwen/Qwen2-VL-72B-Instruct models fails with asyncio.exceptions.CancelledError when using wiki image URLs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: tte/middleware/base.py", line 187, in __call__ response = await self.dispatch_func(request, call_next) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/eagle/argonne_tpc/inference-gateway/envs/vllmv0.6.4.post1/lib/py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ps _No response_ ### 🐛 Describe the bug Model Serving as follows on 8 A100 80G GPUs Model Serving ```bash setup_environment # Define model parameters export CUDA_LAUNCH_BLOCKING=1 model_name="Llama-3.2-90B-Vision-Instru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ls with asyncio.exceptions.CancelledError when using wiki image URLs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Model Serving as follows on 8 A100 80G GPUs Model Se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
