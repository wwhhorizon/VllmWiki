# vllm-project/vllm#39396: [Usage]: Run:ai S3 streamer crashing when loading model from an S3 compatible object storage

| 字段 | 值 |
| --- | --- |
| Issue | [#39396](https://github.com/vllm-project/vllm/issues/39396) |
| 状态 | open |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Run:ai S3 streamer crashing when loading model from an S3 compatible object storage

### Issue 正文摘录

### Your current environment ```text I'm using k8s with the vllm/vllm-openai:v0.17.0 docker image ``` ### How would you like to use vllm I'm serving kimi-k2.5 with vLLM using run:ai streamer after uploading to Coreweave S3 object compatible storage on H200/B200 nodes ``` vllm serve s3://hf-cache/kimi-k2.5 \ --port "8000" \ --host 0.0.0.0 \ --load-format runai_streamer \ --model-loader-extra-config '{"distributed":true,"memory_limit":10000000000}' \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 \ --trust-remote-code \ --enable-auto-tool-choice \ --tensor-parallel-size 8 \ --max-model-len 262144 \ --decode-context-parallel-size 8 \ ``` I'm also using `AWS_EC2_METADATA_DISABLED: true` It usually works well getting 1GB/s per GPU so around 8GB/s total but issues is happening when we are launching like 10+ servers at the same as the S3 throughput naturally decreases per replica to around 400MB/s per GPU but some servers gets an error while streaming the model with the following error and they keep hanging forever without crashing ``` (Worker pid=1254) (Worker_TP0_DCP0 pid=1254) Loading safetensors using Runai Model Streamer: 6% Completed | 12127/208550 [00:13<03:16, 1001.31it/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Run:ai S3 streamer crashing when loading model from an S3 compatible object storage usage ### Your current environment ```text I'm using k8s with the vllm/vllm-openai:v0.17.0 docker image ``` ### How would you...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: oice \ --tensor-parallel-size 8 \ --max-model-len 262144 \ --decode-context-parallel-size 8 \ ``` I'm also using `AWS_EC2_METADATA_DISABLED: true` It usually works well getting 1GB/s per GPU so around 8GB/s total but is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: reamer after uploading to Coreweave S3 object compatible storage on H200/B200 nodes ``` vllm serve s3://hf-cache/kimi-k2.5 \ --port "8000" \ --host 0.0.0.0 \ --load-format runai_streamer \ --model-loader-extra-config '{...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s happening when we are launching like 10+ servers at the same as the S3 throughput naturally decreases per replica to around 400MB/s per GPU but some servers gets an error while streaming the model with the following e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ent environment ```text I'm using k8s with the vllm/vllm-openai:v0.17.0 docker image ``` ### How would you like to use vllm I'm serving kimi-k2.5 with vLLM using run:ai streamer after uploading to Coreweave S3 object co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
