# vllm-project/vllm#26142: [Bug]: Memory leak in DeepSeek FP4 on Blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#26142](https://github.com/vllm-project/vllm/issues/26142) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | moe |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Memory leak in DeepSeek FP4 on Blackwell

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run deepseek using the following command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_ATTENTION_BACKEND=FLASHINFER_MLA vllm serve nvidia/DeepSeek-R1-FP4 -tp 4 --max-model-len 32768 --max-num-seqs 1 --no-enable-prefix-caching --port 8049 --gpu-memory-utilization 0.8 --enforce-eager ``` and every request slowly leads to a small amount of gpu memory that does not get reclaimed. I ran a torch memory trace which identified flashinfer's `mm_fp4` as the allocation source, in the shared experts layer the gate_down_proj and up_proj both allocate their own `out = torch.empty(...)` buffers, and these are not being cleared _somehow_. It's unclear why this buffer specifically is not being freed. Flashinfer is built from-source (JIT mode) based on commit `5f783773edc03c72813be513e7e5e42100689442`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Memory leak in DeepSeek FP4 on Blackwell bug ### Your current environment ### 🐛 Describe the bug I run deepseek using the following command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_ATTENTION_BACKEND=FLASHINFER_MLA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: cribe the bug I run deepseek using the following command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_ATTENTION_BACKEND=FLASHINFER_MLA vllm serve nvidia/DeepSeek-R1-FP4 -tp 4 --max-model-len 32768 --max-num-seqs 1 --no-enabl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d these are not being cleared _somehow_. It's unclear why this buffer specifically is not being freed. Flashinfer is built from-source (JIT mode) based on commit `5f783773edc03c72813be513e7e5e42100689442`. ### Before su...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Memory leak in DeepSeek FP4 on Blackwell bug ### Your current environment ### 🐛 Describe the bug I run deepseek using the following command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_ATTENTION_BACKEND=FLASHINFER_MLA...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ug I run deepseek using the following command: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 VLLM_ATTENTION_BACKEND=FLASHINFER_MLA vllm serve nvidia/DeepSeek-R1-FP4 -tp 4 --max-model-len 32768 --max-num-seqs 1 --no-enable-prefix-ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
