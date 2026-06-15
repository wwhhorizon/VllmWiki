# vllm-project/vllm#10969: [Bug]: ngram Speculation for LlamaForCausalLM Models Fails due to Sampler

| 字段 | 值 |
| --- | --- |
| Issue | [#10969](https://github.com/vllm-project/vllm/issues/10969) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ngram Speculation for LlamaForCausalLM Models Fails due to Sampler

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using ngram speculation with Llama-70B-Instruct, vLLM fails due to the LlamaForCausalLM object missing the sampler attribute. I serve the model with the following command: ``` vllm serve {model_path} \ --served-model-name Llama-70B-Instruct \ --host 0.0.0.0 \ --port worker_port \ --device cuda \ --block-size 32 \ --gpu-memory-utilization 0.9 \ --enable-prefix-caching \ --guided-decoding-backend outlines \ --cpu-offload-gb 0 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 3 \ --distributed-executor-backend ray \ --speculative_model [ngram] \ --num_speculative_tokens 10 ``` This is the traceback: ``` [rank0]: Traceback (most recent call last): [rank0]: File "/usr/local/bin/vllm", line 8, in [rank0]: sys.exit(main()) [rank0]: ^^^^^^ [rank0]: File "/usr/local/lib/python3.12/site-packages/vllm/scripts.py", line 195, in main [rank0]: args.dispatch_function(args) [rank0]: File "/usr/local/lib/python3.12/site-packages/vllm/scripts.py", line 41, in serve [rank0]: uvloop.run(run_server(args)) [rank0]: File "/usr/local/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run [rank0]:...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gpu-memory-utilization 0.9 \ --enable-prefix-caching \ --guided-decoding-backend outlines \ --cpu-offload-gb 0 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 3 \ --distributed-executor-backend ray \ --speculative...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: packages/uvloop/__init__.py", line 109, in run [rank0]: return __asyncio.run( [rank0]: ^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/asyncio/runners.py", line 194, in run [rank0]: return runner.run(main) [rank...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ngram Speculation for LlamaForCausalLM Models Fails due to Sampler bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using ngram speculation with Llama-70B-Ins...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : ngram Speculation for LlamaForCausalLM Models Fails due to Sampler bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using ngram speculation with Llama-70B-Instruct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ame Llama-70B-Instruct \ --host 0.0.0.0 \ --port worker_port \ --device cuda \ --block-size 32 \ --gpu-memory-utilization 0.9 \ --enable-prefix-caching \ --guided-decoding-backend outlines \ --cpu-offload-gb 0 \ --tenso...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
