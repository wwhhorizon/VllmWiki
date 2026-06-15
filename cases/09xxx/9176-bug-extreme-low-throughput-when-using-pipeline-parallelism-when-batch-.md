# vllm-project/vllm#9176: [Bug]: Extreme low throughput when using pipeline parallelism when Batch Size(running req) is small

| 字段 | 值 |
| --- | --- |
| Issue | [#9176](https://github.com/vllm-project/vllm/issues/9176) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Extreme low throughput when using pipeline parallelism when Batch Size(running req) is small

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running Command: ``` python api_server.py --model=/data/Meta-Llama-3___1-8B-Instruct \ -tp 1 \ -pp 2 \ --max-num-seqs 256 \ --dtype bfloat16 \ --max-num-batched-tokens 2048 \ --enable-chunked-prefill \ --enforce-eager \ --gpu-memory-utilization 0.85 ``` Request clients number : 64 input token number: 6000 max out token number:256 **large batch prompt throughput(mix infer)**(prompt throughput is as expected): **large batch decoding throughput**(relatively low): **small batch decoding throughput**(extremely low): I have investigated the potential bottlenecks in serving process, including tensor parallelism (TP) reduce operations when TP is greater than 1, pipeline parallelism (PP) intermediate result transmission, input preparation, and sampling. My analysis reveals that all these components are performing as expected, with one exception: the model's forward pass on **pp rank 0 and tp rank 0** appears to be significantly slower than anticipated (no communication happened here when TP=1 which is wierd). When TP is greater than 1, model forward in all TP ranks in PP rank 0 are slow, but PP rank 1 i...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: hen using pipeline parallelism when Batch Size(running req) is small bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running Command: ``` python api_server.py --model=/d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: **pp rank 0 and tp rank 0** appears to be significantly slower than anticipated (no communication happened here when TP=1 which is wierd). When TP is greater than 1, model forward in all TP ranks in PP rank 0 are slow,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ta/Meta-Llama-3___1-8B-Instruct \ -tp 1 \ -pp 2 \ --max-num-seqs 256 \ --dtype bfloat16 \ --max-num-batched-tokens 2048 \ --enable-chunked-prefill \ --enforce-eager \ --gpu-memory-utilization 0.85 ``` Request clients nu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Extreme low throughput when using pipeline parallelism when Batch Size(running req) is small bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running Command: ```...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ize(running req) is small bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running Command: ``` python api_server.py --model=/data/Meta-Llama-3___1-8B-Instruct \ -tp 1 \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
