# vllm-project/vllm#12507: [Bug]: Index out of range error related to speculative decoding and `-O3`

| 字段 | 值 |
| --- | --- |
| Issue | [#12507](https://github.com/vllm-project/vllm/issues/12507) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Index out of range error related to speculative decoding and `-O3`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to run `meta-llama/Llama-3.2-3B-Instruct` with speculative decoding and all the optimizations enabled without success. The intention was to compile the various models we're serving with `--max-num-seqs 1` so I could benchmark it them that setting and in the previous version of vLLM (not the 0.7 in this bug report) this was causing trouble loading the models, also with an index out of range error. Now, it works even with `--max-num-seqs 1`, but it's `--compilation-config 3` that's causing the model compilation to fail. Here is the command to run it: ```bash vllm serve meta-llama/Llama-3.2-3B-Instruct --host 0.0.0.0 --served-model-name meta-llama/Llama-3.2-3B-Instruct --port 23331 --gpu-memory-utilization 0.98 --tensor-parallel-size 8 --num-speculative-tokens 4 --speculative-model neuralmagic/Llama-3.2-1B-Instruct-quantized.w8a8 --max-num-seqs 1 --compilation-config 3 ``` Output of the log file. [Link](https://github.com/user-attachments/files/18572953/output.log). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: and all the optimizations enabled without success. The intention was to compile the various models we're serving with `--max-num-seqs 1` so I could benchmark it them that setting and in the previous version of vLLM (not...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lative decoding and `-O3` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to run `meta-llama/Llama-3.2-3B-Instruct` with speculative decoding and all the opt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Index out of range error related to speculative decoding and `-O3` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to run `meta-llama/Llama-3.2-3B-Ins...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: pile the various models we're serving with `--max-num-seqs 1` so I could benchmark it them that setting and in the previous version of vLLM (not the 0.7 in this bug report) this was causing trouble loading the models, a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
