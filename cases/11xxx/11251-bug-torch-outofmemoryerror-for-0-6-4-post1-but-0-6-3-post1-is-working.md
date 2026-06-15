# vllm-project/vllm#11251: [Bug]: torch.OutOfMemoryError for 0.6.4.post1 but 0.6.3.post1 is working

| 字段 | 值 |
| --- | --- |
| Issue | [#11251](https://github.com/vllm-project/vllm/issues/11251) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.OutOfMemoryError for 0.6.4.post1 but 0.6.3.post1 is working

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using v100x2(16gx2) to serve the llama3.1 8B model, but i do observe some wired memory phenomenons across 0.6.3.post1 and 0.6.4.post1: 1. the 0.6.4.post1 takes more gpu memory(90% v.s. 80%) when using the following command to launch, this is also showed in this issue: https://github.com/vllm-project/vllm/issues/11230. The command i use is(with just 1 lora module): ` CMD="docker run --gpus all \\ -p ${DEFAULT_PORT}:${DEFAULT_PORT} \\ --ipc=host \\ vllm/vllm-openai:v0.6.x.post1 \\ --model ${MODEL_PATH} \\ --dtype float16 \\ --tensor-parallel_size 2 \\ --gpu-memory-utilization 0.98 \\ --max_model_len 40000 \\ --seed 23 \\ --max-seq-len-to-capture 40000 \\ --port ${DEFAULT_PORT} \\ --disable-log-requests \\ --enable-lora \\ --fully-sharded-loras \\ --max-lora-rank 16 \\ --max-loras ${NUM_LORAS} \\ --lora-modules ${LORA_MODULES}" ` 2. if a send a long context prompt, like nearly 40000 as shown above, the 0.6.3.post1 can work, but 0.6.4.post1 failed with torch.OutOfMemoryError. Even though the 0.6.3.post1 showed fewer gpu kv blocks(about 3000) v.s. 0.6.4.post1(about 5000). The detailed error of 0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vllm/issues/11230. The command i use is(with just 1 lora module): ` CMD="docker run --gpus all \\ -p ${DEFAULT_PORT}:${DEFAULT_PORT} \\ --ipc=host \\ vllm/vllm-openai:v0.6.x.post1 \\ --model ${MODEL_PATH} \\ --dtype flo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: torch.OutOfMemoryError for 0.6.4.post1 but 0.6.3.post1 is working bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm using v100x2(16gx2) to serve the llama3.1 8B mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vllm/vllm-openai:v0.6.x.post1 \\ --model ${MODEL_PATH} \\ --dtype float16 \\ --tensor-parallel_size 2 \\ --gpu-memory-utilization 0.98 \\ --max_model_len 40000 \\ --seed 23 \\ --max-seq-len-to-capture 40000 \\ --port ${...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e, sender) | File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 715, in __call__ | await self.middleware_stack(scope, receive, send) | File "/usr/local/lib/python3.12/dist-packages/starlette/routi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: OR 12-16 21:40:15 multiproc_worker_utils.py:229] torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.02 GiB. GPU 1 has a total capacity of 15.77 GiB of which 1.01 GiB is free. Process 6432 has 14.75 GiB memo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
