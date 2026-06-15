# vllm-project/vllm#33133: [Bug]: Using GPT OSS 20B as Drafter Throws Error

| 字段 | 值 |
| --- | --- |
| Issue | [#33133](https://github.com/vllm-project/vllm/issues/33133) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Using GPT OSS 20B as Drafter Throws Error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use GPT OSS 20B as the target and GPT OSS 20B as the drafter, I get the error below: "File "/home/ubuntu/test_code/vllm/vllm/v1/spec_decode/eagle.py", line 1312, in validate_same_kv_cache_group (EngineCore_DP0 pid=1006172) ERROR 01-26 23:11:38 [core.py:935] len( (EngineCore_DP0 pid=1006172) ERROR 01-26 23:11:38 [core.py:935] AssertionError: All drafting layers should belong to the same kv cache group" Command to run for reproducing: VLLM_USE_V1=1 python3 examples/offline_inference/spec_decode.py \ --model-dir openai/gpt-oss-20b \ --draft-model openai/gpt-oss-20b \ --method draft_model \ --num_spec_tokens 5 \ --dataset-name hf \ --dataset-path philschmid/mt-bench \ --num_prompts 100 \ --temp 0.0 \ --gpu-memory-utilization 0.9 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: VLLM_USE_V1=1 python3 examples/offline_inference/spec_decode.py \ --model-dir openai/gpt-oss-20b \ --draft-model openai/gpt-oss-20b \ --method draft_model \ --num_spec_tokens 5 \ --dataset-name hf \ --dataset-path phils...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Using GPT OSS 20B as Drafter Throws Error bug;stale ### Your current environment ### 🐛 Describe the bug When I use GPT OSS 20B as the target and GPT OSS 20B as the drafter, I get the error below: "File "/home/ubu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ers should belong to the same kv cache group" Command to run for reproducing: VLLM_USE_V1=1 python3 examples/offline_inference/spec_decode.py \ --model-dir openai/gpt-oss-20b \ --draft-model openai/gpt-oss-20b \ --metho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .9 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: re.py:935] AssertionError: All drafting layers should belong to the same kv cache group" Command to run for reproducing: VLLM_USE_V1=1 python3 examples/offline_inference/spec_decode.py \ --model-dir openai/gpt-oss-20b \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
