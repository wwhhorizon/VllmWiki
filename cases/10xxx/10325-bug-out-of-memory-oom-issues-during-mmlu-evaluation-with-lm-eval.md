# vllm-project/vllm#10325: [Bug]: Out of Memory (OOM) Issues During MMLU Evaluation with lm_eval

| 字段 | 值 |
| --- | --- |
| Issue | [#10325](https://github.com/vllm-project/vllm/issues/10325) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;sampling |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Out of Memory (OOM) Issues During MMLU Evaluation with lm_eval

### Issue 正文摘录

### Your current environment vllm 0.6.0 lm_eval 0.4.5 torch 2.4 A100 + CUDA 12.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Description:** When using lm_eval for MMLU accuracy evaluation tasks, I frequently encounter OOM errors. This issue seems to be model-specific, and many models are prone to this problem. For example, even when running the Meta-Llama-8B-Instruct model on an A100 GPU (https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct), OOM errors still occur. I have verified that offline inference with this model works fine, meaning both my software and hardware are capable of running the model. However, when using lm_eval, the system encounters OOM issues. Specifically, when the batch size is set to auto, the system behaves similarly to the benchmark_throughput scenario: all requests are placed in the pool, and vllm continuously fetches requests for inference, followed by result analysis. Upon further investigation, I discovered that the discrepancy between the maximum memory usage reported by the [profile_run ](https://github.com/vllm-project/vllm/blob/32e7db25365415841ebc7c4215851743fbb1bad1/vllm/worker/model_runner.py#L1045C9-L1045C20) function an...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Bug]: Out of Memory (OOM) Issues During MMLU Evaluation with lm_eval bug;stale ### Your current environment vllm 0.6.0 lm_eval 0.4.5 torch 2.4 A100 + CUDA 12.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: g;stale ### Your current environment vllm 0.6.0 lm_eval 0.4.5 torch 2.4 A100 + CUDA 12.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Description:** When using lm_eval for MMLU accuracy evaluation tasks,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nt environment vllm 0.6.0 lm_eval 0.4.5 torch 2.4 A100 + CUDA 12.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Description:** When using lm_eval for MMLU accuracy evaluation tasks, I frequently encounte...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: asks, I frequently encounter OOM errors. This issue seems to be model-specific, and many models are prone to this problem. For example, even when running the Meta-Llama-8B-Instruct model on an A100 GPU (https://huggingf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: Out of Memory (OOM) Issues During MMLU Evaluation with lm_eval bug;stale ### Your current environment vllm 0.6.0 lm_eval 0.4.5 torch 2.4 A100 + CUDA 12.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
