# vllm-project/vllm#20890: [Performance]: Severe performance on 8x A100 80GB with Qwen3-235B-A22B (v0.9.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#20890](https://github.com/vllm-project/vllm/issues/20890) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Severe performance on 8x A100 80GB with Qwen3-235B-A22B (v0.9.0)

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm vllm server: CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 -m vllm.entrypoints.openai.api_server --host localhost --port 8806 --model /models/Qwen3-235B-A22B --gpu-memory-utilization 0.9 --trust-remote-code --max-model-len 32768 --tensor-parallel-size 8 --dtype float16 --max_num_seqs 128 --max_num_batched_tokens 32768 --disable-log-requests benchmark: python3 benchmark_serving.py --host 0.0.0.0 --port 8806 --backend vllm --dataset-name random --num-prompts 32 --random-input-len 1024 --random-output-len 1024 --model /models/Qwen3-2 35B-A22B --ignore-eos result: ![Image](https://github.com/user-attachments/assets/347171db-1f8d-425f-961a-865ad0745049) I noticed someone was able to achieve over 900 tokens/s throughput using vLLM 0.8.5 on 8×A800 with a batch size of 32, input length of 1k, and output length of 1k. Why am I getting significantly lower performance? Has anyone else managed to achieve 900+ tokens/s throughput under similar conditions? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at th...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: Severe performance on 8x A100 80GB with Qwen3-235B-A22B (v0.9.0) usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm vllm server:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: num_seqs 128 --max_num_batched_tokens 32768 --disable-log-requests benchmark: python3 benchmark_serving.py --host 0.0.0.0 --port 8806 --backend vllm --dataset-name random --num-prompts 32 --random-input-len 1024 --rando...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: st-remote-code --max-model-len 32768 --tensor-parallel-size 8 --dtype float16 --max_num_seqs 128 --max_num_batched_tokens 32768 --disable-log-requests benchmark: python3 benchmark_serving.py --host 0.0.0.0 --port 8806 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Severe performance on 8x A100 80GB with Qwen3-235B-A22B (v0.9.0) usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm vllm server:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : Severe performance on 8x A100 80GB with Qwen3-235B-A22B (v0.9.0) usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm vllm server: CUDA_VISIBLE_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
