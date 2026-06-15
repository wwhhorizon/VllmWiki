# vllm-project/vllm#26879: [Bug]: DP start failed: Number of placement groups must match data parallel size

| 字段 | 值 |
| --- | --- |
| Issue | [#26879](https://github.com/vllm-project/vllm/issues/26879) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: DP start failed: Number of placement groups must match data parallel size

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Error occurs when starting vllm instance in DP mode: Number of placement groups must match data parallel size ``` (vllm-dev) root@kebe-gpu-dev-0:~/vllm# ray status ======== Autoscaler status: 2025-10-15 04:45:16.686677 ======== Node status --------------------------------------------------------------- Active: 1 node_beea60aaeb95c97eacecd5abfc8e279cab56b2788c7fa71da449ea0f 1 node_d3984e3edfa7e0bc3fa282290068e7cce70e605baa0a3a17c4bf5208 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Total Usage: 0.0/128.0 CPU (0.0 used of 2.0 reserved in placement groups) 0.0/12.0 GPU (0.0 used of 2.0 reserved in placement groups) 0B/469.80GiB memory 0B/19.00GiB object_store_memory Total Constraints: (no request_resources() constraints) Total Demands: (no resource demands) (vllm-dev) root@kebe-gpu-dev-0:~/vllm# vllm serve /home/jovyan/qwen3-30b-a3b/ --served-model-name=model --tensor-parallel-size=1 --data-parallel-size=2 --enable-expert-parallel --trust-remote-code --enforce-eager --data_parallel_backend=ray --enable-eplb ... (APIServer pid=26246) File "/home/jo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: odel-name=model --tensor-parallel-size=1 --data-parallel-size=2 --enable-expert-parallel --trust-remote-code --enforce-eager --data_parallel_backend=ray --enable-eplb ... (APIServer pid=26246) File "/home/jovyan/vllm/vl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: able-expert-parallel --trust-remote-code --enforce-eager --data_parallel_backend=ray --enable-eplb ... (APIServer pid=26246) File "/home/jovyan/vllm/vllm/v1/engine/utils.py", line 271, in __init__ (APIServer pid=26246)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: demands) (vllm-dev) root@kebe-gpu-dev-0:~/vllm# vllm serve /home/jovyan/qwen3-30b-a3b/ --served-model-name=model --tensor-parallel-size=1 --data-parallel-size=2 --enable-expert-parallel --trust-remote-code --enforce-eag...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
