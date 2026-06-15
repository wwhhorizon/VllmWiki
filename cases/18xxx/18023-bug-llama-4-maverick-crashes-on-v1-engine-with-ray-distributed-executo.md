# vllm-project/vllm#18023: [Bug]: Llama-4-Maverick crashes on V1 engine (with Ray distributed executor)

| 字段 | 值 |
| --- | --- |
| Issue | [#18023](https://github.com/vllm-project/vllm/issues/18023) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama-4-Maverick crashes on V1 engine (with Ray distributed executor)

### Issue 正文摘录

### Your current environment Forward passes with Maverick served across two 8xH100 nodes are crashing on V1 engine, but running fine on V0. Here are the steps to reproduce the error: 1. follow vllm docs from https://docs.vllm.ai/en/latest/serving/distributed_serving.html#running-vllm-on-multiple-nodes to enable vllm on multiple nodes (I'm using vllm/vllm-openai image with 0.8.5.post1) 2. serve the model with `--distributed-executor-backend ray` (without it, vllm engine falls back to V0): ```bash vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct -tp 8 -pp 2 --dtype auto --max-model-len 4096 --gpu-memory-utilization 0.8 --enable-chunked-prefill --distributed-executor-backend ray ``` 4. send some GSM8k requests (requires installing `pip install lmeval[api]`) ```bash lm_eval \ --model local-completions \ --model_args model="meta-llama/Llama-4-Maverick-17B-128E-Instruct",base_url=""http://localhost:8000/v1/completions"",max_retries=3,timeout=300,tokenized_requests=True,add_bos_token=True,max_length=4096,max_gen_tokens=512,num_concurrent=1 \ --tasks gsm8k \ --num_fewshot 5 \ --write_out \ --log_samples \ --output_path ${OUTPUT_BASE_PTH}/${CKPT}/${TASK}/${TAG} \ --show_config ```...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ur current environment Forward passes with Maverick served across two 8xH100 nodes are crashing on V1 engine, but running fine on V0. Here are the steps to reproduce the error: 1. follow vllm docs from https://docs.vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Llama-4-Maverick crashes on V1 engine (with Ray distributed executor) bug;ray;stale ### Your current environment Forward passes with Maverick served across two 8xH100 nodes are crashing on V1 engine, but running...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: -4-Maverick crashes on V1 engine (with Ray distributed executor) bug;ray;stale ### Your current environment Forward passes with Maverick served across two 8xH100 nodes are crashing on V1 engine, but running fine on V0....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: reproduce the error: 1. follow vllm docs from https://docs.vllm.ai/en/latest/serving/distributed_serving.html#running-vllm-on-multiple-nodes to enable vllm on multiple nodes (I'm using vllm/vllm-openai image with 0.8.5....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: image with 0.8.5.post1) 2. serve the model with `--distributed-executor-backend ray` (without it, vllm engine falls back to V0): ```bash vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct -tp 8 -pp 2 --dtype auto...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
