# vllm-project/vllm#18619: [Bug][PERF]: Qwen2.5 performance degradation 0.8.4 -> 0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#18619](https://github.com/vllm-project/vllm/issues/18619) |
| 状态 | closed |
| 标签 | bug;stale;qwen |
| 评论 | 39; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][PERF]: Qwen2.5 performance degradation 0.8.4 -> 0.8.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I found a performance degradation for Qwen2.5 model 0.8.4 vs 0.8.5. vllm serve run command: ``` vllm serve Qwen/Qwen2.5-VL-3B-Instruct --disable-log-requests --max-num-seqs 1024 --block-size 16 --max-num-batched-tokens 2048 --no-enable-prefix-caching ``` bench run command: ``` vllm bench serve --model Qwen/Qwen2.5-VL-3B-Instruct --request-rate 200 --num-prompts 1000 --random-input-len 600 --random-output-len 125 --ignore-eos ``` **Results of 7 runs** 0.8.4 ``` Throughput values: 62.75, 63.09, 62.81, 62.78, 62.90, 62.79, 61.42 Median throughput: 62.79 req/s Standard error: 0.21 (0.33%) ``` 0.8.5 ``` Throughput values: 57.87, 57.91, 57.71, 57.74, 57.98, 57.80, 57.74 Median throughput: 57.80 req/s Standard error: 0.04 (0.07%) ``` Degradation is **8.6%** **Profile analysis.** I see sufficient increase in time we spend in attn. 0.8.4 ![Image](https://github.com/user-attachments/assets/3e328875-612b-46dd-977b-227eedceef76) 0.8.5 ![Image](https://github.com/user-attachments/assets/723238c8-f8ff-4988-b991-d9342d17d605) Percentage we spend in attn increased from 14.2% to 38.8% ### Before submitting a new issue... - [x] Make sure you alrea...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 4 (0.07%) ``` Degradation is **8.6%** **Profile analysis.** I see sufficient increase in time we spend in attn. 0.8.4 ![Image](https://github.com/user-attachments/assets/3e328875-612b-46dd-977b-227eedceef76) 0.8.5 ![Ima...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug][PERF]: Qwen2.5 performance degradation 0.8.4 -> 0.8.5 bug;stale;qwen ### Your current environment ### 🐛 Describe the bug I found a performance degradation for Qwen2.5 model 0.8.4 vs 0.8.5. vllm serve run command:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: -random-output-len 125 --ignore-eos ``` **Results of 7 runs** 0.8.4 ``` Throughput values: 62.75, 63.09, 62.81, 62.78, 62.90, 62.79, 61.42 Median throughput: 62.79 req/s Standard error: 0.21 (0.33%) ``` 0.8.5 ``` Throug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 8% ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: wen/Qwen2.5-VL-3B-Instruct --disable-log-requests --max-num-seqs 1024 --block-size 16 --max-num-batched-tokens 2048 --no-enable-prefix-caching ``` bench run command: ``` vllm bench serve --model Qwen/Qwen2.5-VL-3B-Instr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
