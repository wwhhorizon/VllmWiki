# vllm-project/vllm#42354: [Bug]: Distributed inference hanging on a 2 node DGX spark cluster with Mistral 3.5 Medium 128B with TP=2

| 字段 | 值 |
| --- | --- |
| Issue | [#42354](https://github.com/vllm-project/vllm/issues/42354) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Distributed inference hanging on a 2 node DGX spark cluster with Mistral 3.5 Medium 128B with TP=2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran distributed inference with TP=2 with Mistral 3.5 Medium on a 2 node DGX spark cluster with the VLLM nightly docker image vllm/vllm-openai:nightly-fb1ac806c55a6dc96fe92261b80c8550e9c39d2f. I created a Dockerfile to install ray and deployed the cluster using the run_cluster.sh script from the VLLM repo examples. I referred to the DGX Spark playbook for [creating VLLM cluster on two Sparks](https://build.nvidia.com/spark/vllm/stacked-sparks). ```Dockerfile FROM vllm/vllm-openai:nightly-fb1ac806c55a6dc96fe92261b80c8550e9c39d2f RUN pip install ray[default] ``` And served the model using this command ```shell vllm serve mistralai/Mistral-Medium-3.5-128B \ --tensor-parallel-size 2 \ --load-format mistral \ --tokenizer-mode mistral \ --tool-call-parser mistral \ --enable-auto-tool-choice \ --reasoning-parser mistral \ --max-model-len 2048 \ --max_num_seqs 1 \ --gpu_memory_utilization 0.8 \ --distributed-executor-backend ray ``` When testing inference, the first or the second call hangs with one node stuck at 96% GPU utilization and the other one goes to 96% and then drops to 0 after a few seconds. During this time the generation t/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: h Mistral 3.5 Medium on a 2 node DGX spark cluster with the VLLM nightly docker image vllm/vllm-openai:nightly-fb1ac806c55a6dc96fe92261b80c8550e9c39d2f. I created a Dockerfile to install ray and deployed the cluster usi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: fe92261b80c8550e9c39d2f RUN pip install ray[default] ``` And served the model using this command ```shell vllm serve mistralai/Mistral-Medium-3.5-128B \ --tensor-parallel-size 2 \ --load-format mistral \ --tokenizer-mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 0.0 tokens/s, Avg generation throughput: 3.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% (APIServer pid=1071) INFO 05-11 22:50:53 [v1/metrics/loggers.py:271] Engine...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: x_num_seqs 1 \ --gpu_memory_utilization 0.8 \ --distributed-executor-backend ray ``` When testing inference, the first or the second call hangs with one node stuck at 96% GPU utilization and the other one goes to 96% an...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: a few seconds. During this time the generation t/s drop to 0 as well. It reproduces every time. Relevant logs around the hang ```text (APIServer pid=1071) INFO 05-11 22:50:52 [v1/metrics/loggers.py:271] Engine 000: Avg...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
