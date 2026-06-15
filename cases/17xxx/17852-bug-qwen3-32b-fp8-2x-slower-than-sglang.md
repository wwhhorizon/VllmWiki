# vllm-project/vllm#17852: [Bug]: Qwen3-32B-FP8 2x slower than SGLang

| 字段 | 值 |
| --- | --- |
| Issue | [#17852](https://github.com/vllm-project/vllm/issues/17852) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-32B-FP8 2x slower than SGLang

### Issue 正文摘录

### Your current environment VLLM: 0.8.5 SGLang: 0.4.5.post1 Hello. I'm testing the inference speed of Qwen3-32B-FP8 on H20 (96G) vllm command ``` export TP=2 model=model/Qwen3-32B-FP8 vllm serve $model --tensor-parallel-size $TP --max-num-seqs 1024 --port 8080 --host 0.0.0.0 ``` sglang command ``` server_host=0.0.0.0 server_port=8090 model_path=model/Qwen3-32B-FP8 tp=2 export CUDA_VISIBLE_DEVICES=6,7 python -m sglang.launch_server \ --host ${server_host} \ --port ${server_port} \ --model ${model_path} \ --tp ${tp} \ --mem-fraction 0.9 \ --random-seed 42 \ --max-running-requests 1024 ``` I'm testing with random token ids (input 512/output 512, concurrent 32) Here is TPOT(s): | vllm | sglang | boost -- | -- | -- | -- offline FP8 | 0.032 | 0.016 | 200% online FP8 | 0.026 | 0.024 | 108% BF16 | 0.032 | 0.030 | 106% offline FP8: Qwen3-32B-FP8 online FP8: Qwen3-32B with --quantization fp8 BF16: Qwen3-32B ### 🐛 Describe the bug I found vllm is 32ms while sglang is 16ms, which is 2x faster than vllm. What's more, when I switched to bf16 precision, vllm is the same as fp8. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot l...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3-32B-FP8 2x slower than SGLang bug;stale ### Your current environment VLLM: 0.8.5 SGLang: 0.4.5.post1 Hello. I'm testing the inference speed of Qwen3-32B-FP8 on H20 (96G) vllm command ``` export TP=2 model=m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: host=0.0.0.0 server_port=8090 model_path=model/Qwen3-32B-FP8 tp=2 export CUDA_VISIBLE_DEVICES=6,7 python -m sglang.launch_server \ --host ${server_host} \ --port ${server_port} \ --model ${model_path} \ --tp ${tp} \ --m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-32B-FP8 2x slower than SGLang bug;stale ### Your current environment VLLM: 0.8.5 SGLang: 0.4.5.post1 Hello. I'm testing the inference speed of Qwen3-32B-FP8 on H20 (96G) vllm command ``` export TP=2 model=m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3-32B-FP8 2x slower than SGLang bug;stale ### Your current environment VLLM: 0.8.5 SGLang: 0.4.5.post1 Hello. I'm testing the inference speed of Qwen3-32B-FP8 on H20 (96G) vllm command ``` export TP=2 model=m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ## Your current environment VLLM: 0.8.5 SGLang: 0.4.5.post1 Hello. I'm testing the inference speed of Qwen3-32B-FP8 on H20 (96G) vllm command ``` export TP=2 model=model/Qwen3-32B-FP8 vllm serve $model --tensor-parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
