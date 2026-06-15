# vllm-project/vllm#26191: [Bug]: Performance Regression in Acceptance length for EAGLE3

| 字段 | 值 |
| --- | --- |
| Issue | [#26191](https://github.com/vllm-project/vllm/issues/26191) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Performance Regression in Acceptance length for EAGLE3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The acceptance length of EAGLE3 on `main` is lower than it used to be. ```shell python examples/offline_inference/spec_decode.py \ --model-dir meta-llama/Llama-3.1-8B-Instruct \ --eagle-dir yuhuili/EAGLE3-LLaMA3.1-Instruct-8B \ --method eagle3 \ --num_spec_tokens 7 \ --dataset-name hf \ --dataset-path philschmid/mt-bench \ --num_prompts 80 \ --temp 0.0 ``` According to previous measurements, like https://github.com/vllm-project/vllm/pull/17504#issuecomment-2845707371, confirmed here: https://github.com/vllm-project/vllm/pull/24322 Previous AL=3.53 ```shell total_num_output_tokens: 16990 num_drafts: 4816 num_draft_tokens: 33712 num_accepted_tokens: 12208 mean acceptance length: 3.53 -------------------------------------------------- acceptance at token 0: 0.74 acceptance at token 1: 0.54 acceptance at token 2: 0.41 acceptance at token 3: 0.31 acceptance at token 4: 0.23 acceptance at token 5: 0.17 acceptance at token 6: 0.13 ``` Current AL=3.40 ```shell -------------------------------------------------- total_num_output_tokens: 17028 num_drafts: 5010 num_draft_tokens: 35070 num_accepted_tokens: 12067 mean acceptance length: 3.41 -...

## 现有链接修复摘要

#26498 [Bugfix] Invalidate positions when using padded speculative decoding

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: . ```shell python examples/offline_inference/spec_decode.py \ --model-dir meta-llama/Llama-3.1-8B-Instruct \ --eagle-dir yuhuili/EAGLE3-LLaMA3.1-Instruct-8B \ --method eagle3 \ --num_spec_tokens 7 \ --dataset-name hf \...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: wer than it used to be. ```shell python examples/offline_inference/spec_decode.py \ --model-dir meta-llama/Llama-3.1-8B-Instruct \ --eagle-dir yuhuili/EAGLE3-LLaMA3.1-Instruct-8B \ --method eagle3 \ --num_spec_tokens 7...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Performance Regression in Acceptance length for EAGLE3 bug ### Your current environment ### 🐛 Describe the bug The acceptance length of EAGLE3 on `main` is lower than it used to be. ```shell python examples/offli...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26498](https://github.com/vllm-project/vllm/pull/26498) | mentioned | 0.6 | [Bugfix] Invalidate positions when using padded speculative decoding | g ## Purpose This PR addresses the acceptance rate issue outlined in #26191: AL is reduced by about 5% when long speculative sequences are used. This was not caught previously bec… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
