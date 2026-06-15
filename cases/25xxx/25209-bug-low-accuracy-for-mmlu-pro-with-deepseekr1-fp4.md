# vllm-project/vllm#25209: [Bug]: Low Accuracy for MMLU Pro with DeepSeekR1-FP4

| 字段 | 值 |
| --- | --- |
| Issue | [#25209](https://github.com/vllm-project/vllm/issues/25209) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Low Accuracy for MMLU Pro with DeepSeekR1-FP4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug MMLU-Pro accuracy is quite low with DSR1-FP4 model in simple TP setting Result: ``` vllm (pretrained=/models/DeepSeek-R1-FP4,quantization=modelopt_fp4,tensor_parallel_size=4,max_model_len=32768,gpu_memory_utilization=0.90,add_bos_token=True,trust_remote_code=True), gen_kwargs: (temperature=0.0), limit: 100.0, num_fewshot: 5, batch_size: 512 | Tasks |Version| Filter |n-shot| Metric | |Value | |Stderr| |-------------------|------:|--------------|-----:|-----------|---|-----:|---|-----:| |mmlu_pro | 2.0|custom-extract| |exact_match|↑ |0.2271|± |0.0109| | - biology | 2.1|custom-extract| 5|exact_match|↑ |0.3600|± |0.0482| | - business | 2.1|custom-extract| 5|exact_match|↑ |0.1800|± |0.0386| | - chemistry | 2.1|custom-extract| 5|exact_match|↑ |0.3200|± |0.0469| | - computer_science| 2.1|custom-extract| 5|exact_match|↑ |0.2400|± |0.0429| | - economics | 2.1|custom-extract| 5|exact_match|↑ |0.2900|± |0.0456| | - engineering | 2.1|custom-extract| 5|exact_match|↑ |0.1900|± |0.0394| | - health | 2.1|custom-extract| 5|exact_match|↑ |0.1500|± |0.0359| | - history | 2.1|custom-extract| 5|exact_match|↑ |0.3500|± |0.0479| | - law | 2.1|custom-ex...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 0.0), limit: 100.0, num_fewshot: 5, batch_size: 512 | Tasks |Version| Filter |n-shot| Metric | |Value | |Stderr| |-------------------|------:|--------------|-----:|-----------|---|-----:|---|-----:| |mmlu_pro | 2.0|cust...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Low Accuracy for MMLU Pro with DeepSeekR1-FP4 bug;stale ### Your current environment ### 🐛 Describe the bug MMLU-Pro accuracy is quite low with DSR1-FP4 model in simple TP setting Result: ``` vllm (pretrained=/mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Low Accuracy for MMLU Pro with DeepSeekR1-FP4 bug;stale ### Your current environment ### 🐛 Describe the bug MMLU-Pro accuracy is quite low with DSR1-FP4 model in simple TP setting Result: ``` vllm (pretrained=/mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Low Accuracy for MMLU Pro with DeepSeekR1-FP4 bug;stale ### Your current environment ### 🐛 Describe the bug MMLU-Pro accuracy is quite low with DSR1-FP4 model in simple TP setting Result: ``` vllm (pretrained=/mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
