# vllm-project/vllm#13582: Using VLLM0.7.2 server to start DeepSeek-R1 model on 8xNVIDIA-H200, there is a phenomenon of cuda out of memory and service shutting down.

| 字段 | 值 |
| --- | --- |
| Issue | [#13582](https://github.com/vllm-project/vllm/issues/13582) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Using VLLM0.7.2 server to start DeepSeek-R1 model on 8xNVIDIA-H200, there is a phenomenon of cuda out of memory and service shutting down.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running "vllm serve" command with DeepSeek_R1 on 8xNVIDIA-H200 always cause CUDA out-of-memory error. ```shell PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True nohup vllm serve /export/dp/DeepSeek-R1 --tensor-parallel-size 8 --trust-remote-code --max_num_seqs 32 --max_model_len 6000 --enable_chunked_prefill --gpu_memory_utilization 0.97 --max_num_batched_tokens 4000 > /export/vllmserve_fp8.log 2>&1 & ``` The parameters used above actually works on another 8xNVIDIA-H20 machine(successful load & stable service). The content of "/export/vllmserve_fp8.log" is in the attachment below. [vllmserve_fp8.log](https://github.com/user-attachments/files/18880237/vllmserve_fp8.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er to start DeepSeek-R1 model on 8xNVIDIA-H200, there is a phenomenon of cuda out of memory and service shutting down. bug ### Your current environment ### 🐛 Describe the bug Running "vllm serve" command with DeepSeek_R...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rust-remote-code --max_num_seqs 32 --max_model_len 6000 --enable_chunked_prefill --gpu_memory_utilization 0.97 --max_num_batched_tokens 4000 > /export/vllmserve_fp8.log 2>&1 & ``` The parameters used above actually work...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;oom env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: emory_utilization 0.97 --max_num_batched_tokens 4000 > /export/vllmserve_fp8.log 2>&1 & ``` The parameters used above actually works on another 8xNVIDIA-H20 machine(successful load & stable service). The content of "/ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
