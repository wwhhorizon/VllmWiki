# vllm-project/vllm#19264: [Performance]: The same latency of Qwen3-8B and Qwen3-8b-Fp8B

| 字段 | 值 |
| --- | --- |
| Issue | [#19264](https://github.com/vllm-project/vllm/issues/19264) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: The same latency of Qwen3-8B and Qwen3-8b-Fp8B

### Issue 正文摘录

### Report of performance regression GPU: NVIDIA GeForce RTX 4090 (24G) api serve: vllm serve Qwen/Qwen3-8B(or Qwen3-8B-FP8) --disable-log-requests --gpu-memory-utilization 0.9 --max_model_len 4096 benchmark test: python3 vllm/benchmarks/benchmark_serving.py --model Qwen/Qwen3-8B (or Qwen3-8B-FP8) --backend vllm --dataset-name hf --dataset-path AI-MO/aimo-validation-aime --hf-split train --num-prompts 100 Qwen3-8b ![Image](https://github.com/user-attachments/assets/af00c233-e3a1-49a1-829a-0c2634f04a18) Qwen3-8b-fp8 ![Image](https://github.com/user-attachments/assets/53d8426e-25cf-4451-958a-8d34c7475ed5) req/s of Qwen3-8b is 0.43 ，Qwen3-8b-fp8 is 0.32. Is the test method for quantized networks correct? Quantized model seem not too fast then float model. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text transformers 4.52.3 xformers 0.0.29.post2 torch 2.6.0 vllm 0.8.5.post1 ```

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: The same latency of Qwen3-8B and Qwen3-8b-Fp8B performance;stale ### Report of performance regression GPU: NVIDIA GeForce RTX 4090 (24G) api serve: vllm serve Qwen/Qwen3-8B(or Qwen3-8B-FP8) --disable-log-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: The same latency of Qwen3-8B and Qwen3-8b-Fp8B performance;stale ### Report of performance regression GPU: NVIDIA GeForce RTX 4090 (24G) api serve: vllm serve Qwen/Qwen3-8B(or Qwen3-8B-FP8) --disable-log-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: The same latency of Qwen3-8B and Qwen3-8b-Fp8B performance;stale ### Report of performance regression GPU: NVIDIA GeForce RTX 4090 (24G) api serve: vllm serve Qwen/Qwen3-8B(or Qwen3-8B-FP8) --disable-log-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Performance]: The same latency of Qwen3-8B and Qwen3-8b-Fp8B performance;stale ### Report of performance regression GPU: NVIDIA GeForce RTX 4090 (24G) api serve: vllm serve Qwen/Qwen3-8B(or Qwen3-8B-FP8) --disable-log-r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: marks/benchmark_serving.py --model Qwen/Qwen3-8B (or Qwen3-8B-FP8) --backend vllm --dataset-name hf --dataset-path AI-MO/aimo-validation-aime --hf-split train --num-prompts 100 Qwen3-8b ![Image](https://github.com/user-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
