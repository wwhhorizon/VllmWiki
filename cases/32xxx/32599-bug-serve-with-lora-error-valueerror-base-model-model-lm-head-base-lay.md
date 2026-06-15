# vllm-project/vllm#32599: [Bug]: Serve with LoRA error "ValueError: base_model.model.lm_head.base_layer.weight is unsupported LoRA weight"

| 字段 | 值 |
| --- | --- |
| Issue | [#32599](https://github.com/vllm-project/vllm/issues/32599) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Serve with LoRA error "ValueError: base_model.model.lm_head.base_layer.weight is unsupported LoRA weight"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I follow [the document here ](https://docs.vllm.ai/en/stable/features/lora/) and serve the model with lora: ```bash vllm serve meta-llama/Llama-3.2-3B-Instruct \ --enable-lora \ --lora-modules sql-lora=jeeejeee/llama32-3b-text2sql-spider ``` The error message: ``` EngineCore_DP0 pid=14469) ERROR 01-19 20:41:34 [core.py:918] File "/root/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 915, in _handle_client_request (EngineCore_DP0 pid=14469) ERROR 01-19 20:41:34 [core.py:918] result = method(*self._convert_msgspec_args(method, args)) (EngineCore_DP0 pid=14469) ERROR 01-19 20:41:34 [core.py:918] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=14469) ERROR 01-19 20:41:34 [core.py:918] File "/root/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 498, in add_lora (EngineCore_DP0 pid=14469) ERROR 01-19 20:41:34 [core.py:918] return self.model_executor.add_lora(lora_request) (EngineCore_DP0 pid=14469) ERROR 01-19 20:41:34 [core.py:918] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=14469) ERROR 01-19 20:41:34 [core.py:918] File "/root/anaco...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: se_model.model.lm_head.base_layer.weight is unsupported LoRA weight" bug;stale ### Your current environment ### 🐛 Describe the bug I follow [the document here ](https://docs.vllm.ai/en/stable/features/lora/) and serve t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Serve with LoRA error "ValueError: base_model.model.lm_head.base_layer.weight is unsupported LoRA weight" bug;stale ### Your current environment ### 🐛 Describe the bug I follow [the document here ](https://docs.v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
