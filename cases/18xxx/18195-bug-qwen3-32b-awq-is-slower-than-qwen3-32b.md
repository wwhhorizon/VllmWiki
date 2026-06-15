# vllm-project/vllm#18195: [Bug]: Qwen3-32B-AWQ is slower than Qwen3-32B

| 字段 | 值 |
| --- | --- |
| Issue | [#18195](https://github.com/vllm-project/vllm/issues/18195) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-32B-AWQ is slower than Qwen3-32B

### Issue 正文摘录

### My current environment I use Evalscope to Test Qwen3-32B-AWQ & Qwen3-32B's Inference Performance. I use my private cloud for serving. VLLM version :0.8.5 post1 Qwen3-32B-AWQ serving argument: python3 -m vllm.entrypoints.openai.api_server \ --model /data/model \ --served-model-name Qwen3-32B-AWQ \ --max-num-seqs 8192 \ --quantization awq_marlin \ --enable-reasoning \ --reasoning-parser deepseek_r1 \ --trust-remote-code \ --port 8501 \ --dtype bfloat16 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --gpu-memory-utilization 0.9 Qwen3-32B serving argument: python3 -m vllm.entrypoints.openai.api_server \ --model /data/model \ --served-model-name Qwen3-32B \ --tensor-parallel-size 2 \ --max-num-seqs 8192 \ --trust-remote-code \ --port 8501 \ --dtype bfloat16 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --gpu-memory-utilization 0.9 Both instance uses 2 A100 80G with tp 2. ### 🐛 Describe the bug evalscope serving performance(evalscope perf --number 1000 --parallel 250 ) test: 1000 requests in total , 250 concurrency, dataset:openqa, max-output-length 240 (coordinate with Qwen2.5 output length) Qwen3-32B-AWQ result: ![Image](https://github.com/user-attachments/a...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --served-model-name Qwen3-32B-AWQ \ --max-num-seqs 8192 \ --quantization awq_marlin \ --enable-reasoning \ --reasoning-parser deepseek_r1 \ --trust-remote-code \ --port 8501 \ --dtype bfloat16 \ --enable-auto-tool-choic...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l-parser hermes \ --gpu-memory-utilization 0.9 Both instance uses 2 A100 80G with tp 2. ### 🐛 Describe the bug evalscope serving performance(evalscope perf --number 1000 --parallel 250 ) test: 1000 requests in total , 2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-32B-AWQ is slower than Qwen3-32B bug;stale ### My current environment I use Evalscope to Test Qwen3-32B-AWQ & Qwen3-32B's Inference Performance. I use my private cloud for serving. VLLM version :0.8.5 post1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3-32B-AWQ is slower than Qwen3-32B bug;stale ### My current environment I use Evalscope to Test Qwen3-32B-AWQ & Qwen3-32B's Inference Performance. I use my private cloud for serving. VLLM version :0.8.5 post1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: AWQ is slower than Qwen3-32B bug;stale ### My current environment I use Evalscope to Test Qwen3-32B-AWQ & Qwen3-32B's Inference Performance. I use my private cloud for serving. VLLM version :0.8.5 post1 Qwen3-32B-AWQ se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
