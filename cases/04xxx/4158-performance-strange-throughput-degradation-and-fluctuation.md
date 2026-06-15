# vllm-project/vllm#4158: [Performance]: strange throughput degradation and fluctuation

| 字段 | 值 |
| --- | --- |
| Issue | [#4158](https://github.com/vllm-project/vllm/issues/4158) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: strange throughput degradation and fluctuation

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression At the begining there is a high throughput when processing 8 parallel requests: ![image](https://github.com/vllm-project/vllm/assets/4468773/ab64919a-5d43-4f65-8ada-9c716f40a842) For unknown reason, the throughtput falls from ~350 tokens/s to ~30 tokens/s followed by a rise to ~300 tokens/s again. ![image](https://github.com/vllm-project/vllm/assets/4468773/fa48f6b1-bf25-43d9-8b71-7f43e308822a) The low throughput lasted about 15 minutes. During the period, I use a `parallel -j8 ...` command to keep sending requests. Command to launch the server: ```bash python -m vllm.entrypoints.openai.api_server --port 8000 \ --model /path/to/Qwen-1.5-72B-chat/ \ --served-model-name qwen-7b \ --tokenizer-mode auto \ --trust-remote-code \ --pipeline-parallel-size 1 \ --tensor-parallel-size 8 \ --gpu-memory-utilization 0.8 ``` ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: it is necessary) ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```bash python -m vllm.entrypoints.openai.api_server --port 8000 \ --model /path/to/Qwen-1.5-72B-chat/ \ --served-model-name qwen-7b \ --tokenizer-mode auto \ --trust-remote-code \ --pipeline-parallel-size 1 \ --tensor-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Performance]: strange throughput degradation and fluctuation performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression At the begining there is a high throughput when proce...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Performance]: strange throughput degradation and fluctuation performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression At the begining there is a high throughput when proc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
