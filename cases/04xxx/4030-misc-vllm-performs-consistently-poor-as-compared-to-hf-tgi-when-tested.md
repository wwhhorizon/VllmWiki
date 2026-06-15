# vllm-project/vllm#4030: [Misc]: vLLM performs consistently poor as compared to HF TGI when tested with the DeepSeek Coder Model

| 字段 | 值 |
| --- | --- |
| Issue | [#4030](https://github.com/vllm-project/vllm/issues/4030) |
| 状态 | closed |
| 标签 |  |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: vLLM performs consistently poor as compared to HF TGI when tested with the DeepSeek Coder Model

### Issue 正文摘录

### Anything you want to discuss about vllm. Hello Folks, We are using the Deep Seek Coder model for code completions and chat completions. I did try to run the benchmark scripts for that model both for vLLM and TGI and I see that vLLM metrics are consistently poorer as compared to TGI. Could you please review and comment on the setup ? Bring up the servers: ``` MODEL="deepseek-ai/deepseek-coder-1.3b-instruct" ``` ``` python -m vllm.entrypoints.openai.api_server \ --model ${MODEL} \ --swap-space 16 \ --disable-log-requests ``` ``` (TGI backend) ./launch_tgi_server.sh ${MODEL} 8192 ``` On the client side, run: ``` python benchmarks/benchmark_serving.py \ --backend vllm \ --model ${MODEL} \ --dataset-name sharegpt \ --dataset-path /home/anindya/ShareGPT_V3_unfiltered_cleaned_split.json \ --request-rate 10 \ --num-prompts 1000 \ --save-result ``` ``` python benchmarks/benchmark_serving.py \ --backend tgi \ --model ${MODEL} \ --endpoint /generate_stream \ --dataset-name sharegpt \ --dataset-path /home/anindya/ShareGPT_V3_unfiltered_cleaned_split.json \ --request-rate 10 \ --num-prompts 1000 \ --save-result ``` Results: ``` With DeepSeek Model vLLM Backend ============ Serving Benchmar...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Misc]: vLLM performs consistently poor as compared to HF TGI when tested with the DeepSeek Coder Model ### Anything you want to discuss about vllm. Hello Folks, We are using the Deep Seek Coder model for code completio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Misc]: vLLM performs consistently poor as compared to HF TGI when tested with the DeepSeek Coder Model ### Anything you want to discuss about vllm. Hello Folks, We are using the Deep Seek Coder model for code completio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: EL} \ --swap-space 16 \ --disable-log-requests ``` ``` (TGI backend) ./launch_tgi_server.sh ${MODEL} 8192 ``` On the client side, run: ``` python benchmarks/benchmark_serving.py \ --backend vllm \ --model ${MODEL} \ --d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: _server \ --model ${MODEL} \ --swap-space 16 \ --disable-log-requests ``` ``` (TGI backend) ./launch_tgi_server.sh ${MODEL} 8192 ``` On the client side, run: ``` python benchmarks/benchmark_serving.py \ --backend vllm \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
