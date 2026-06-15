# vllm-project/vllm#29871: [Usage]: Extremly low token input speed for DeepSeek-R1-Distill-Llama-70B

| 字段 | 值 |
| --- | --- |
| Issue | [#29871](https://github.com/vllm-project/vllm/issues/29871) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Extremly low token input speed for DeepSeek-R1-Distill-Llama-70B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am currently using vllm to benchmark several (10+) LLMs. I am running the latest version (0.11.2). I am experiencing severe performance issues for one particular model (`deepseek-ai/DeepSeek-R1-Distill-Llama-70B`). I am running on 8 H100 GPUs with 80GB RAM each. I am running 2 instances of the model on 4 GPUs each. When logging on error level I notice extreme drops in token input speeds after the first few requests: ``` # Initial Processed prompts: 100% | 25/25 [05:08 , 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['all'], 'splitting_ops': None, 'compile_mm_encod er': False, 'use_inductor': None, 'compile_sizes': [], 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': , 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': [], 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_cudagraph_capture_size': 0, 'local_cache_dir': None} ``` I have seen the same drops when...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ntly using vllm to benchmark several (10+) LLMs. I am running the latest version (0.11.2). I am experiencing severe performance issues for one particular model (`deepseek-ai/DeepSeek-R1-Distill-Llama-70B`). I am running...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Extremly low token input speed for DeepSeek-R1-Distill-Llama-70B usage;stale ### Your current environment ### 🐛 Describe the bug I am currently using vllm to benchmark several (10+) LLMs. I am running the lates...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: r model (`deepseek-ai/DeepSeek-R1-Distill-Llama-70B`). I am running on 8 H100 GPUs with 80GB RAM each. I am running 2 instances of the model on 4 GPUs each. When logging on error level I notice extreme drops in token in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : Extremly low token input speed for DeepSeek-R1-Distill-Llama-70B usage;stale ### Your current environment ### 🐛 Describe the bug I am currently using vllm to benchmark several (10+) LLMs. I am running the latest versi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mp_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['all'], 'splitting_ops': None, 'compile_mm_encod er': False, 'use_inductor': None, 'compile_sizes': [], 'indu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
