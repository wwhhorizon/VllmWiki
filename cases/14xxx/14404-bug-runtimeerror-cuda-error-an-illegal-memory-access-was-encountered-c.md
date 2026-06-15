# vllm-project/vllm#14404: [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered  cos_sin = self.cos_sin_cache[torch.add(positions, offsets)

| 字段 | 值 |
| --- | --- |
| Issue | [#14404](https://github.com/vllm-project/vllm/issues/14404) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered  cos_sin = self.cos_sin_cache[torch.add(positions, offsets)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 12345 --max-model-len 131072 --max-num-batched-tokens 2048 --trust-remote-code --tensor-parallel-size 8 --gpu-memory-utilization 0.98 --served-model-name deepseek-reasoner --model /data/DeepSeek-R1-AWQ/cognitivecomputations/DeepSeek-R1-awq/ --enable-chunked-prefill --quantization moe_wna16 --max-num-seqs 16 python3 benchmark_serving.py --backend openai --model deepseek-reasoner --tokenizer /data/DeepSeek-R1-AWQ/cognitivecomputations/DeepSeek-R1-awq/ --dataset-name random --num-prompts 10000 --request-rate 20 --port 12345 --random-input-len 1024 --random-output-len 100 --ignore-eos 1;36m(VllmWorker rank=5 pid=33503)[0;0m ERROR 03-06 06:49:30 [multiproc_executor.py:375] WorkerProc hit an exception: %s [1;36m(VllmWorker rank=5 pid=33503)[0;0m ERROR 03-06 06:49:30 [multiproc_executor.py:375] Traceback (most recent call last): [1;36m(VllmWorker rank=5 pid=33503)[0;0m ERROR 03-06 06:49:30 [multiproc_executor.py:375] File "/workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 371, in worker_busy_loop [1;36m(VllmWorker rank=5 pid=33503)[0;0m...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ountered cos_sin = self.cos_sin_cache[torch.add(positions, offsets) bug;stale ### Your current environment ### 🐛 Describe the bug VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 12345 -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rank=5 pid=33503)[0;0m ERROR 03-06 06:49:30 [multiproc_executor.py:375] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. [1;36m(VllmWorker rank=5 pid=33503)[0;0m ERROR 03-06 06:49:30 [multiproc_exe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: CUDA error: an illegal memory access was encountered cos_sin = self.cos_sin_cache[torch.add(positions, offsets) bug;stale ### Your current environment ### 🐛 Describe the bug VLLM_USE_V1=1 python3 -m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ble-chunked-prefill --quantization moe_wna16 --max-num-seqs 16 python3 benchmark_serving.py --backend openai --model deepseek-reasoner --tokenizer /data/DeepSeek-R1-AWQ/cognitivecomputations/DeepSeek-R1-awq/ --dataset-n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uantization moe_wna16 --max-num-seqs 16 python3 benchmark_serving.py --backend openai --model deepseek-reasoner --tokenizer /data/DeepSeek-R1-AWQ/cognitivecomputations/DeepSeek-R1-awq/ --dataset-name random --num-prompt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
