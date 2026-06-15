# vllm-project/vllm#8369: [Bug]: Crash after few multi image calls

| 字段 | 值 |
| --- | --- |
| Issue | [#8369](https://github.com/vllm-project/vllm/issues/8369) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | runtime_err |
| Operator 关键词 | gemm |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash after few multi image calls

### Issue 正文摘录

### Your current environment Environment was set up by pulling the main branch and building the Dockerfile. Hardware was 4xA100 with an Azure Instance (Standard NC96ads A100 v4). Server image is: ubuntu-hpc (2204) Startup: python3 -m vllm.entrypoints.openai.api_server --port=8000 --host=0.0.0.0 --chat-template="/docker_share/models/internVL2-template.jinja" --model="/fine_tunes/internvl2_76b_hermes2_llama3_70b_dynamic_res_2nd_finetune" --tensor-parallel-size=4 --max-model-len=8192 --trust_remote_code --enforce-eager --max-lora-rank 128 --limit-mm-per-prompt image=4 ### 🐛 Describe the bug I have build from source with the current main branch to use online multi image inference with internVL2 76B (finetuned). First few inferences work with no issue. After like 10 calls the server crashes with following stack trace The issue occurs when callen multithreaded and single threaded. Somehow the bug doesnt happen when i remove --max-lora-rank 128 and set --max-model-len=6000 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## 现有链接修复摘要

#8375 [Bugfix] Fix InternVL2 inference with various num_patches

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: nai.api_server --port=8000 --host=0.0.0.0 --chat-template="/docker_share/models/internVL2-template.jinja" --model="/fine_tunes/internvl2_76b_hermes2_llama3_70b_dynamic_res_2nd_finetune" --tensor-parallel-size=4 --max-mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rrent environment Environment was set up by pulling the main branch and building the Dockerfile. Hardware was 4xA100 with an Azure Instance (Standard NC96ads A100 v4). Server image is: ubuntu-hpc (2204) Startup: python3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: p by pulling the main branch and building the Dockerfile. Hardware was 4xA100 with an Azure Instance (Standard NC96ads A100 v4). Server image is: ubuntu-hpc (2204) Startup: python3 -m vllm.entrypoints.openai.api_server...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm gemm build_error;crash env_dependency #8375 [Bugfix] Fix InternVL2 inference with various num_patches Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm g...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8375](https://github.com/vllm-project/vllm/pull/8375) | closes_keyword | 0.95 | [Bugfix] Fix InternVL2 inference with various num_patches | FIX #8369 **TODO** - [x] Add test to cover these cases. **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- in |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
