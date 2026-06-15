# vllm-project/vllm#9290: [Bug]:  Out of memory with large multi-step and large gpu-memory-utilization values - `--num-scheduler-steps 16 --gpu-memory-utilization 0.941` 

| 字段 | 值 |
| --- | --- |
| Issue | [#9290](https://github.com/vllm-project/vllm/issues/9290) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Out of memory with large multi-step and large gpu-memory-utilization values - `--num-scheduler-steps 16 --gpu-memory-utilization 0.941` 

### Issue 正文摘录

### Your current environment ### Model Input Dumps The .pkl is 28G and takes too long to upload. As an alternative, I removed dump mechanism and let the stack-trace print to the terminal - Check the bug description. ### 🐛 Describe the bug vLLM built from source - commit e4d652ea3ed (October 10) I encounter a crash with the following server and client command. Server command: ``` python3 -m vllm.entrypoints.openai.api_server -tp 4 --model ~/models/Meta-Llama-3-70B-Instruct --port 8000 --disable-log-stats --disable-log-requests --gpu-memory-utilization 0.941 --max-num-seqs 512 --dtype bfloat16 --num-scheduler-steps 16 --multi-step-stream-outputs true ``` Client command ``` python3 benchmark_serving.py --backend vllm --model ~/models/Meta-Llama-3-70B-Instruct --dataset-name sharegpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 500 --port 8000 --request-rate inf --ignore-eos ``` Stack Trace: ``` ERROR 10-11 12:27:29 engine.py:157] OutOfMemoryError('CUDA out of memory. Tried to allocate 138.00 MiB. GPU 0 has a total capacity of 79.15 GiB of which 2.19 MiB is free. Including non-PyTorch memory, this process has 79.12 GiB memory in use. Of the allocated memory...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: y with large multi-step and large gpu-memory-utilization values - `--num-scheduler-steps 16 --gpu-memory-utilization 0.941` bug;stale ### Your current environment ### Model Input Dumps The .pkl is 28G and takes too long...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 'CUDA out of memory. Tried to allocate 138.00 MiB. GPU 0 has a total capacity of 79.15 GiB of which 2.19 MiB is free. Including non-PyTorch memory, this process has 79.12 GiB memory in use. Of the allocated memory 71.57...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: isable-log-requests --gpu-memory-utilization 0.941 --max-num-seqs 512 --dtype bfloat16 --num-scheduler-steps 16 --multi-step-stream-outputs true ``` Client command ``` python3 benchmark_serving.py --backend vllm --model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: and takes too long to upload. As an alternative, I removed dump mechanism and let the stack-trace print to the terminal - Check the bug description. ### 🐛 Describe the bug vLLM built from source - commit e4d652ea3ed (Oc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uts true ``` Client command ``` python3 benchmark_serving.py --backend vllm --model ~/models/Meta-Llama-3-70B-Instruct --dataset-name sharegpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 500...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
