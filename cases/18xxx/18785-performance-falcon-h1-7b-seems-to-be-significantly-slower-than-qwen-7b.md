# vllm-project/vllm#18785: [Performance]: Falcon H1 7B seems to be significantly slower than Qwen 7B

| 字段 | 值 |
| --- | --- |
| Issue | [#18785](https://github.com/vllm-project/vllm/issues/18785) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Falcon H1 7B seems to be significantly slower than Qwen 7B

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Hi team! Thanks for the great work. To use the new Falcon H1 models, I've installed vllm, as well as transformers, from source as detailed in the docs (environment information provided below). I have also seperately installed mamba-ssm and causal-conv1d as this made huggingface's SFTTrainer much faster (`pip install --no-build-isolation git+https://github.com/Dao-AILab/causal-conv1d.git@main && pip install git+https://github.com/state-spaces/mamba.git@main`). I'm running the offline throughput benchmarking script as described below and it seems like Falcon H1 7B is much slower than Qwen 7B. Is this expected? **Falcon Test:** ``` python3 vllm/benchmarks/benchmark_throughput.py --model tiiuae/Falcon-H1-7B-Instruct --dataset-name sonnet --dataset-path vllm/benchmarks/sonnet.txt --num-prompts 100 ``` **Falcon Output:** ``` Processed prompts: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:36<00:00, 2.77it/s, est. speed input: 1505.07 toks/s, output: 415.57 toks/s] Throughput: 2.76 requests/s, 1913.92 total tokens/s, 414.11 output...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: team! Thanks for the great work. To use the new Falcon H1 models, I've installed vllm, as well as transformers, from source as detailed in the docs (environment information provided below). I have also seperately instal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ent information provided below). I have also seperately installed mamba-ssm and causal-conv1d as this made huggingface's SFTTrainer much faster (`pip install --no-build-isolation git+https://github.com/Dao-AILab/causal-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Performance]: Falcon H1 7B seems to be significantly slower than Qwen 7B performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi team! Thanks for the great work. To u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: roposal to improve performance _No response_ ### Report of performance regression Hi team! Thanks for the great work. To use the new Falcon H1 models, I've installed vllm, as well as transformers, from source as detaile...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : Falcon H1 7B seems to be significantly slower than Qwen 7B performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi team! Thanks for the great work. To use the new Fa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
