# vllm-project/vllm#17470: [Usage]:  OOM happend when run DeepSeek-R1-BF16 with 80k max model len by 16 gpu/90G memory

| 字段 | 值 |
| --- | --- |
| Issue | [#17470](https://github.com/vllm-project/vllm/issues/17470) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:  OOM happend when run DeepSeek-R1-BF16 with 80k max model len by 16 gpu/90G memory

### Issue 正文摘录

### Your current environment ```text we run deepseek-r1-bf16 with vllm 0.7.3 and cuda 12.6 ,16 gpu but oom happend. here is parammetes: nohup python -m vllm.entrypoints.openai.api_server \ --model /models/DeepSeek-R1-BF16 \ --port 2000 \ --dtype bfloat16 \ --tensor-parallel-size 16 \ --trust-remote-code \ --gpu-memory-utilization 0.975 \ --distributed-executor-backend=mp \ --max-model-len 80000 \ --swap-size 80 \ --enforce-eager \ --block-size 16 \ --served-model-name dsr1bf16 &> /models/start.log & Any suggestions? ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: OOM happend when run DeepSeek-R1-BF16 with 80k max model len by 16 gpu/90G memory usage;stale ### Your current environment ```text we run deepseek-r1-bf16 with vllm 0.7.3 and cuda 12.6 ,16 gpu but oom happend....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: urrent environment ```text we run deepseek-r1-bf16 with vllm 0.7.3 and cuda 12.6 ,16 gpu but oom happend. here is parammetes: nohup python -m vllm.entrypoints.openai.api_server \ --model /models/DeepSeek-R1-BF16 \ --por...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: p \ --max-model-len 80000 \ --swap-size 80 \ --enforce-eager \ --block-size 16 \ --served-model-name dsr1bf16 &> /models/start.log & Any suggestions? ``` ### How would you like to use vllm I want to run inference of a [...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: emote-code \ --gpu-memory-utilization 0.975 \ --distributed-executor-backend=mp \ --max-model-len 80000 \ --swap-size 80 \ --enforce-eager \ --block-size 16 \ --served-model-name dsr1bf16 &> /models/start.log & Any sugg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
