# vllm-project/vllm#14983: [Bug]: [AMD] [vLLM=0.7.3]  ValueError: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected.

| 字段 | 值 |
| --- | --- |
| Issue | [#14983](https://github.com/vllm-project/vllm/issues/14983) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [AMD] [vLLM=0.7.3]  ValueError: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Followed [AMD-Doc](https://github.com/volcengine/verl/pull/360) It ran for the examples scripts for GRPO on LLMs. However, i'm trying to run for VLMs, ` bash examples/grpo_trainer/run_qwen2_5_vl-7b.sh ` Getting this error : ``` (main_task pid=294091) self.multimodal_config = self._init_multimodal_config( (main_task pid=294091) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (main_task pid=294091) File "/usr/local/lib/python3.12/dist-packages/vllm-0.7.4.dev332+gaf40d336b.rocm631-py3.12-linux-x86_64.egg/vllm/config.py", line 460, in _init_multimodal_config (main_task pid=294091) if self.registry.is_multimodal_model(self.architectures): (main_task pid=294091) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (main_task pid=294091) File "/usr/local/lib/python3.12/dist-packages/vllm-0.7.4.dev332+gaf40d336b.rocm631-py3.12-linux-x86_64.egg/vllm/model_executor/models/registry.py", line 478, in is_multimodal_model (main_task pid=294091) model_cls, _ = self.inspect_model_cls(architectures) (main_task pid=294091) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (main_task pid=294091) File "/usr/local/lib/python3.12/dist-packages/vllm-0.7.4.dev332+gaf40d336b.rocm631...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: [AMD] [vLLM=0.7.3] ValueError: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected. bug;stale ### Your current environment ### 🐛 Describe the bug Followed [AMD-Doc](https://github.co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 0) ERROR 03-17 19:56:11 [registry.py:330] from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs (WorkerDict pid=307390) ERROR 03-17 19:56:11 [registry.py:330] from vllm.executor.executor_base import ExecutorBase...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [AMD] [vLLM=0.7.3] ValueError: Model architectures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected. bug;stale ### Your current environment ### 🐛 Describe the bug Followed [AMD-Doc](https://github.co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tures ['Qwen2_5_VLForConditionalGeneration'] failed to be inspected. bug;stale ### Your current environment ### 🐛 Describe the bug Followed [AMD-Doc](https://github.com/volcengine/verl/pull/360) It ran for the examples...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sked questions. development ci_build;hardware_porting;model_support cuda;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
