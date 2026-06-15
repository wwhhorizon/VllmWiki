# vllm-project/vllm#20780: [Bug]: Eagle 3 has 20-30% higher AL but only ~5% faster than Eagle 1

| 字段 | 值 |
| --- | --- |
| Issue | [#20780](https://github.com/vllm-project/vllm/issues/20780) |
| 状态 | closed |
| 标签 | bug;speculative-decoding |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Eagle 3 has 20-30% higher AL but only ~5% faster than Eagle 1

### Issue 正文摘录

### Your current environment[/+] ### 🐛 Describe the bug Eagle 3 is expected to be much faster than Eagle 1. We can see 20-30% better Acceptance Length for K=3/4. Practically, we should compare the e2e gains for the optimal K for E1 and E3. For llama 3.1 8b, E1 has optimal K=3 and E3 has optimal K=4. This means E3 is better than E1 by only ~5% on their best config. Is this expected? | AL | | -- | -- | -- | -- K | Eagle 1 | Eagle 3 | Gain % 2 | 2.1 | 2.36 | 1.123809524 3 | 2.29 | 2.79 | 1.218340611 4 | 2.39 | 3.08 | 1.288702929 5 | 2.43 | 3.32 | 1.366255144 6 | 2.45 | 3.46 | 1.412244898 7 | 2.47 | 3.54 | 1.433198381 | TPOT ms | | | | | -- | -- | -- | -- | -- | -- | -- BS 1 | vanilla | EAGLE 1 | EAGLE 3 | | E1 over vanilla | E3 over E1 K=2 | 7.07 | 4.37 | 4.32 | | 1.61784897 | 1.011574074 K=3 | 7.07 | 4.29 | 4.09 | | 1.648018648 | 1.048899756 K=4 | 7.07 | 4.48 | 4.05 | | 1.567627494 | 1.10617284 K=5 | 7.07 | 4.71 | 4.13 | | 1.61047836 | 1.140435835 K=6 | 7.07 | 4.94 | 4.2 | | 1.543668122 | 1.176190476 K=7 | 7.07 | 5.2 | 4.29 | | 1.359615385 | 1.212121212 Best TPOT | 7.07 | 4.29 | 4.05 | | | 1.059259259 Best K | | 3 | 4 | | | ### Commands to repro ``` # eagle VLLM_USE_V1=1 vllm serve...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ly, we should compare the e2e gains for the optimal K for E1 and E3. For llama 3.1 8b, E1 has optimal K=3 and E3 has optimal K=4. This means E3 is better than E1 by only ~5% on their best config. Is this expected? | AL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Eagle 3 has 20-30% higher AL but only ~5% faster than Eagle 1 bug;speculative-decoding ### Your current environment[/+] ### 🐛 Describe the bug Eagle 3 is expected to be much faster than Eagle 1. We can see 20-30%...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: path philschmid/mt-bench --num-prompts 80 --print-output ``` development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda build_error env_dependency Your current environment[/+]
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 6255144 6 | 2.45 | 3.46 | 1.412244898 7 | 2.47 | 3.54 | 1.433198381 | TPOT ms | | | | | -- | -- | -- | -- | -- | -- | -- BS 1 | vanilla | EAGLE 1 | EAGLE 3 | | E1 over vanilla | E3 over E1 K=2 | 7.07 | 4.37 | 4.32 | | 1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: POT python3 benchmarks/benchmark_serving.py --port 9001 --save-result --backend vllm --model meta-llama/Llama-3.1-8B-Instruct --endpoint /v1/completions --dataset-name hf --dataset-path philschmid/mt-bench --num-prompts...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
