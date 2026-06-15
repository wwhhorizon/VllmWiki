# vllm-project/vllm#19101: [Bug]: Deepseek-R1 with DEP16 hangs after kv cache allocation

| 字段 | 值 |
| --- | --- |
| Issue | [#19101](https://github.com/vllm-project/vllm/issues/19101) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek-R1 with DEP16 hangs after kv cache allocation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run DSR1 with DEP16 on 2 nodes 8xH100 each. On node 1 (10.52.51.17): ```bash vllm serve deepseek-ai/DeepSeek-R1 --served_model_name deepseek-ai/DeepSeek- R1 --data_parallel_size 16 --data_parallel_size_local 8 --data_parallel_address 10.52.51.17 --data_parallel_rpc_port 13345 --max -model-len 10240 --enable-expert-parallel ``` On node 2: ```bash vllm serve deepseek-ai/DeepSeek-R1 --served_model_name deepseek-ai/DeepSeek-R1 - -data_parallel_size 16 --data_parallel_size_local 8 --data_parallel_address 10.52.51.17 --data_parallel_rpc_port 13345 --max-mod el-len 10240 --enable-expert-parallel --data_parallel_start_rank 8 --headless & ``` The model is loading weights, running torch compile and allocating kv cache, then hangs with 100% GPU utilization until NCCL timeout error. Full logs attached. [node1.txt](https://github.com/user-attachments/files/20579635/node1.txt) [node2.txt](https://github.com/user-attachments/files/20579634/node2.txt) Same happens without EP. TP16 with Ray is working fine. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: art_rank 8 --headless & ``` The model is loading weights, running torch compile and allocating kv cache, then hangs with 100% GPU utilization until NCCL timeout error. Full logs attached. [node1.txt](https://github.com/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### 🐛 Describe the bug I am trying to run DSR1 with DEP16 on 2 nodes 8xH100 each. On node 1 (10.52.51.17): ```bash vllm serve deepseek-ai/DeepSeek-R1 --served_model_name deepseek-ai/DeepSeek- R1 --data_parallel_size 16...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 52.51.17 --data_parallel_rpc_port 13345 --max -model-len 10240 --enable-expert-parallel ``` On node 2: ```bash vllm serve deepseek-ai/DeepSeek-R1 --served_model_name deepseek-ai/DeepSeek-R1 - -data_parallel_size 16 --da...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Deepseek-R1 with DEP16 hangs after kv cache allocation bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to run DSR1 with DEP16 on 2 nodes 8xH100 each. On node 1 (10.52.51.17): ```bash vll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rt;moe;sampling_logits;scheduler_memory cache;cuda;moe;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
