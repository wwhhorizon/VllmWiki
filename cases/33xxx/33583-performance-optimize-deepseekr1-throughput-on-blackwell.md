# vllm-project/vllm#33583: [Performance]: Optimize DeepSeekR1 Throughput on Blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#33583](https://github.com/vllm-project/vllm/issues/33583) |
| 状态 | open |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Optimize DeepSeekR1 Throughput on Blackwell

### Issue 正文摘录

### Proposal to improve performance This issue tracks DeepSeekR1 throughput performance optimization on Blackwell, described in vLLM blog: https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html. ## Reproducing Instructions ### Image ``` docker pull ghcr.io/minosfuture/vllm-gb200:custom ``` ### Branch ``` git clone https://github.com/minosfuture/vllm/ --branch pd_gb200_0114 ``` Recipes, slurm scripts, and example logs can be found in the branch: https://github.com/minosfuture/vllm/tree/pd_gb200_0114/runs/DS-R1 ## PRs 1. #30014 @jiahanc 2. #32001 @jiahanc 4. #31171 @jiahanc 5. #32817 @minosfuture 6. #31743 @minosfuture 7. #29941 @minosfuture 8. #29936 @minosfuture 9. #29935 @minosfuture 10. #29710 @minosfuture 11. #26397 @minosfuture ### Benchmark-related PRs 1. #32814 @minosfuture 2. #32808 @minosfuture ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pag...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: Optimize DeepSeekR1 Throughput on Blackwell performance ### Proposal to improve performance This issue tracks DeepSeekR1 throughput performance optimization on Blackwell, described in vLLM blog: https://b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: Optimize DeepSeekR1 Throughput on Blackwell performance ### Proposal to improve performance This issue tracks DeepSeekR1 throughput performance optimization on Blackwell, described in vLLM blog: https://b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: blog: https://blog.vllm.ai/2026/02/03/dsr1-gb200-part1.html. ## Reproducing Instructions ### Image ``` docker pull ghcr.io/minosfuture/vllm-gb200:custom ``` ### Branch ``` git clone https://github.com/minosfuture/vllm/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
