# vllm-project/vllm#11260: [Bug]: vLLM on TPU does not support --pipeline-parallel-size with Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#11260](https://github.com/vllm-project/vllm/issues/11260) |
| 状态 | closed |
| 标签 | bug;tpu;ray;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM on TPU does not support --pipeline-parallel-size with Ray

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I setup v5e-32(8 hosts/4 chips each) and started a ray cluster. output of **ray status** ``` ======== Autoscaler status: 2024-12-17 11:18:22.317629 ======== Node status --------------------------------------------------------------- Active: 1 node_719fd8c930dcd8b932914ebb34d70d16323b468e1f93094a78d50f75 1 node_ac79abf69175ce6f927b5317fe292d22aea9ac4e3c224a7ba42ca6d3 1 node_23a15d4de28063c4a04865b963c54c0a8f29d8e928c298e4021a146b 1 node_153c21365890656c54742efe22e675b89127db7998084e482c8260c6 1 node_cedcf4265be52d297b3d95bab832675688d8241360c819bd9bd63de7 1 node_8993f15ab992801a04a70b5b7c4c691158b949bd7da98c35154aa372 1 node_3723c73cee4bc754265308f5a9f384b493e06b7d76860a739e9ddfb4 1 node_e2823d348a9370bfe108d635330b339b48e4847ce0608af311cd75e2 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Usage: 0.0/880.0 CPU 0.0/32.0 TPU 0.0/1.0 TPU-v5litepod-32-head 0B/1.01TiB memory 0B/449.11GiB object_store_memory 0.0/8.0 tpuvm-01 Demands: (no resource demands) ``` I start serving with below command ``` vllm serve mistrala...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: LM on TPU does not support --pipeline-parallel-size with Ray bug;tpu;ray;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I setup v5e-32(8 hosts/4 chips each) and started a r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: h) and started a ray cluster. output of **ray status** ``` ======== Autoscaler status: 2024-12-17 11:18:22.317629 ======== Node status --------------------------------------------------------------- Active: 1 node_719fd...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: lel-size with Ray bug;tpu;ray;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I setup v5e-32(8 hosts/4 chips each) and started a ray cluster. output of **ray status** ``` ==...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: messages ```text INFO 12-17 09:37:22 api_server.py:643] vLLM API server version 0.6.4.post2.dev378+g69ba344d INFO 12-17 09:37:22 api_server.py:644] args: Namespace(subparser='serve', model_tag='mistralai/Pixtral-Large-I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Dumps _No response_ ### 🐛 Describe the bug I setup v5e-32(8 hosts/4 chips each) and started a ray cluster. output of **ray status** ``` ======== Autoscaler status: 2024-12-17 11:18:22.317629 ======== Node status -------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
