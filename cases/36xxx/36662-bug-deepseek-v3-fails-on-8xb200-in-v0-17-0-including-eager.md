# vllm-project/vllm#36662: [Bug]: Deepseek-v3 fails on 8xB200 in v0.17.0 (including eager)

| 字段 | 值 |
| --- | --- |
| Issue | [#36662](https://github.com/vllm-project/vllm/issues/36662) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek-v3 fails on 8xB200 in v0.17.0 (including eager)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Reproduced inside the `vllm/vllm-openai:0.17.0` docker image. ``` $ vllm serve deepseek-ai/DeepSeek-V3 -tp=8 # Also fails in eager $ vllm serve deepseek-ai/DeepSeek-V3 -tp=8 --enforce-eager # TODO checking dp-ep $ vllm serve deepseek-ai/DeepSeek-V3 -dp=8 --enable-expert-parallel --enforce-eager # eval command lm_eval --model local-completions --model_args pretrained=deepseek-ai/DeepSeek-V3,base_url=http://0.0.0.0:8000/v1/completions,num_concurrent=50,max_retries=3 --tasks gsm8k --num_fewshot 5 --batch_size auto --limit 100 ``` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ | 0|± | 0| | | |strict-match | 5|exact_match|↑ | 0|± | 0| ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#36551 [torch.compile] Add support for non-contiguous fused RMSNorm + group quant

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ### 🐛 Describe the bug Reproduced inside the `vllm/vllm-openai:0.17.0` docker image. ``` $ vllm serve deepseek-ai/DeepSeek-V3 -tp=8 # Also fails in eager $ vllm serve deepseek-ai/DeepSeek-V3 -tp=8 --enforce-eager # TODO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Deepseek-v3 fails on 8xB200 in v0.17.0 (including eager) bug ### Your current environment ### 🐛 Describe the bug Reproduced inside the `vllm/vllm-openai:0.17.0` docker image. ``` $ vllm serve deepseek-ai/DeepSeek...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: TODO checking dp-ep $ vllm serve deepseek-ai/DeepSeek-V3 -dp=8 --enable-expert-parallel --enforce-eager # eval command lm_eval --model local-completions --model_args pretrained=deepseek-ai/DeepSeek-V3,base_url=http://0....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: eepseek-ai/DeepSeek-V3 -dp=8 --enable-expert-parallel --enforce-eager # eval command lm_eval --model local-completions --model_args pretrained=deepseek-ai/DeepSeek-V3,base_url=http://0.0.0.0:8000/v1/completions,num_conc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;nan_inf env_dependency #36551 [torch.compile] Add support for non-contiguous fused RMSNorm + group quant Your current environme...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36551](https://github.com/vllm-project/vllm/pull/36551) | mentioned | 0.6 | [torch.compile] Add support for non-contiguous fused RMSNorm + group quant | 5\|exact_match\|↑ \| 0.91\|± \|0.0288\| lm-eval appears broken for DSv3 (#36662), fix in #36296. Below results include this PR ``` $ vllm serve deepseek-ai/DeepSeek-V3 $ lm_eval --model… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
