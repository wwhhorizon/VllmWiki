# vllm-project/vllm#33134: [Bug]: try to run vllm bench with "throughput", got error.

| 字段 | 值 |
| --- | --- |
| Issue | [#33134](https://github.com/vllm-project/vllm/issues/33134) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: try to run vllm bench with "throughput", got error.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug try to run vllm bench with "throughput", got error. suppose my vllm version 0.8.0 is too old? vllm bench throughput INFO 01-25 21:29:06 [__init__.py:239] Automatically detected platform cuda. usage: vllm bench [options] vllm bench: error: argument bench_type: invalid choice: 'throughput' (choose from serve) root@ins-drlwc-69f685db5b-9kfmr:vllm bench throughput --help INFO 01-25 21:29:20 [__init__.py:239] Automatically detected platform cuda. usage: vllm bench [options] vllm bench: error: argument bench_type: invalid choice: 'throughput' (choose from serve) root@ins-drlwc-69f685db5b-9kfmr:~/data/Qwen# python3 -m vllm.entrypoints.cli.main bench throughput --help INFO 01-25 21:29:39 [__init__.py:239] Automatically detected platform cuda. usage: vllm bench [options] main.py bench: error: argument bench_type: invalid choice: 'throughput' (choose from serve) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g try to run vllm bench with "throughput", got error. suppose my vllm version 0.8.0 is too old? vllm bench throughput INFO 01-25 21:29:06 [__init__.py:239] Automatically detected platform cuda. usage: vllm bench [option...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ut INFO 01-25 21:29:06 [__init__.py:239] Automatically detected platform cuda. usage: vllm bench [options] vllm bench: error: argument bench_type: invalid choice: 'throughput' (choose from serve) root@ins-drlwc-69f685db...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 'throughput' (choose from serve) root@ins-drlwc-69f685db5b-9kfmr:~/data/Qwen# python3 -m vllm.entrypoints.cli.main bench throughput --help INFO 01-25 21:29:39 [__init__.py:239] Automatically detected platform cuda. usag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: try to run vllm bench with "throughput", got error. bug;stale ### Your current environment ### 🐛 Describe the bug try to run vllm bench with "throughput", got error. suppose my vllm version 0.8.0 is too old? vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: try to run vllm bench with "throughput", got error. bug;stale ### Your current environment ### 🐛 Describe the bug try to run vllm bench with "throughput", got error. suppose my vllm version 0.8.0 is too old? vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
