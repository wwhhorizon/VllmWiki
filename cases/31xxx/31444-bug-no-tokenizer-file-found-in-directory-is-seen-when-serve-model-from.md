# vllm-project/vllm#31444: [Bug]: "No tokenizer file found in directory" is seen when serve model from local directory after upgrading vllm from 0.11.2 to 0.12

| 字段 | 值 |
| --- | --- |
| Issue | [#31444](https://github.com/vllm-project/vllm/issues/31444) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "No tokenizer file found in directory" is seen when serve model from local directory after upgrading vllm from 0.11.2 to 0.12

### Issue 正文摘录

### Your current environment cuda 128 and vllm 0.12.0, 0.13.0, 0.14 ### 🐛 Describe the bug Issue: running the following command on a machine without outside network connection after downloading the model to /data/models/minimax_m2 from huggingface. It works well in 0.11.2, but it's failed in 0.12, 0.13 and 0.14 ============================================ ``` vllm serve --model /data/models/minimax_m2 --tokenizer /data/models/minimax_m2 --host 0.0.0.0 --port 8004 --tensor-parallel-size 4 --served-model-name minimax_m2 --api-key xxxxx --gpu-memory-utilization 0.95 --tool-call-parser minimax_m2 --reasoning-parser minimax_m2_append_think --enable-auto-tool-choice --trust-remote-code ``` ----------------------------------------------------------------------------- ``` ^[[0;36m(APIServer pid=3604781)^[[0;0m INFO 12-28 04:44:45 [utils.py:253] non-default args: {'model_tag': '/data/models/minimax_m2', 'host': '0.0.0.0', 'port': 8004, 'api_key': ['xxxxx'], 'enable_auto_tool_choice': True, 'tool_call_parser': 'minimax_m2', 'model': '/data/models/minimax_m2', 'tokenizer': '/data/models/minimax_m2', 'trust_remote_code': True, 'served_model_name': ['minimax_m2'], 'reasoning_parser': 'minimax_...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: id=3604781)^[[0;0m INFO 12-28 04:44:52 [model.py:2086] Downcasting torch.float32 to torch.bfloat16. ^[[0;36m(APIServer pid=3604781)^[[0;0m INFO 12-28 04:44:52 [model.py:1750] Using max model len 196608 ^[[0;36m(APIServe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: line 96, in run ^[[0;36m(APIServer pid=3604781)^[[0;0m return __asyncio.run( ^[[0;36m(APIServer pid=3604781)^[[0;0m ~~~~~~~~~~~~~^ ^[[0;36m(APIServer pid=3604781)^[[0;0m wrapper(), ^[[0;36m(APIServer pid=3604781)^[[0;0m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: grading vllm from 0.11.2 to 0.12 bug;stale ### Your current environment cuda 128 and vllm 0.12.0, 0.13.0, 0.14 ### 🐛 Describe the bug Issue: running the following command on a machine without outside network connection...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: "No tokenizer file found in directory" is seen when serve model from local directory after upgrading vllm from 0.11.2 to 0.12 bug;stale ### Your current environment cuda 128 and vllm 0.12.0, 0.13.0, 0.14 ### 🐛 De...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: model from local directory after upgrading vllm from 0.11.2 to 0.12 bug;stale ### Your current environment cuda 128 and vllm 0.12.0, 0.13.0, 0.14 ### 🐛 Describe the bug Issue: running the following command on a machine...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
