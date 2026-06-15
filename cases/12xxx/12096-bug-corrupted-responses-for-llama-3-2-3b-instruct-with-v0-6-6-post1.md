# vllm-project/vllm#12096: [Bug]: Corrupted responses for Llama-3.2-3B-Instruct with v0.6.6.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#12096](https://github.com/vllm-project/vllm/issues/12096) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Corrupted responses for Llama-3.2-3B-Instruct with v0.6.6.post1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm `v0.6.6.post1` frequently produces corrupted responses when serving [meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct). This typically happens for longer responses. An example of a prompt that seems to have a high probability (>50%) of hitting this is "write a cv for homer simpson". This seems to be a regression as I cannot reproduce this with `v0.6.4.post1` and identical steps. I've observed this on multiple NVIDIA GPUs, including`L40S` and `RTX 4000 SFF`. **Repro** Serve `meta-llama/Llama-3.2-3B-Instruct` with vllm version `v0.6.6.post1`: ``` vllm serve meta-llama/Llama-3.2-3B-Instruct --served-model-name llama-3-2-3b-it ``` Send a request: ```sh curl localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "llama-3-2-3b-it", "messages": [{"role": "user", "content": "write a cv for homer simpson"}], "stream": false }' ``` Response snippet: ... embarked Sol existed trainer Tunisia replacing Wash Bac knowing franchise Premier sun lacked Tight circulating survived polishing policy redund Blocks visibly gorgeous(\n freeway...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 000 SFF`. **Repro** Serve `meta-llama/Llama-3.2-3B-Instruct` with vllm version `v0.6.6.post1`: ``` vllm serve meta-llama/Llama-3.2-3B-Instruct --served-model-name llama-3-2-3b-it ``` Send a request: ```sh curl localhost...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: steps. I've observed this on multiple NVIDIA GPUs, including`L40S` and `RTX 4000 SFF`. **Repro** Serve `meta-llama/Llama-3.2-3B-Instruct` with vllm version `v0.6.6.post1`: ``` vllm serve meta-llama/Llama-3.2-3B-Instruct...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ma/Llama-3.2-3B-Instruct --served-model-name llama-3-2-3b-it ``` Send a request: ```sh curl localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "llama-3-2-3b-it", "messages": [{"role":...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: write a cv for homer simpson". This seems to be a regression as I cannot reproduce this with `v0.6.4.post1` and identical steps. I've observed this on multiple NVIDIA GPUs, including`L40S` and `RTX 4000 SFF`. **Repro**...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: "role": "user", "content": "write a cv for homer simpson"}], "stream": false }' ``` Response snippet: ... embarked Sol existed trainer Tunisia replacing Wash Bac knowing franchise Premier sun lacked Tight circulating su...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
