# vllm-project/vllm#27626: [Bug]: gpt-oss-120b with EAGLE3 Speculative decoding, awful benchmarks

| 字段 | 值 |
| --- | --- |
| Issue | [#27626](https://github.com/vllm-project/vllm/issues/27626) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-120b with EAGLE3 Speculative decoding, awful benchmarks

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have been playing around with EAGLE3 speculative decoding with gpt-oss-120b, and I was VERY impressed with the speedup. I wanted to start testing some ideas with speculative decoding, part of which involved beginning with a benchmark(s). Using lm_eval, I ran Humaneval and MMLU, I was surprsised with Humaneval gave me a score of 0.22, and here is the output from the mmlu test | Groups |Version|Filter|n-shot|Metric| |Value | |Stderr| |------------------|------:|------|------|------|---|-----:|---|-----:| |mmlu | 2|none | |acc |↑ |0.2849|± |0.0037| | - humanities | 2|none | |acc |↑ |0.3541|± |0.0067| | - other | 2|none | |acc |↑ |0.2678|± |0.0079| | - social sciences| 2|none | |acc |↑ |0.2395|± |0.0077| | - stem | 2|none | |acc |↑ |0.2426|± |0.0076| I ran both test multiple times with the same results. So I decided to remove the EAGLE3 speculative decoding parts from my deployment and ran again, immediately the numbers were back to where I expected: | Groups |Version|Filter|n-shot|Metric| |Value | |Stderr| |------------------|------:|------|------|------|---|-----:|---|-----:| |mmlu | 2|none | |acc |↑ |0.7266|± |0.0035| | - humani...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: of 0.22, and here is the output from the mmlu test | Groups |Version|Filter|n-shot|Metric| |Value | |Stderr| |------------------|------:|------|------|------|---|-----:|---|-----:| |mmlu | 2|none | |acc |↑ |0.2849|± |0....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gpt-oss-120b with EAGLE3 Speculative decoding, awful benchmarks bug;stale ### Your current environment ### 🐛 Describe the bug I have been playing around with EAGLE3 speculative decoding with gpt-oss-120b, and I w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: gpt-oss-120b with EAGLE3 Speculative decoding, awful benchmarks bug;stale ### Your current environment ### 🐛 Describe the bug I have been playing around with EAGLE3 speculative decoding with gpt-oss-120b, and I w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: gpt-oss-120b with EAGLE3 Speculative decoding, awful benchmarks bug;stale ### Your current environment ### 🐛 Describe the bug I have been playing around with EAGLE3 speculative decoding with gpt-oss-120b, and I w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
