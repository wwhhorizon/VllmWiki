# vllm-project/vllm#25582: [Bug]: support the Qwen3-VL-235B-A22B model？

| 字段 | 值 |
| --- | --- |
| Issue | [#25582](https://github.com/vllm-project/vllm/issues/25582) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;gemm;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: support the Qwen3-VL-235B-A22B model？

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I attempted to run the Qwen3-VL model on vLLM with the following command: `vllm serve /home/qspace/base_model_Qwen3-VL-235B-A22B-Instruct_export --served-model-name Qwen3-VL-235B-A22B --tensor-parallel-size 4 --pipeline-parallel-size 2 --limit-mm-per-prompt '{ "image":8, "video":1}'` However, I encountered an error. ``` (Worker_PP0_TP2 pid=72464) INFO 09-24 20:54:47 [gpu_model_runner.py:2539] Starting to load model /home/qspace/base_model_Qwen3-VL-235B-A22B-Instruct_export... (Worker_PP0_TP0 pid=72462) INFO 09-24 20:54:48 [gpu_model_runner.py:2539] Starting to load model /home/qspace/base_model_Qwen3-VL-235B-A22B-Instruct_export... (Worker_PP1_TP0 pid=72466) INFO 09-24 20:54:48 [gpu_model_runner.py:2539] Starting to load model /home/qspace/base_model_Qwen3-VL-235B-A22B-Instruct_export... (Worker_PP1_TP2 pid=72468) INFO 09-24 20:54:48 [gpu_model_runner.py:2539] Starting to load model /home/qspace/base_model_Qwen3-VL-235B-A22B-Instruct_export... (Worker_PP1_TP1 pid=72467) INFO 09-24 20:54:48 [gpu_model_runner.py:2539] Starting to load model /home/qspace/base_model_Qwen3-VL-235B-A22B-Instruct_export... (Worker_PP1_TP3 pid=72469) INF...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: support the Qwen3-VL-235B-A22B model？ bug ### Your current environment ### 🐛 Describe the bug I attempted to run the Qwen3-VL model on vLLM with the following command: `vllm serve /home/qspace/base_model_Qwen3-VL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ch... (Worker_PP0_TP0 pid=72462) INFO 09-24 20:54:48 [cuda.py:347] Using Flash Attention backend on V1 engine. (Worker_PP1_TP2 pid=72468) INFO 09-24 20:54:48 [cuda.py:347] Using Flash Attention backend on V1 engine. (Wo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding attention;cuda;gemm;moe;operator;triton build_error...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: File "/mnt/cephfs/user_xuanweifu/vllm/vllm/model_executor/models/qwen3_moe.py", line 699, in load_weights (Worker_PP1_TP3 pid=72469) ERROR 09-24 20:54:49 [multiproc_executor.py:597] return loader.load_weights(weights) (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng model from scratch... (Worker_PP0_TP0 pid=72462) INFO 09-24 20:54:48 [cuda.py:347] Using Flash Attention backend on V1 engine. (Worker_PP1_TP2 pid=72468) INFO 09-24 20:54:48 [cuda.py:347] Using Flash Attention backen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
